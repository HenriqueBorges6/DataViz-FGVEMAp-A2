import pandas as pd
import numpy as np
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.io import output_file
from bokeh.transform import factor_cmap
from bokeh.palettes import Category10

df = pd.read_csv("cleaned_coffee_dataset.csv")

df["Flavor"] = df["Flavor"] + np.random.normal(0, 0.1, size=len(df))
df["Acidity"] = df["Acidity"] + np.random.normal(0, 0.1, size=len(df))

coffee_data = ColumnDataSource(data=df)

output_file("vis_1.html")

companies = df["Company"].unique()
colors = factor_cmap("Company", palette=Category10[10], factors=companies)

figure = figure(width=800, height=600)

scatter_plot = figure.circle(x="Flavor", y="Acidity", source=coffee_data, size=8, alpha=0.9,color=colors)

figure.xaxis.axis_label = "Sabor"
figure.yaxis.axis_label = "Acidez"
figure.title.text = "Sabor x Acidez"
figure.title.align = "center"
figure.grid.grid_line_color = "lightgray"
figure.grid.grid_line_alpha = 0.5

tooltips = [("Flavor", "@Flavor"), ("Acidity", "@Acidity"), ("Company", "@Company")]
hover_tool = HoverTool(renderers=[scatter_plot], tooltips=tooltips)
figure.add_tools(hover_tool)

show(figure)


