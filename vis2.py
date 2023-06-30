import pandas as pd
import numpy as np
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool, PanTool, ResetTool, WheelZoomTool, TapTool
from bokeh.layouts import column

df = pd.read_csv("cleaned_coffee_dataset.csv")
country = df['Country of Origin'].value_counts()

countries = country.index.tolist()
cont = country.tolist()

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

country_colors = [colors[i % len(colors)] for i in range(len(countries))]

source = ColumnDataSource(data=dict(countries=countries, counts=cont, colors=country_colors))

hover = HoverTool(
    tooltips=[
        ("País", "@countries"),
        ("Contagem", "@counts"),
    ]
)

bar_plot = figure(x_range=countries, height=600, width=850, tools=[hover, PanTool(), ResetTool(), WheelZoomTool(), TapTool()])
bar_plot.vbar(x='countries', top='counts', width=0.8, source=source, color='colors', line_color='black', line_width=1.3)  # Increase line_width value and set line_color to black

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

layout = column(bar_plot)

show(layout)
