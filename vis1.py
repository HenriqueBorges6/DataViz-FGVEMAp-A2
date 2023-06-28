# importando bibliotecas
import pandas as pd
from bokeh.plotting import figure, show

# lendo o csv
dados = pd.read_csv("cleaned_coffee_dataset.csv")

# Preparando os dados
aroma = dados["Body"]
sabor = dados["Flavor"]

# Criando o plotting com os títulos e eixos
aroma_sabor = figure(title="Cheira bem, é bom",
                     x_axis_label="Aroma",
                     y_axis_label="Sabor")

# Escolhendo o tipo do gráfico
aroma_sabor.circle(aroma, sabor,
                   color= "#6F4E37",
                   legend_label="Café"
)