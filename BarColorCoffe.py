#Blibliotecas utilizadas
from bokeh.plotting import figure, show
from myfunctions import cds_generator
from bokeh.palettes import Category10_10
from bokeh.transform import factor_cmap
from bokeh.io import curdoc
import pandas as pd

#Tema utilizado
curdoc().theme = "light_minimal"

#base de dados
dados = cds_generator("cleaned_coffee_dataset.csv")

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
qtd_cores = figure(x_range=top_7_cores.index.tolist(), height=350, title="Contagem de Cores de Café")
qtd_cores.vbar(x=top_7_cores.index.tolist(), top=top_7_cores.values, width=0.9,
       fill_color=cores_personalizadas)

# Configurando o eixo x
qtd_cores.xgrid.grid_line_color = None
qtd_cores.xaxis.major_label_orientation = 1.2

# Exibindo o gráfico
show(qtd_cores)