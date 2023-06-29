import pandas as pd
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import PanTool, BoxZoomTool, ResetTool

df = pd.read_csv("cleaned_coffee_dataset.csv")  

country_column = "Country of Origin"  
value_column = "Total Cup Points"  

if country_column not in df.columns:
    raise KeyError(f"The column '{country_column}' does not exist in the DataFrame.")

grouped_df = df.groupby(country_column)[value_column]

p = figure(width=1000, height=800, y_range=(df[value_column].min(), df[value_column].max()))

countries = grouped_df.groups.keys()
x_values = list(range(1, len(countries) + 1))
box_width = 0.7
gap_width = 0.2

for x, country in zip(x_values, countries):
    values = grouped_df.get_group(country)
    p.vbar(x=x, top=values.max(), bottom=values.min(), width=box_width, fill_color="#3B84C4", line_color="black")
    p.rect(x=x, y=values.median(), width=box_width, height=0.01, fill_color="white", line_color="black")
    p.segment(x0=x - gap_width, y0=values.max(), x1=x + gap_width, y1=values.max(), line_color="black")
    p.segment(x0=x - gap_width, y0=values.min(), x1=x + gap_width, y1=values.min(), line_color="black")

p.xaxis.ticker = x_values
p.xaxis.major_label_overrides = {x: str(country) for x, country in zip(x_values, countries)}
p.xaxis.major_label_orientation = 45
p.yaxis.axis_label = value_column
p.xaxis.axis_label = "Países" 
p.title.text = "Pontos de Qualidade totais por país"
p.title.align = "center"

p.add_tools(PanTool(), BoxZoomTool(), ResetTool())

curdoc().add_root(p)
