#Importei a função 'ColumnDataSource' do 'bokeh.models'
from bokeh.models import ColumnDataSource

#Chamei a biblioteca pandas de 'pd'
import pandas as pd

#Botei em uma variável o csv usado no trabalho
df_cafe = pd.read_csv('cleaned_coffee_dataset.csv')

"""Verifiquei quantos lotes foram produzidos por país, e criei o
CDS com o nome do país e seu respectivo numero de lotes produzidos"""
def ocorrencia_por_pais(df_cafe):
    producao_total = df_cafe['Country of Origin'].value_counts()
    numero_de_lotes = producao_total.values
    nome_do_pais_correspondente = producao_total.index
    novo_cds = ColumnDataSource(data=dict(valores=numero_de_lotes, indices=nome_do_pais_correspondente))
    return novo_cds


"""VIS 1"""

"""Criei uma função para criar um cds com os paises como index e a sua produção total em kg"""
def peso_total_por_pais(df_cafe):
    df_cafe['Peso da Mochila'] = df_cafe['Bag Weight'].str.replace(' kg', '').astype(int)
    df_cafe['Peso Total Por Produtora'] = df_cafe['Number of Bags'] * df_cafe['Peso da Mochila']
    producao_por_pais_em_kg = df_cafe.groupby('Country of Origin')['Peso Total Por Produtora'].sum().reset_index()
    producao_por_pais_em_kg = producao_por_pais_em_kg.set_index('Country of Origin')
    novo_cds = ColumnDataSource(data=dict(producao=producao_por_pais_em_kg['Peso Total Por Produtora'].tolist(), paises=producao_por_pais_em_kg.index.tolist()))
    return novo_cds

"""Função para criar objetos em cds com a media da qualidade do cafe por pais"""
def media_por_pais(df_cafe):
    media_da_qualidade_do_cafe = df_cafe.groupby('Country of Origin')['Overall'].mean()
    novo_df = pd.DataFrame({'País': media_da_qualidade_do_cafe.index, 'Média das Notas': media_da_qualidade_do_cafe.values})
    novo_cds = ColumnDataSource(data=dict(paises=novo_df['País'], medias=novo_df['Média das Notas']))
    return novo_cds

"""Criei um cds com a produção total por país, e a média da qualidade por país, para fazer o gráfico"""
Producao = peso_total_por_pais(df_cafe).data['producao']
Paises = media_por_pais(df_cafe).data['paises']
Media = media_por_pais(df_cafe).data['medias']
correlacao_quantidade_qualidade = ColumnDataSource(data=dict(media=Media,producao=Producao, paises=Paises))


"""VIS 2"""

'''Criei duas colunas novas no df_cafe, uma seria 'Data de Avaliação', que é a coluna 'Grading Date' em datetime,
e a outra é a coluna 'MesAno' que é a coluna 'Data de Avaliação' porém no formato em que só contém o mês e o ano'''
def nova_coluna_de_data_de_avaliacao(df_cafe):
    df_cafe['Data de Avaliação'] = pd.to_datetime(df_cafe['Grading Date'], format='mixed', dayfirst=True)
    df_cafe['MesAno'] = df_cafe['Data de Avaliação'].dt.to_period('M')
    return df_cafe

'''Criei um DataFrame que contém as colunas 'MesAno' e 'Overall' '''
def analise_coffe_limpo(df_cafe):
    df = nova_coluna_de_data_de_avaliacao(df_cafe)
    novo_df = df.loc[:, ['MesAno', 'Overall']]
    return novo_df

novo_df = analise_coffe_limpo(df_cafe)

#Criei o df que será utilizado no segundo gráfico, contendo a média por mes de avaliação do mundo inteiro, e passei para cds
df_para_vis2 = novo_df.groupby(novo_df['MesAno'])['Overall'].mean().reset_index()
cds_df_para_vis2 = ColumnDataSource(data=df_para_vis2)

#Verifiquei a média geral da coluna 'Overall' para poder traçar uma span annotation no gráfico
def media_coluna_overall(df_cafe):
    media = df_cafe['Overall'].mean()
    return media

# Criando um DataFrame apenas para poder colocar legenda no gráfico, a respeito da média que é uma span annotation
valores = cds_df_para_vis2.data['MesAno']  
numero = 7,63  
df = pd.DataFrame({'Valores': valores, 'Numero': [numero] * len(valores)})

# Convertendo o DataFrame para um ColumnDataSource
cds_media = ColumnDataSource(df)

'''VIS 3'''

# Dicionário de associação entre países e continentes
continent_dict = {'Asia': ['Taiwan', 'Laos', 'Thailand', 'Indonesia', 'Vietnam', 'Myanmar'],
    'North America': ['Costa Rica', 'Guatemala', 'United States (Hawaii)', 'Mexico'],
    'South America': ['Colombia', 'Brazil', 'Peru', 'Panama'],
    'Africa': ['Tanzania, United Republic Of', 'Ethiopia', 'Kenya', 'Uganda', 'Madagascar'],
    'Central America': ['Nicaragua', 'Honduras', 'El Salvador']}

# Função para obter o continente de um país
def get_continent(country):
    for continent, countries in continent_dict.items():
        if country in countries:
            return continent
    return None

# Criei essa função para fazer um DataFrame com o continente a data em que foi avaliado e a nota nessa avaliação
def dados_para_vis_3(df_cafe):
    df_cafe['Continente'] = df_cafe['Country of Origin'].apply(get_continent)
    media_de_notas_por_continente = df_cafe.groupby(['Continente', 'MesAno'])['Overall'].mean().reset_index()
    return media_de_notas_por_continente

media_de_notas_por_continente = dados_para_vis_3(df_cafe)

#Criei a coluna 'Continente' fora da função anterior para facilitar a manipulação
df_cafe['Continente'] = df_cafe['Country of Origin'].apply(get_continent)

#Criei a variável 'continentes' com cada continente presente no dataset
continentes = df_cafe['Continente'].unique()

# Criar um CDS para cada continente
cds_por_continente = {}
for continente in continentes:
    dados_filtrados = media_de_notas_por_continente[media_de_notas_por_continente['Continente'] == continente]
    cds_filtrado = ColumnDataSource(dados_filtrados)
    cds_por_continente[continente] = cds_filtrado
    
#Joguei os cds criados em variáveis para facilitar a plotagem do gráfico
cds_north_america = cds_por_continente['North America']
cds_south_america =cds_por_continente['South America']
cds_asia = cds_por_continente['Asia']
cds_africa = cds_por_continente['Africa']
cds_central_america = cds_por_continente['Central America']
