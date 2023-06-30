# Criando função que transforma data_set em ColunmDataSource
def cds_generator(data):
    import pandas as pd
    from bokeh.models import ColumnDataSource
    data_set = pd.read_csv(data)
    source = ColumnDataSource(data_set)
    return source

"""
conferindo "função cds_generator":
data = cds_generator("df_arabica_clean.csv")
print(data.data['Overall'])
"""
# Função para gerar boxplot
def generate_boxplot(column_name):
    import pandas as pd
    import numpy as np
    from bokeh.plotting import figure, show
    from bokeh.models import ColumnDataSource
    # Carregar o dataset
    df = pd.read_csv('df_arabica_clean.csv')

    # Contar a frequência de cada cor
    frequencia_cores = df['Color'].value_counts()

    # Selecionar as 6 cores com mais registros e agrupar as demais em "Outras"
    top_cores = frequencia_cores.head(6).index.tolist()
    df['Color'] = df['Color'].apply(lambda x: x if x in top_cores else 'Outras')

    # Criar uma lista com cada Color
    tipos_cores = df['Color'].unique()

    # Criar uma lista vazia para armazenar os dados de cada Color
    dados_cores = []

    # Para cada tipo de cor, selecionar os dados correspondentes e calcular cada quartil do boxplot
    for cor in tipos_cores:
        dados_cor = df[df['Color'] == cor][column_name].values
        q1 = np.percentile(dados_cor, 25)
        q2 = np.percentile(dados_cor, 50)
        q3 = np.percentile(dados_cor, 75)
        whisker_bottom = np.min(dados_cor)
        whisker_top = np.max(dados_cor)
        dados_cores.append({'cor': cor, 'q1': q1, 'q2': q2, 'q3': q3, 'whisker_bottom': whisker_bottom, 'whisker_top': whisker_top})

    # Criar um DataFrame com os dados_cores criados no for anterior
    df_dados_cores = pd.DataFrame(dados_cores)

    # Criar um ColumnDataSource com os dados do DataFrame
    source = ColumnDataSource(df_dados_cores)

    # Criar o gráfico de boxplot para cada tipo de cor
    p = figure(y_range=tipos_cores, width=400, height=400, title=f"Boxplot por Tipo de Cor - {column_name}")
    p.hbar(y='cor', left='q1', right='q3', height=0.7, fill_color="#F5DEB3", line_color="black", source=source)
    p.segment(y0='cor', x0='whisker_bottom', y1='cor', x1='whisker_top', line_width=2, line_color="black", source=source)
    p.hbar(y='cor', left='q2', right='q2', height=0.5, fill_color="white", line_color="black", source=source)
    #retornar p para usar como tabpanel
    return p