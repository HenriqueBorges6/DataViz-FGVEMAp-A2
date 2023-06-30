# Import necessary libraries
import pandas as pd
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import ResetTool, Select
from bokeh.layouts import column
from bokeh.models.sources import ColumnDataSource

def box_plot(data_path):
    # Carregar o conjunto de dados
    df = pd.read_csv(data_path)

    # Definir os nomes das colunas
    country_column_name = "Country of Origin"  # Nome da coluna de país
    value_column_name = "Total Cup Points"  # Nome da coluna de valor

    # Agrupar o DataFrame por país e coluna de valor
    group_df = df.groupby(country_column_name)[value_column_name]

    # Criar a figura do box plot
    box_plot = figure(width=900, height=600, y_range=(df[value_column_name].min(), df[value_column_name].max()))

    # Definir os parâmetros do box plot
    x_values = list(range(1, len(group_df) + 1))  # Valores do eixo x
    box_width = 0.7  # Largura dos boxes
    line_width = 1  # Largura das linhas

    # Definir cores para cada país
    colors = [
        "#3fc1bf", "#da3e5b", "#51c15a", "#975ace", "#86b93b", "#af3ea7", "#bdb02e", "#5c6bcc",
        "#db9134", "#5e95cf", "#cd4f31", "#66c08a", "#c03987", "#4a8a36", "#e374d4", "#697329",
        "#bd8ed7", "#aeac5d", "#e75f93", "#37835d", "#8d558c", "#96652c"
    ]

    # Criar a fonte de dados para os box plots
    box_source = ColumnDataSource(data=dict(
        x=x_values,
        top=[values.max() for _, values in group_df],
        bottom=[values.min() for _, values in group_df],
        colors=colors[:len(group_df)]
    ))

    # Plotar os box plots
    box_plot.vbar(source=box_source, x="x", top="top", bottom="bottom", width=box_width,
                fill_color="colors", line_color="black", line_width=line_width)

    # Plotar as hastes (whiskers)
    for x, (_, values) in zip(x_values, group_df):
        iqr = values.quantile(0.75) - values.quantile(0.25)
        lower_whisker = max(values.quantile(0.25) - 1.5 * iqr, df[value_column_name].min())
        upper_whisker = min(values.quantile(0.75) + 1.5 * iqr, df[value_column_name].max())

        box_plot.segment(x, lower_whisker, x, values.min(), line_color="black", line_width=line_width)
        box_plot.segment(x - box_width / 2, lower_whisker, x + box_width / 2, lower_whisker,
                        line_color="black", line_width=line_width)
        box_plot.segment(x, upper_whisker, x, values.max(), line_color="black", line_width=line_width)
        box_plot.segment(x - box_width / 2, upper_whisker, x + box_width / 2, upper_whisker,
                        line_color="black", line_width=line_width)

    # Configurar os eixos, rótulos e fontes no gráfico
    box_plot.xaxis.ticker = x_values
    box_plot.xaxis.major_label_overrides = {x: str(country) for x, country in zip(x_values, group_df.groups.keys())}
    box_plot.xaxis.major_label_orientation = 45
    box_plot.yaxis.axis_label = value_column_name
    box_plot.xaxis.axis_label = "Países"
    box_plot.title.text = "Distribuição de pontos de qualidade por país"
    box_plot.title.align = "center"
    box_plot.title.text_font_size = "12pt"
    box_plot.title.text_font = "Arial"

    # Personalizar o estilo da grade
    box_plot.xgrid.grid_line_color = "#884A39"
    box_plot.ygrid.grid_line_color = "#884A39"
    box_plot.xgrid.grid_line_alpha = 0.3
    box_plot.ygrid.grid_line_alpha = 0.3

    # Adicionar ferramentas interativas
    box_plot.add_tools(ResetTool())

    # Criar o menu suspenso (dropdown)
    countries = ["Todos"] + list(df["Country of Origin"].unique())

    select_dropdown = Select(title="Filtrar por país:", options=countries, value="Todos")

    # Função de retorno de chamada para o menu suspenso
    def select_country_callback(attr, old, new):
        if select_dropdown.value == "Todos":
            new_data = df.copy()  # Criar uma cópia do DataFrame
        else:
            new_data = df[df["Country of Origin"] == select_dropdown.value]

        # Agrupar os novos dados por país e coluna de valor
        new_group_df = new_data.groupby(country_column_name)[value_column_name]

        # Atualizar a fonte de dados usada no gráfico
        box_source.data = dict(
            x=list(range(1, len(new_group_df) + 1)),
            top=[values.max() for _, values in new_group_df],
            bottom=[values.min() for _, values in new_group_df],
            colors=colors[:len(new_group_df)]
        )

        # Atualizar rótulos do eixo x
        box_plot.xaxis.major_label_overrides = {x: str(country) for x, country in zip(x_values, new_group_df.groups.keys())}

        # Limpar as hastes anteriores
        box_plot.renderers = [box_plot.renderers[0]]

        # Plotar as hastes (whiskers) para o país selecionado
        for x, (_, values) in zip(x_values, new_group_df):
            iqr = values.quantile(0.75) - values.quantile(0.25)
            lower_whisker = max(values.quantile(0.25) - 1.5 * iqr, df[value_column_name].min())

            upper_whisker = min(values.quantile(0.75) + 1.5 * iqr, df[value_column_name].max())

            box_plot.segment(x, lower_whisker, x, values.min(), line_color="black", line_width=line_width)

            box_plot.segment(x - box_width / 2, lower_whisker, x + box_width / 2, lower_whisker,
                            line_color="black", line_width=line_width)

            box_plot.segment(x, upper_whisker, x, values.max(), line_color="black", line_width=line_width)

            box_plot.segment(x - box_width / 2, upper_whisker, x + box_width / 2, upper_whisker,
                            line_color="black", line_width=line_width)

    select_dropdown.on_change("value", select_country_callback)

    # Centralizar o gráfico no meio da figura
    box_plot.x_range.start = min(x_values) + 3
    box_plot.x_range.end = max(x_values) - 3

    # Criar o layout
    layout = column(select_dropdown, box_plot)

    # Adicionar o layout ao curdoc
    curdoc().add_root(layout)
