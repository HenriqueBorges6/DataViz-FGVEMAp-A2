#Blibliotecas utilizadas
from bokeh.plotting import figure, show
from myfunctions import cds_generator
from bokeh.palettes import Category10_10
from bokeh.transform import factor_cmap
from bokeh.io import curdoc
import pandas as pd
from bokeh.models import TabPanel, Tabs
from bokeh.plotting import figure, show

#Tema utilizado
curdoc().theme = "light_minimal"

dados = cds_generator("cleaned_coffee_dataset.csv")

# Coluna do seu arquivo CSV
cor_cafe_coluna = 'Color'

# Obtendo a contagem de ocorrências de cada cor de café
cor_cafe_series = pd.Series(dados.data[cor_cafe_coluna])
cor_cafe_contagem = cor_cafe_series.value_counts()

# Obtendo as 7 cores mais frequentes e agrupando as demais
top_7_cores = cor_cafe_contagem[:6]
outras_cores = cor_cafe_contagem[6:]
total_outras_cores = outras_cores.sum()
top_7_cores['Outras Cores'] = total_outras_cores

# Definindo as cores personalizadas
cores_personalizadas = ['#008000', '#0EBE45', '#1BC4B4', '#1771B4', '#ADFF2F', '#964B00', '#78ABAB']

# Revertendo a ordem das barras e das cores
top_7_cores = top_7_cores.iloc[::-1]
cores_personalizadas = cores_personalizadas[::-1]

# Criando o gráfico de barras horizontais com as cores personalizadas
p = figure(y_range=top_7_cores.index.tolist(), width=513 ,height=483,
           title="Contagem de Cores de Café",
           background_fill_color="#F0F0F0")

p.hbar(y=top_7_cores.index.tolist(), right=top_7_cores.values, height=0.8,
       fill_color=cores_personalizadas[:len(top_7_cores)], line_color=None)

# Configurando o eixo y
p.ygrid.grid_line_color = None

#Criando itém 1 para iteratividade
tab1 = TabPanel(child=p, title="Horizontal")


"""
Crinado iten 2 para iteratividade dográfico
"""


#base de dados
dados = cds_generator("df_arabica_clean.csv")

#Preparando o dados
cor_cafe_coluna = 'Color'

# Obtendo a contagem de ocorrências de cada cor de café
cor_cafe_series = pd.Series(dados.data[cor_cafe_coluna])
cor_cafe_contagem = cor_cafe_series.value_counts()

# Obtendo as 7 cores mais frequentes e agrupando as demais
top_7_cores = cor_cafe_contagem[:6]
outras_cores = cor_cafe_contagem[6:]
total_outras_cores = outras_cores.sum()
top_7_cores['Outras Cores'] = total_outras_cores

#Criando cores para cada barra
cores_personalizadas = ['#008000', '#0EBE45', '#1BC4B4', '#1771B4', '#ADFF2F', '#964B00', '#78ABAB']

# Criando o gráfico de barras
qtd_cores = figure(x_range=top_7_cores.index.tolist(), width=513 ,height=483, title="Contagem de Cores de Café",
                   background_fill_color="#F0F0F0")
qtd_cores.vbar(x=top_7_cores.index.tolist(), top=top_7_cores.values, width=0.9,
       fill_color=cores_personalizadas)

# Configurando o eixo x
qtd_cores.xgrid.grid_line_color = None
qtd_cores.xaxis.major_label_orientation = 0.5

#iten de iteratividade 2 criado
tab2 = TabPanel(child=qtd_cores, title="Vertical")

# Exibindo o gráfico
show(Tabs(tabs=[tab1, tab2]))
