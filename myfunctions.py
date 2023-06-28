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