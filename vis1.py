#Bibliotecas utilizadas
import pandas as pd
from bokeh.plotting import figure, show
from myfunctions import cds_generator 
from bokeh.models import ColumnDataSource

dados = cds_generator("cleaned_coffee_dataset.csv")

aroma = dados.data["Body"]
sabor = dados.data["Flavor"]
nota_geral = dados.data["Overall"]

"""
invertendo a escala da nota geral para, quanto menor a nota, mais transparente
"""
max_nota = max(nota_geral)
nota_geral_invertida = [max_nota - nota for nota in nota_geral]

#Fazendo o gráfico
aroma_sabor = figure(title="Cheira bem, é bom",
                     x_axis_label="Aroma",
                     y_axis_label="Sabor",
                     width = 513,
                     height= 483)

"""
Esse será um scater plot
Escolhi essa cor marrom por conta do tema café
Nele temos a relação entre o aroma do café e seu sabor
Os pontos menos transparentes são os que receberam notas maiores na coluna "Overall"
"""
aroma_sabor.circle(aroma, sabor,
                   fill_color="#6F4E37",
                   line_color="#6F4E37",
                   size = 10,
                   fill_alpha=nota_geral_invertida/max_nota, 
                   legend_label="Café"
)

show(aroma_sabor)