import pandas as pd
import numpy as np
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.io import output_file

df = pd.read_csv("cleaned_coffee_dataset.csv")
df["Flavor"] = df["Flavor"] + np.random.normal(0, 0.1, size=len(df))
df["Acidity"] = df["Acidity"] + np.random.normal(0, 0.1, size=len(df))
coffee_data = ColumnDataSource(data=df)
output_file("vis_1.html")
figure = figure(width=800, height=600)
scatter_plot = figure.circle(x="Flavor", y="Acidity", source=coffee_data, size=8, alpha=0.9)
figure.xaxis.axis_label = "Sabor"
figure.yaxis.axis_label = "Acidez"
figure.title.text = "Sabor x Acidez"
figure.grid.grid_line_color = "lightgray"
figure.grid.grid_line_alpha = 0.5
tooltips = [("Flavor", "@Flavor"), ("Acidity", "@Acidity"), ("Company", "@Company")]
inter_tools = HoverTool(renderers=[scatter_plot], tooltips=tooltips)
figure.add_tools(inter_tools)

show(figure)


