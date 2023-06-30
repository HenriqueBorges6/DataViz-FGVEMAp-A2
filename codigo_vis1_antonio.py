from bokeh.plotting import figure, show, curdoc
from bokeh.models import ColumnDataSource, HoverTool, Label, Select
from bokeh.palettes import brewer
import pandas as pd
import numpy as np
from bokeh.transform import factor_cmap
from bokeh.palettes import YlOrBr
from bokeh.layouts import row

df = pd.read_csv('cleaned_coffee_dataset.csv')
# Criar um ColumnDataSource a partir do DataFrame
freq_Country_of_Origin = df['Country of Origin'].value_counts()

top_Country_of_Origin = freq_Country_of_Origin.head(10).index.tolist()
filtered_countries = df[df['Country of Origin'].isin(top_Country_of_Origin)]
uniq_countries = filtered_countries['Country of Origin'].unique()
# Criei uma lista vazia para armazenar os dados de cada Color
countries_data= []
countries = ["All"] + list(df["Country of Origin"].unique())

for c in uniq_countries:
    data = df[df['Country of Origin'] == c]['Altitude'].values
    q1 = np.percentile(data, 25)
    q2 = np.percentile(data, 50)
    q3 = np.percentile(data, 75)
    whisker_bottom = np.min(data)
    whisker_top = np.max(data)
    countries_data.append({'country': c, 'q1': q1, 'q2': q2, 'q3': q3, 'whisker_bottom': whisker_bottom, 'whisker_top': whisker_top})


df_data = pd.DataFrame(countries_data).sort_values(by='q2',ascending=True)
uniq_countries=df_data['country'].unique()
# Criar um ColumnDatacSource com os dados do DataFrame
source = ColumnDataSource(df_data)

# Definir a paleta de cores gradiente de marrom

colors = factor_cmap("country", palette=YlOrBr[9], factors=uniq_countries)




# Boxplot para as altitudes e cada tipo de país
p = figure(y_range=uniq_countries, width=600, height=400, title="Origem do Café e Altitude das plantações")
p.hbar(y='country', left='q1', right='q3', height=0.7, fill_color=colors, line_color="black", source=source)
p.segment(y0='country', x0='whisker_bottom', y1='country', x1='whisker_top', line_width=2, line_color="black", source=source)
p.hbar(y='country', left='q2', right='q2', height=0.5, fill_color=colors, line_color="black", source=source)
p.xaxis.axis_label = "Altitude (em metros acima do nível do mar)" 
p.yaxis.axis_label = "País" 
p.title.text = "Altitude: Comparação entre diferentes países produtores"
p.title.align = "center"

# Display the layout
show(p)
