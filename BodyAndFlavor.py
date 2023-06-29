#Bibliotecas utilizadas
import numpy as np
from bokeh.plotting import figure, show
from myfunctions import cds_generator
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.io import curdoc

#Aplicando um tema
curdoc().theme = "light_minimal"

#Utilizando a função para transformar o dataset em CDS
dados = cds_generator("cleaned_coffee_dataset.csv")

#Preparando os dados
aroma = dados.data["Body"]
sabor = dados.data["Flavor"]
nota_geral = dados.data["Overall"]

#Fazendo um alpha para que quanto maior o Overall do café, menos trasparente apareça no plot
alpha = (nota_geral - 6.0) / (8.5 - 6.0)

# Adicionar jitter às coordenadas dos pontos
jitter_range = 0.03  
aroma_jitter = np.random.uniform(-jitter_range, jitter_range, len(aroma))
sabor_jitter = np.random.uniform(-jitter_range, jitter_range, len(sabor))
aroma += aroma_jitter
sabor += sabor_jitter
#Usamos o jitter para conseguir ter uma melhor noção da quantidade de amostras

#preparando o gráfico
aroma_sabor = figure(title="Cheira bem, é bom", 
                     x_axis_label="Aroma",
                     y_axis_label="Sabor",
                     width=513, 
                     height=483
                     )
"""
Será um scatter plot, a ideia é verificar a relação entre o aroma e o sabor,
 junto a média nos outros aspectos.
"""
aroma_sabor.circle(aroma, sabor,
                   fill_color="#6F4E37",
                   line_color="#6F4E37",
                   fill_alpha=alpha, 
                   legend_label="Café",
                   size = 10
)
#personalizando um pouco o plot, retirando alguns elementos "desnecessários"
aroma_sabor.toolbar.autohide = True 
aroma_sabor.toolbar.logo = None # Não vejo necessidade em aparecer a logo do bokeh
aroma_sabor.grid.visible = False 
# Não vejo necessidade da grade de fundo. A posição e o alpha são suficientes

# Movi a legenda pra esquerda, assim ela sobrepõem os pontos
aroma_sabor.legend.location = "top_left"

#função pra mostrar o gráfico
show(aroma_sabor)
