import pandas as pd
import numpy as np
from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource, HoverTool, PanTool, ResetTool, WheelZoomTool, TapTool, BoxSelectTool, BoxZoomTool
from bokeh.layouts import column
from bokeh.models.widgets import RangeSlider, Button

# Carregar os dados
df = pd.read_csv("cleaned_coffee_dataset.csv")

# Contar as ocorrências de cada país
country = df['Country of Origin'].value_counts()

# Obter a lista de países e suas respectivas frequências
countries = country.index.tolist()
cont = country.tolist()

# Definir as cores para os países respectivos
colors = [
    "#3fc1bf", "#da3e5b", "#51c15a", "#975ace", "#86b93b", "#af3ea7", "#bdb02e", "#5c6bcc",
    "#db9134", "#5e95cf", "#cd4f31", "#66c08a", "#c03987", "#4a8a36", "#e374d4", "#697329",
    "#bd8ed7", "#aeac5d", "#e75f93", "#37835d", "#8d558c", "#96652c"
]

# Criar a fonte de dados para o gráfico
source = ColumnDataSource(data=dict(countries=countries, counts=cont, colors=colors))

# Criar a ferramenta de hover (sobreposição)
hover = HoverTool(
    tooltips=[
        ("País", "@countries"),
        ("Contagem", "@counts"),
    ]
)

# Criar o gráfico de barras
bar_plot = figure(
    x_range=countries,
    height=600,
    width=850,
    tools=[hover, PanTool(), ResetTool(), WheelZoomTool(), TapTool(), BoxSelectTool(), BoxZoomTool()]
)

bar_plot.vbar(
    x='countries',
    top='counts',
    width=0.8,
    source=source,
    color='colors',
    line_color='black',
    line_width=1.3
)

# Configurar a aparência do gráfico
bar_plot.xaxis.major_label_orientation = 'vertical'
bar_plot.xgrid.grid_line_color = "#884A39"
bar_plot.ygrid.grid_line_color = "#884A39"
bar_plot.grid.grid_line_alpha = 0.5
bar_plot.xaxis.axis_line_width = 0.6
bar_plot.yaxis.axis_line_width = 0.6
bar_plot.xaxis.axis_label = "Países"
bar_plot.yaxis.axis_label = "Contagem"
bar_plot.title.text = "Contagem dos países"
bar_plot.title.align = "center"
bar_plot.title.text_font_size = "12pt"

# Criar o controle deslizante de intervalo
range_slider = RangeSlider(start=0, end=max(cont), value=(0, max(cont)), step=1, title="Intervalo")

# Criar o botão de redefinir
reset_button = Button(label="Redefinir")

# Função de retorno de chamada para o botão de redefinir
def reset():
    range_slider.value = (0, max(cont))

# Função de retorno de chamada para filtrar com base no deslizante(para filtrar os dados) por intervalo
def filter_data(attr, old, new):
    lower, upper = range_slider.value
    filtered_data = df[df['Country of Origin'].isin(countries)]
    filtered_data = filtered_data.groupby('Country of Origin').filter(lambda x: lower <= len(x) <= upper)
    filtered_counts = filtered_data['Country of Origin'].value_counts()
    filtered_countries = filtered_counts.index.tolist()

    # Atualizar os dados da fonte com os valores filtrados
    source.data = dict(countries=filtered_countries, counts=filtered_counts.tolist())
    source.data['colors'] = [colors[countries.index(country)] for country in filtered_countries]
    bar_plot.x_range.factors = filtered_countries  # Atualizar o intervalo do eixo x

range_slider.on_change('value', filter_data)
reset_button.on_click(reset)

layout = column(range_slider, reset_button, bar_plot)

# Adicionar o layout ao documento atual
curdoc().add_root(layout)

