import pandas as pd
from bokeh.io import curdoc, show
from bokeh.plotting import figure
from bokeh.models import PanTool, BoxZoomTool, ResetTool

df = pd.read_csv("cleaned_coffee_dataset.csv")

country_column = "Country of Origin"
value_column = "Total Cup Points"

if country_column not in df.columns:
    raise KeyError(f"The column '{country_column}' does not exist in the DataFrame.")

grouped_df = df.groupby(country_column)[value_column]

p = figure(width=900, height=700, y_range=(df[value_column].min(), df[value_column].max()))

countries = grouped_df.groups.keys()
x_values = list(range(1, len(countries) + 1))
box_width = 0.7
gap_width = 0.2
line_width = 1

for x, country in zip(x_values, countries):
    values = grouped_df.get_group(country)
    p.vbar(x=x, top=values.max(), bottom=values.min(), width=box_width, fill_color="#A7727D", line_color="black", line_width=line_width)
    p.rect(x=x, y=values.median(), width=box_width, height=0.01, fill_color="white", line_color="black")
    p.segment(x0=x - gap_width, y0=values.max(), x1=x + gap_width, y1=values.max(), line_color="black", line_width=line_width)
    p.segment(x0=x - gap_width, y0=values.min(), x1=x + gap_width, y1=values.min(), line_color="black", line_width=line_width)

    iqr = values.quantile(0.75) - values.quantile(0.25)
    lower_whisker = values.quantile(0.25) - 1.5 * iqr
    upper_whisker = values.quantile(0.75) + 1.5 * iqr

    lower_whisker = max(lower_whisker, df[value_column].min())
    upper_whisker = min(upper_whisker, df[value_column].max())

    p.segment(x0=x, y0=lower_whisker, x1=x, y1=values.min(), line_color="black")
    p.segment(x0=x - box_width / 2, y0=lower_whisker, x1=x + box_width / 2, y1=lower_whisker, line_color="black")
    p.segment(x0=x, y0=upper_whisker, x1=x, y1=values.max(), line_color="black")
    p.segment(x0=x - box_width / 2, y0=upper_whisker, x1=x + box_width / 2, y1=upper_whisker, line_color="black")

p.xaxis.ticker = x_values
p.xaxis.major_label_overrides = {x: str(country) for x, country in zip(x_values, countries)}
p.xaxis.major_label_orientation = 45
p.yaxis.axis_label = value_column
p.xaxis.axis_label = "Países"
p.title.text = "Pontos de Qualidade totais por país"
p.title.align = "center"
p.title.text_font_size = "12pt"  
p.title.text_font = "Arial" 

p.xgrid.grid_line_color = "#884A39"
p.ygrid.grid_line_color = "#884A39"
p.xgrid.grid_line_alpha = 0.3
p.ygrid.grid_line_alpha = 0.3
p.add_tools(PanTool(), BoxZoomTool(), ResetTool())
show(p)
