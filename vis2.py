# Para rodar o código: bokeh serve --show vis2.py    
import pandas as pd
import numpy as np
from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource

df = pd.read_csv("cleaned_coffee_dataset.csv")
country_counts = df['Country of Origin'].value_counts()

countries = country_counts.index.tolist()
cont = country_counts.tolist()

bar_plot = figure(x_range=countries, height=600, width=850)

bar_plot.vbar(x=countries, top=cont, width=0.8)

bar_plot.xaxis.major_label_orientation = 'vertical'

bar_plot.grid.grid_line_color = "lightgray"
bar_plot.grid.grid_line_alpha = 0.5
bar_plot.xaxis.axis_line_width = 1.2
bar_plot.yaxis.axis_line_width = 1.2

bar_plot.xaxis.axis_label = "Países"
bar_plot.yaxis.axis_label = "Contagem"
bar_plot.title.text = "Contagem dos países"
curdoc().add_root(bar_plot)
