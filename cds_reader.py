import pandas as pd
import numpy as np

# Criando função que transforma data_set em ColunmDataSource
from bokeh.models import ColumnDataSource, HoverTool, Label, Select
def df_to_cds_conv(df):
    source = ColumnDataSource(df)
    return source

"""
conferindo "função cds_generator":
data = cds_generator("df_arabica_clean.csv")
print(data.data['Overall'])
"""

# Leitura dos dados
df = pd.read_csv('cleaned_coffee_dataset.csv')
coffee_data = df_to_cds_conv(df)
quakers = coffee_data.data["Quakers"]
quakers = np.float16(quakers)
aroma = coffee_data.data["Aroma"]
nota_geral = coffee_data.data["Overall"]
alpha = (nota_geral - 6.0) / (8.5 - 6.0)

data_para_vis_2 = {
    'Quakers': quakers,
    'Aroma': aroma,
    'Overall': nota_geral
    }
# Criar o ColumnDataSource para o plot_2
def source_para_vis_2(data_para_vis_2):
    source_para_vis_2 = ColumnDataSource(data_para_vis_2)
    nota_geral = source_para_vis_2.data["Overall"]
    alpha = (nota_geral - 6.0) / (8.5 - 6.0)
    source_para_vis_2.data["Alpha"] = alpha
    return source_para_vis_2
