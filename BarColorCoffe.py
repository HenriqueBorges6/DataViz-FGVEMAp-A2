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

# Criando o gráfico de barras
p = figure(x_range=cor_cafe_contagem.index.tolist(), height=350, title="Contagem de Cores de Café")
p.vbar(x=cor_cafe_contagem.index.tolist(), top=cor_cafe_contagem.values, width=0.9,
       fill_color=factor_cmap(cor_cafe_coluna, palette=Category10_10, factors=cor_cafe_contagem.index.tolist()))

# Configurando o eixo x
p.xgrid.grid_line_color = None
p.xaxis.major_label_orientation = 1.2

# Exibindo o gráfico
show(p)