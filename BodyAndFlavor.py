from bokeh.plotting import figure, show
from myfunctions import cds_generator
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.io import curdoc
from bokeh.models import Div, RangeSlider, Spinner
from bokeh.layouts import layout
import numpy as np

# Aplicando um tema
curdoc().theme = "light_minimal"

#Usando a função pra ler o csv e transformar em CDS
dados = cds_generator("cleaned_coffee_dataset.csv")

#Preparando os dados
aroma = dados.data["Body"]
sabor = dados.data["Flavor"]
nota_geral = dados.data["Overall"]

#Alpha pra usar de forma que as observações com menor overall sejam mais trasparentes
alpha = (nota_geral - 6.0) / (8.5 - 6.0)

#Adicionar jitter para ajudar a visualizar melhor os dados
jitter_range = 0.03  
aroma_jitter = np.random.uniform(-jitter_range, jitter_range, len(aroma))
sabor_jitter = np.random.uniform(-jitter_range, jitter_range, len(sabor))
aroma += aroma_jitter
sabor += sabor_jitter

#Criando o plot
p = figure(
    title="Cheira bem, é bom",
    x_axis_label="Aroma",
    y_axis_label="Sabor",
    width=600,  
    height=400,
    background_fill_color="#F0F0F0",
)

#Será um scatter plot
aroma_sabor = p.circle(
    aroma,
    sabor,
    fill_color="#6F4E37",
    line_color="#6F4E37",
    fill_alpha=alpha,  
    legend_label="Café",
    size=10,
)

#Adicionando um Widget do bokeh
div = Div(
    text="""
        <p>Defina o tamanho do cículo para a visualização:</p>
        """,
    width=200,
    height=30,
)
spinner = Spinner(
    title="Circle size",  
    low=0,  
    high=60,  
    step=3,  
    value=aroma_sabor.glyph.size,  
    width=200,  
)
spinner.js_link("value", aroma_sabor.glyph, "size")

#plotar o gráfico com o widget
layout = layout([[div, spinner], [p]])

show(layout)