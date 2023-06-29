import pandas as pd
import numpy as np
from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource, HoverTool, RangeSlider, Button, PanTool, BoxZoomTool, ResetTool
from bokeh.layouts import column

df = pd.read_csv("cleaned_coffee_dataset.csv")
country = df['Country of Origin'].value_counts()

countries = country.index.tolist()
cont = country.tolist()

source = ColumnDataSource(data=dict(countries=countries, counts=cont))

hover = HoverTool(
    tooltips=[
        ("País", "@countries"),
        ("Contagem", "@counts")
    ]
)

bar_plot = figure(x_range=countries, height=600, width=850, tools=[hover, PanTool(), BoxZoomTool(), ResetTool()])
bar_plot.vbar(x='countries', top='counts', width=0.8, source=source, color='navy')

bar_plot.xaxis.major_label_orientation = 'vertical'
bar_plot.grid.grid_line_color = "lightgray"
bar_plot.grid.grid_line_alpha = 0.5
bar_plot.xaxis.axis_line_width = 1.2
bar_plot.yaxis.axis_line_width = 1.2
bar_plot.xaxis.axis_label = "Países"
bar_plot.yaxis.axis_label = "Contagem"
bar_plot.title.text = "Contagem dos países"
bar_plot.title.align = "center"

range_slider = RangeSlider(title="Faixa", start=0, end=30, value=(0, 30),step=1)

reset_button = Button(label="Resetar", button_type="default")

def reset():
    range_slider.value = (0, 30)

def filter_data(attr, old, new):
    lower, upper = range_slider.value
    filtered_data = df[df['Country of Origin'].isin(countries)]
    filtered_data = filtered_data.groupby('Country of Origin').filter(lambda x: lower < len(x) < upper)
    filtered_counts = filtered_data['Country of Origin'].value_counts()
    filtered_countries = filtered_counts.index.tolist()
    source.data = dict(countries=filtered_countries, counts=filtered_counts.tolist())
    bar_plot.x_range.factors = filtered_countries  
    
range_slider.on_change('value', filter_data)
reset_button.on_click(reset)

layout = column(bar_plot, range_slider, reset_button)
curdoc().add_root(layout)
