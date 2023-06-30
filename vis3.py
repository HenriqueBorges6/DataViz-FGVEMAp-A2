import pandas as pd
from bokeh.io import show
from bokeh.plotting import figure
from bokeh.models import PanTool, BoxZoomTool, ResetTool

# Carregar o conjunto de dados
df = pd.read_csv("cleaned_coffee_dataset.csv")

country_column = "Country of Origin"
value_column = "Total Cup Points"

# Verificar se a coluna do país existe no DataFrame
if country_column not in df.columns:
    raise KeyError(f"A coluna '{country_column}' não existe no DataFrame.")

# Agrupar o DataFrame por país e coluna de valor
grouped_df = df.groupby(country_column)[value_column]

# Criar a figura do gráfico de caixa
box_plot = figure(width=900, height=700, y_range=(df[value_column].min(), df[value_column].max()))

x_values = list(range(1, len(grouped_df) + 1))
box_width = 0.7
gap_width = 0.2
line_width = 1

# Define cores para cada país
colors = ["#A7727D", "#4D7AA8", "#9A8E99", "#D9B611", "#6A9373"]  # Adicione mais cores se necessário

# Plotar cada país
for x, (country, values) in enumerate(grouped_df):
    # Desenhar a caixa
    box_plot.vbar(x=x+1, top=values.max(), bottom=values.min(), width=box_width,
                  fill_color=colors[x % len(colors)], line_color="black", line_width=line_width)
    
    # Desenhar a linha da mediana
    box_plot.rect(x=x+1, y=values.median(), width=box_width, height=0.01,
                  fill_color="white", line_color="black")
    
    # Desenhar os segmentos superior e inferior da caixa
    box_plot.segment(x0=x+1-gap_width, y0=values.max(), x1=x+1+gap_width,
                     y1=values.max(), line_color="black", line_width=line_width)
    box_plot.segment(x0=x+1-gap_width, y0=values.min(), x1=x+1+gap_width,
                     y1=values.min(), line_color="black", line_width=line_width)

    # Calcular o intervalo interquartil e os limites dos whiskers para centralizar
    iqr = values.quantile(0.75) - values.quantile(0.25)
    lower_whisker = max(values.quantile(0.25) - 1.5 * iqr, df[value_column].min())
    upper_whisker = min(values.quantile(0.75) + 1.5 * iqr, df[value_column].max())

    # Desenhar o whisker inferior
    box_plot.segment(x0=x+1, y0=lower_whisker, x1=x+1, y1=values.min(), line_color="black")
    box_plot.segment(x0=x+1-box_width/2, y0=lower_whisker, x1=x+1+box_width/2, y1=lower_whisker,
                     line_color="black")
    
    # Desenhar o whisker superior
    box_plot.segment(x0=x+1, y0=upper_whisker, x1=x+1, y1=values.max(), line_color="black")
    box_plot.segment(x0=x+1-box_width/2, y0=upper_whisker, x1=x+1+box_width/2, y1=upper_whisker,
                     line_color="black")

# Configurar os eixos, legendas e fontes presentes no gráfico
box_plot.xaxis.ticker = x_values
box_plot.xaxis.major_label_overrides = {x: str(country) for x, country in zip(x_values, grouped_df.groups.keys())}
box_plot.xaxis.major_label_orientation = 45
box_plot.yaxis.axis_label = value_column
box_plot.xaxis.axis_label = "Países"
box_plot.title.text = "Pontos de Qualidade totais por país"
box_plot.title.align = "center"
box_plot.title.text_font_size = "12pt"
box_plot.title.text_font = "Arial"

# Personalizar o estilo dos grids
box_plot.xgrid.grid_line_color = "#884A39"
box_plot.ygrid.grid_line_color = "#884A39"
box_plot.xgrid.grid_line_alpha = 0.3
box_plot.ygrid.grid_line_alpha = 0.3

# Adicionar ferramentas interativas
box_plot.add_tools(PanTool(), BoxZoomTool(), ResetTool())

# Mostrar o gráfico
show(box_plot)
