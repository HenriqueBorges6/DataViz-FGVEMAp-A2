from bokeh.models import Range1d, ColumnDataSource
from bokeh.plotting import figure, show
from bokeh.io import output_file,save,show
from bokeh.layouts import gridplot
from sklearn import datasets
import pandas as pd
import numpy as np


df = pd.read_csv("cleaned_coffee_dataset.csv")
coffee_data = ColumnDataSource(data=df)
                
output_file("vis_1.html")

figure = figure()
scatter_plot = figure.circle(x="Flavor", y="Acidity", source=coffee_data, size=8, color="#C38154", alpha=0.9)

figure.xaxis.axis_label = "Sabor"
figure.xaxis.axis_label = "Acidez"
figure.title.text = "Sabor x Acidez"
figure.grid.grid_line_color = "lightgray"
figure.grid.grid_line_alpha = 0.5
scatter_plot.hover_glyph = None  # Disable the default hover glyph
tooltips = [("Flavor", "@Flavor"), ("Acidity", "@Acidity")]
scatter_plot.add_tools(figure.tooltips(tooltips))


show(figure)

