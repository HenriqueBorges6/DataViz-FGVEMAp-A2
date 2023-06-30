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
    # Carregar o dataset
    df = pd.read_csv('df_arabica_clean.csv')

    # Contar a frequência de cada cor
    frequencia_cores = df['Color'].value_counts()

    # Selecionar as 6 cores com mais registros e agrupar as demais em "Outras"
    top_cores = frequencia_cores.head(6).index.tolist()
    df['Color'] = df['Color'].apply(lambda x: x if x in top_cores else 'Outras')

    # Criar uma lista com cada cor
    tipos_cores = df['Color'].unique()

    # Criar uma lista vazia para armazenar os dados de cada cor
    dados_cores = []

    # Para cada tipo de cor, selecionar os dados correspondentes e calcular cada quartil do boxplot
    for cor, cor_palette in zip(tipos_cores, Category10_7):
        dados_cor = df[df['Color'] == cor][column_name].values
        q1 = np.percentile(dados_cor, 25)
        q2 = np.percentile(dados_cor, 50)
        q3 = np.percentile(dados_cor, 75)
        whisker_bottom = np.min(dados_cor)
        whisker_top = np.max(dados_cor)
        dados_cores.append({'cor': cor, 'q1': q1, 'q2': q2, 'q3': q3, 'whisker_bottom': whisker_bottom, 'whisker_top': whisker_top, 'cor_palette': cor_palette})

    # Criar um DataFrame com os dados_cores criados no for anterior
    df_dados_cores = pd.DataFrame(dados_cores)

    # Criar um ColumnDataSource com os dados do DataFrame
    source = ColumnDataSource(df_dados_cores)

    # Criar o gráfico de boxplot para cada tipo de cor
    p = figure(y_range=tipos_cores, width=400, height=400, title=f"Boxplot por Tipo de Cor - {column_name}")
    p.hbar(y='cor', left='q1', right='q3', height=0.7, fill_color='cor_palette', line_color="black", source=source)
    p.segment(y0='cor', x0='whisker_bottom', y1='cor', x1='whisker_top', line_width=2, line_color="black", source=source)
    p.hbar(y='cor', left='q2', right='q2', height=0.5, fill_color="white", line_color="black", source=source)
    
    #usar retunr para atribuir o tabpanel
    return p

def barplot():
    from bokeh.plotting import figure, show
    from bokeh.palettes import Category10_10
    from bokeh.transform import factor_cmap
    from bokeh.io import curdoc
    import pandas as pd
    from bokeh.models import TabPanel, Tabs
    from bokeh.plotting import figure, show

    # Tema utilizado
    curdoc().theme = "light_minimal"

    dados = cds_generator("df_arabica_clean.csv")

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
    p = figure(y_range=top_7_cores.index.tolist(), width=513, height=483, title="Contagem de Cores de Café", background_fill_color="#F0F0F0")

    p.hbar(y=top_7_cores.index.tolist(), right=top_7_cores.values, height=0.8, fill_color=cores_personalizadas[:len(top_7_cores)], line_color=None)

    # Configurando o eixo y
    p.ygrid.grid_line_color = None

    return p

def vertical_bar():
    from bokeh.plotting import figure, show
    from bokeh.palettes import Category10_10
    from bokeh.transform import factor_cmap
    from bokeh.io import curdoc
    import pandas as pd
    from bokeh.models import TabPanel, Tabs
    from bokeh.plotting import figure, show
    # Base de dados
    dados = cds_generator("df_arabica_clean.csv")

    # Preparando os dados
    cor_cafe_coluna = 'Color'

    # Obtendo a contagem de ocorrências de cada cor de café
    cor_cafe_series = pd.Series(dados.data[cor_cafe_coluna])
    cor_cafe_contagem = cor_cafe_series.value_counts()

    # Obtendo as 7 cores mais frequentes e agrupando as demais
    top_7_cores = cor_cafe_contagem[:6]
    outras_cores = cor_cafe_contagem[6:]
    total_outras_cores = outras_cores.sum()
    top_7_cores['Outras Cores'] = total_outras_cores

    # Criando cores para cada barra
    cores_personalizadas = ['#008000', '#0EBE45', '#1BC4B4', '#1771B4', '#ADFF2F', '#964B00', '#78ABAB']

    # Criando o gráfico de barras
    qtd_cores = figure(x_range=top_7_cores.index.tolist(), width=513, height=483, title="Contagem de Cores de Café", background_fill_color="#F0F0F0")
    qtd_cores.vbar(x=top_7_cores.index.tolist(), top=top_7_cores.values, width=0.9, fill_color=cores_personalizadas)

    # Configurando o eixo x
    qtd_cores.xgrid.grid_line_color = None
    qtd_cores.xaxis.major_label_orientation = 0.5

    # Item de iteratividade 2 criado
    return qtd_cores

def scatter():
    from bokeh.plotting import figure, show
    from myfunctions import cds_generator
    from bokeh.models import HoverTool, ColumnDataSource
    from bokeh.io import curdoc
    from bokeh.models import Div, RangeSlider, Spinner
    from bokeh.layouts import layout
    import numpy as np

    # Aplicando um tema
    curdoc().theme = "light_minimal"

    dados = cds_generator("df_arabica_clean.csv")

    aroma = dados.data["Body"]
    sabor = dados.data["Flavor"]
    nota_geral = dados.data["Overall"]

    alpha = (nota_geral - 6.0) / (8.5 - 6.0)

    jitter_range = 0.03  

    # Adicionar jitter às coordenadas dos pontos
    aroma_jitter = np.random.uniform(-jitter_range, jitter_range, len(aroma))
    sabor_jitter = np.random.uniform(-jitter_range, jitter_range, len(sabor))
    aroma += aroma_jitter
    sabor += sabor_jitter

    p = figure(
        title="Cheira bem, é bom",
        x_axis_label="Aroma",
        y_axis_label="Sabor",
        width=513,  
        height=483,
        background_fill_color="#F0F0F0",
    )

    aroma_sabor = p.circle(
        aroma,
        sabor,
        fill_color="#6F4E37",
        line_color="#6F4E37",
        fill_alpha=alpha,  
        legend_label="Café",
        size=10,
    )

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

    layout = layout([[div, spinner], [p]])

    show(layout)
