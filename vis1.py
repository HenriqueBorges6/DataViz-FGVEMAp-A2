# Para rodar o código: bokeh serve --show vis1.py    
import pandas as pd
import numpy as np
from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource, HoverTool, Label, Select
from bokeh.transform import factor_cmap
from bokeh.palettes import Category10

# Lê os dados do arquivo .csv e retorna um dataframe
df = pd.read_csv("cleaned_coffee_dataset.csv")

# Criando pequenas variações nos valores para melhorar a visualização gráfica.
df["Flavor"]  = df["Flavor"] + np.random.normal(0, 0.1, size=len(df))
df["Acidity"] = df["Acidity"] + np.random.normal(0, 0.1, size=len(df))

# Criei ColumnDataSource
coffee_data = ColumnDataSource(data=df)

# Atribui cores diferentes para as empresas distintas
companies = df["Company"].unique()
colors = factor_cmap("Company", palette=Category10[10], factors=companies)


figure = figure(width=850, height=600)
                   
# Criação de um gráfico de dispersão
scatter_plot = figure.circle(x="Flavor", y="Acidity", source=coffee_data, size=8, alpha=0.7, color=colors)

# Mudança das legendas das variáveis
figure.xaxis.axis_label = "Sabor"
figure.yaxis.axis_label = "Acidez"
figure.title.text = "Sabor x Acidez"
figure.title.align = "center"

# Customizando as linhas e grids dos gráficos
figure.grid.grid_line_color = "lightgray"
figure.grid.grid_line_alpha = 0.5
figure.xaxis.axis_line_width = 1.2
figure.yaxis.axis_line_width = 1.2

# Adicionei 'hoover tooltips' para o gráfico de dispersão'
tooltips = [("Grau do Sabor", "@Flavor"), ("Grau de ascidez", "@Acidity"), ("Companhia", "@Company")]
hover= HoverTool(renderers=[scatter_plot], tooltips=tooltips)
figure.add_tools(hover)
                                                                                                
# criei uma lista de todos os países presentes no dataset
countries = ["All"] + list(df["Country of Origin"].unique())
# utilizei a classe Select para mudar a representação gráfica pela escolha do país por um dropdown
select = Select(title="Filtre por país:", options=countries, value="All")

# faz a mudança do dataset para o país escolhido
def select_country(attribute, old, new):
    if select.value == "All":
        new_data = df
    else:
        new_data = df[df["Country of Origin"] == select.value]
    coffee_data.data = ColumnDataSource.from_df(new_data)

select.on_change("value", select_country)

# adiciona uma citação no gráfico que fica presente na tela a todo momento
citation = Label(x=2, y=510, x_units='screen', y_units='screen', text='Identificação das companhias pelas cores',
                 border_line_color='black', border_line_alpha=1.0,
                 background_fill_color='white', background_fill_alpha=0.3, text_font_size='9pt')
figure.add_layout(citation)

# Exibe o gráfico no navegador
curdoc().add_root(select)
curdoc().add_root(figure)