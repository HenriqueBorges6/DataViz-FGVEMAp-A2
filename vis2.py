import pandas as pd
import numpy as np
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool, PanTool, ResetTool, WheelZoomTool, TapTool, BoxSelectTool, BoxZoomTool
from bokeh.layouts import column

# Carregar o dataset
df = pd.read_csv("cleaned_coffee_dataset.csv")

# Contar a quantidade de ocorrências de cada país
country = df['Country of Origin'].value_counts()

# Obter a lista de países e suas respectivas frequências
countries = country.index.tolist()
cont = country.tolist()

# Definir as cores dos respectivos países
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
country_colors = [colors[i % len(colors)] for i in range(len(countries))]

# Criar a fonte de dados para o gráfico
source = ColumnDataSource(data=dict(countries=countries, counts=cont, colors=country_colors))

# Criar a ferramenta de hover
hover = HoverTool(
    tooltips=[
        ("País", "@countries"),
        ("Contagem", "@counts"),
    ]
)

# Definir as ferramentas interativas

# Criar o gráfico de barras
bar_plot = figure(x_range=countries, height=600, width=850, tools=[hover, PanTool(), ResetTool(), WheelZoomTool(), TapTool(),  BoxSelectTool(),BoxZoomTool()])
bar_plot.vbar(x='countries', top='counts', width=0.8, source=source, color='colors', line_color='black', line_width=1.3)  # Aumentar o valor de line_width e definir line_color como preto

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

# Definir as propriedades dos glifos de seleção e não seleção para a interatividade
bar_plot.vbar(x='countries', top='counts', width=0.8, source=source, color='colors', line_color='black',
            line_width=1.3, alpha=0.7, selection_color='colors', nonselection_color='colors', selection_alpha=1,
            nonselection_alpha=0.2)


layout = column(bar_plot)

# Mostrar o gráfico
show(layout)
