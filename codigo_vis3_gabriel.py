from manipulacao_dados_gabriel import cds_north_america, cds_south_america, cds_africa, cds_asia, cds_central_america
from bokeh.plotting import figure
from bokeh.io import show
from bokeh.models import Range1d
import pandas as pd


figure3=figure(x_axis_type = 'datetime', width = 600, height = 400)

#Adicionei 5 linhas no gráfico em que cada uma delas é um continente
figure3.line(x='MesAno', y='Overall', source=cds_north_america, line_width=2, legend_label = 'América do Norte', color = '#3C2919', alpha = 1, muted_alpha = 0.05, muted_color = '#3C2919' )
figure3.line(x='MesAno', y='Overall', source=cds_south_america, line_width=2, legend_label = 'América do Sul', color = '#6A3C1A', alpha = 1, muted_alpha = 0.05, muted_color = '#6A3C1A')
figure3.line(x='MesAno', y='Overall', source=cds_central_america, line_width=2.2, legend_label = 'América Central', color = '#D99771',alpha = 1, muted_alpha = 0.05, muted_color = '#D99771')
figure3.line(x='MesAno', y='Overall', source=cds_asia, line_width=2, legend_label = 'Ásia', color = '#865D37',alpha = 1, muted_alpha = 0.05, muted_color = '#865D37')
figure3.line(x='MesAno', y='Overall', source=cds_africa, line_width=2, legend_label = 'África', color = '#B4855B',alpha = 1, muted_alpha = 0.05, muted_color = '#B4855B')


figure3.toolbar.active_drag = None

#Configurei a legenda para ter uma interatividade ao clicar em um continente da legenda e assim ele ficar menos visível
figure3.legend.click_policy="mute"
figure3.legend.location = "top_right"

#Configurando mais a legenda
legend = figure3.legend[0]
legend.label_text_font_size = '8pt'
legend.label_standoff = 0
legend.spacing = 0
legend.margin = 0

#Configurações básicas do gráfico
figure3.title.text = 'De Onde Vem o Melhor Café?'
figure3.title.text_color = "#73574D"
figure3.title.text_font = "Arial"
figure3.title.text_font_size = "20px"
figure3.title.align = "left"
figure3.grid.grid_line_alpha = 0
figure3.background_fill_color = "#D9CCC5"
figure3.y_range.start = 7
figure3.y_range.end = 8.6
figure3.xaxis.major_tick_in = 0
figure3.yaxis.major_tick_in = 0
figure3.yaxis.axis_label = "Qualidade"
figure3.xaxis.axis_label = "Data da Avaliação"
figure3.yaxis.axis_label_text_color = "#3D2923"
figure3.xaxis.axis_label_text_color = "#3D2923"
figure3.yaxis.axis_label_text_font_size = "11pt"
figure3.xaxis.axis_label_text_font_size = "11pt"
figure3.xaxis.axis_line_width = 2
figure3.yaxis.axis_line_width = 2
figure3.xaxis.axis_line_color = "#73574D"
figure3.yaxis.axis_line_color = "#73574D"
figure3.xaxis[0].ticker.num_minor_ticks = 0
figure3.yaxis[0].ticker.num_minor_ticks = 0
figure3.xaxis.major_tick_line_color = "#73574D"
figure3.yaxis.major_tick_line_color = "#73574D"
figure3.yaxis[0].ticker.desired_num_ticks = 5

# Defini a faixa de datas desejada
new_start_date = pd.to_datetime('2022-05-01')
new_end_date = pd.to_datetime('2023-04-01')

# Defini a nova faixa do eixo x usando Range1d
figure3.x_range = Range1d(new_start_date, new_end_date)

#Tirei a logo
figure3.toolbar.logo = None