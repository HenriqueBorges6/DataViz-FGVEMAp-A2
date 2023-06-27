import pandas as pd
import numpy as np
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool, Label
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

scatter_plot = figure.circle(x="Flavor", y="Acidity", source=coffee_data, size=8, alpha=0.7, color=colors)

figure.xaxis.axis_label = "Sabor"
figure.yaxis.axis_label = "Acidez"
figure.title.text = "Sabor x Acidez"
figure.title.align = "center"
figure.grid.grid_line_color = "lightgray"
figure.grid.grid_line_alpha = 0.5

tooltips = [("Flavor", "@Flavor"), ("Acidity", "@Acidity"), ("Company", "@Company")]
hover_tool = HoverTool(renderers=[scatter_plot], tooltips=tooltips)
figure.add_tools(hover_tool)

#labels = LabelSet(x='Flavor', y='Acidity', text='Company', polui demais o gráfico por isso vou usar o citation
#              x_offset=5, y_offset=5, source=coffee_data)

citation = Label(x=2, y=513, x_units='screen', y_units='screen', text='Identificação das companhias pelas cores',
                 border_line_color='black', border_line_alpha=1.0,
                 background_fill_color='white', background_fill_alpha=0.3, text_font_size='9pt')

figure.add_layout(citation)

show(figure)




