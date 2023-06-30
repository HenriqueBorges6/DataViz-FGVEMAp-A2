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
    #Bibliotecas    
    import pandas as pd
    import numpy as np
    from bokeh.plotting import figure, show
    from bokeh.models import ColumnDataSource
    from bokeh.palettes import Category10_7
    
    # Carregando o dataset
    df = pd.read_csv('df_arabica_clean.csv')

    # Frequência de cada Color
    frequencia_cores = df['Color'].value_counts()

    # Selecionar as 6 cores com mais ocorrencias e agrupar as demais em "Outras"
    top_cores = frequencia_cores.head(6).index.tolist()
    df['Color'] = df['Color'].apply(lambda x: x if x in top_cores else 'Outras')

    # Criei uma lista com cada Color
    tipos_cores = df['Color'].unique()

    # Criei uma lista vazia para armazenar os dados de cada cor
    dados_cores = []

    # Preparando os dados pro bloxpot, calculando os quartis
    for cor, cor_palette in zip(tipos_cores, Category10_7):
        dados_cor = df[df['Color'] == cor][column_name].values
        q1 = np.percentile(dados_cor, 25)
        q2 = np.percentile(dados_cor, 50)
        q3 = np.percentile(dados_cor, 75)
        whisker_bottom = np.min(dados_cor)
        whisker_top = np.max(dados_cor)
        dados_cores.append({'cor': cor, 
                            'q1': q1, 
                            'q2': q2, 
                            'q3': q3, 
                            'whisker_bottom': whisker_bottom, 
                            'whisker_top': whisker_top, 
                            'cor_palette': cor_palette})

    # Criei um DataFrame com os dados_cores criados no for anterior
    df_dados_cores = pd.DataFrame(dados_cores)

    # Criei um ColumnDataSource com os dados do DataFrame
    source = ColumnDataSource(df_dados_cores)

    # Criei o gráfico de boxplot para cada tipo de color
    p = figure(y_range=tipos_cores, 
               width=600, 
               height=400, 
               title=f"Boxplot por Color - {column_name}",
               background_fill_color="#F0F0F0")
    p.hbar(y='cor', 
           left='q1', 
           right='q3', 
           height=0.7, 
           fill_color='cor_palette', 
           line_color="black", 
           source=source)
    p.segment(y0='cor', 
              x0='whisker_bottom', 
              y1='cor', 
              x1='whisker_top', 
              line_width=2, 
              line_color="black", 
              source=source)
    p.hbar(y='cor', 
           left='q2', 
           right='q2', 
           height=0.5, 
           fill_color="white", 
           line_color="black", 
           source=source)
    
    #usar retunr para atribuir o tabpanel
    return p
