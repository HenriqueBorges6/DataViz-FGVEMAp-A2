import pandas as pd
import numpy as np
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

# Carregando o dataset
df = pd.read_csv('cleaned_coffee_dataset.csv')

# Contando a frequência de cada cor
frequencia_cores = df['Color'].value_counts()

# Selecionando os 6 Color com mais registros e agrupando o resto em "Outras"
top_cores = frequencia_cores.head(6).index.tolist()
df['Color'] = df['Color'].apply(lambda x: x if x in top_cores else 'Outras')

# Criando uma lista com cada color
tipos_cores = df['Color'].unique()

# Criei uma lista vazia para armazenar os dados de cada Color
dados_cores = []

# Para cada tipo de cor, seleciona os dados correspondentes e calcula cada quartil do boxplot
for cor in tipos_cores:
    dados_cor = df[df['Color'] == cor]['Overall'].values
    q1 = np.percentile(dados_cor, 25)
    q2 = np.percentile(dados_cor, 50)
    q3 = np.percentile(dados_cor, 75)
    whisker_bottom = np.min(dados_cor)
    whisker_top = np.max(dados_cor)
    dados_cores.append({'cor': cor, 'q1': q1, 'q2': q2, 'q3': q3, 'whisker_bottom': whisker_bottom, 'whisker_top': whisker_top})

# Criar um data frame com o dados_cores criados no for anterior
df_dados_cores = pd.DataFrame(dados_cores)

# Criar um ColumnDataSource com os dados do DataFrame
source = ColumnDataSource(df_dados_cores)

# Criar o gráfico de boxplot para cada tipo de Color
p = figure(y_range=tipos_cores, width=400, height=400, title="Boxplot por Tipo de Cor")
p.hbar(y='cor', left='q1', right='q3', height=0.7, fill_color="#F5DEB3", line_color="black", source=source)
p.segment(y0='cor', x0='whisker_bottom', y1='cor', x1='whisker_top', line_width=2, line_color="black", source=source)
p.hbar(y='cor', left='q2', right='q2', height=0.5, fill_color="white", line_color="black", source=source)

# Exibir o gráfico
show(p)