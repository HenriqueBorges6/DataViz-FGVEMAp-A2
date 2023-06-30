#Import dos dados organizados para o gráfico
from manipulacao_dados_gabriel import cds_df_para_vis2, df_cafe, media_coluna_overall,cds_media

#Import para a visualização em bokeh
from bokeh.plotting import figure
from bokeh.models.annotations import Span
from bokeh.models import HoverTool, CustomJSHover
from bokeh.models.formatters import NumeralTickFormatter

#Defini o formato do eixo x , largura, altura e as tools do gráfico
figure2= figure(x_axis_type = 'datetime', width = 600, height = 400, tools=['pan', 'reset','box_zoom'])

#Plotei as barras no graáfico, já editando algumas características
barras = figure2.vbar(x='MesAno', top='Overall', source = cds_df_para_vis2, color="#73574D", line_width = 20)

#Essa linha invisível foi criada para facilitar o implementamento da hoover tool
figure2.line(x='MesAno', y='Overall', source = cds_df_para_vis2, alpha = 0)

#Configurações básicas do gráfico
figure2.title.text = 'Evolução da Qualidade do Café no Mundo'
figure2.title.text_color = "#73574D"
figure2.title.text_font = "Arial"
figure2.title.text_font_size = "22px"
figure2.title.align = "left"
figure2.background_fill_color = "#D9CCC5"
figure2.yaxis.axis_label = "Qualidade"
figure2.xaxis.axis_label = "Data da Avaliação"
figure2.grid.grid_line_alpha = 0
figure2.yaxis.axis_label_text_color = "#3D2923"
figure2.xaxis.axis_label_text_color = "#3D2923"
figure2.xaxis.minor_tick_line_color = "#3D2923"
figure2.yaxis.minor_tick_line_color = "#3D2923"
figure2.xaxis.major_tick_in = 0
figure2.yaxis.major_tick_in = 0
figure2.xaxis.axis_line_width = 2
figure2.yaxis.axis_line_width = 2
figure2.xaxis.axis_line_color = "#73574D"
figure2.yaxis.axis_line_color = "#73574D"
figure2.xaxis[0].ticker.num_minor_ticks = 0
figure2.yaxis[0].ticker.num_minor_ticks = 0
figure2.xaxis.axis_label_text_font_size = "11pt"
figure2.yaxis.axis_label_text_font_size = "11pt"
figure2.y_range.start = 7
figure2.y_range.end = 8
figure2.yaxis.formatter = NumeralTickFormatter(format="0.0")

#Criei a hoover tool mexendo o formato do eixo x para datetime
hover_tool = HoverTool(
    tooltips=[
        ( 'Data',   '@MesAno{%F}'            ),
        ( 'Qualidade',  '@Overall' )
    ],
    formatters={
        '@MesAno'  : 'datetime'}
       , mode='vline'
)

# Adicione a ferramenta de destaque ao gráfico
figure2.add_tools(hover_tool)

#Adicionei uma linha pontilhada que representa a média geral da qualidade do café
span = Span(location=media_coluna_overall(df_cafe), dimension="width",line_color='#260B01',line_width=2, line_dash = 'dashed')
figure2.add_layout(span)

#Uma forma de colocar uma legenda para span annotation
figure2.line(x='Valores', y='Numero', source=cds_media, color = '#260B01',line_dash = 'dashed', line_width = 2, legend_label = 'Média Geral')

#Tirei a logo
figure2.toolbar.logo = None