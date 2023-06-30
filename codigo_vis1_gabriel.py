#Import para a visualização em bokeh
from bokeh.plotting import figure
from bokeh.models import HoverTool, NumeralTickFormatter
import numpy as np

#Importei do meu módulo os dados para o gráfico
from manipulacao_dados_gabriel import correlacao_quantidade_qualidade

# Dados
x = correlacao_quantidade_qualidade.data['media']
y = correlacao_quantidade_qualidade.data['producao']

# Criar um objeto Figure
figure1 = figure(tools ='')

# Plotar os pontos de dispersão
figure1.circle(source=correlacao_quantidade_qualidade, x='media', y='producao', fill_color="#73574D", line_color="#73574D", size=10)

# Calcular os coeficientes da reta de regressão
coefficients = np.polyfit(x, y, 1)
slope = coefficients[0]
intercept = coefficients[1]

# Traçar a reta de regressão
x_regression = np.array([min(x), max(x)])
y_regression = slope * x_regression + intercept
figure1.line(x_regression, y_regression, line_color='#260B01', line_width=3, legend_label = "Reta de regressão")

# Configurações adicionais do gráfico
figure1.width = 600
figure1.height = 400
figure1.background_fill_color = "#D9CCC5"
figure1.title.text = 'Quantidade é Qualidade?'
figure1.title.text_color = "#73574D"
figure1.title.text_font = "Arial"
figure1.title.text_font_size = "22px"
figure1.title.align = "left"
figure1.x_range.start = 7
figure1.x_range.end = 8
figure1.y_range.start = -200
figure1.y_range.end = 350000
figure1.xaxis[0].ticker.desired_num_ticks = 2
figure1.yaxis[0].ticker.desired_num_ticks = 3
figure1.xaxis[0].ticker.num_minor_ticks = 0
figure1.yaxis[0].ticker.num_minor_ticks = 0
figure1.grid.grid_line_alpha = 0
figure1.xaxis.axis_label = "Nota"
figure1.yaxis.axis_label = "Produção (kg)"
figure1.xaxis.axis_label_text_font_size = "11pt"
figure1.yaxis.axis_label_text_font_size = "11pt"
figure1.xaxis.axis_label_text_color = "#3D2923"
figure1.yaxis.axis_label_text_color = "#3D2923"
figure1.xaxis.minor_tick_line_color = "#3D2923"
figure1.yaxis.minor_tick_line_color = "#3D2923"
figure1.xaxis.minor_tick_in = 0
figure1.yaxis.minor_tick_in = 0
figure1.xaxis.major_tick_in = 0
figure1.yaxis.major_tick_in = 0
figure1.axis.major_label_text_color = "#3D2923"
figure1.xaxis.axis_line_width = 2
figure1.yaxis.axis_line_width = 2
figure1.xaxis.axis_line_color = "#73574D"
figure1.yaxis.axis_line_color = "#73574D"
figure1.yaxis.formatter = NumeralTickFormatter(format="0")

#Adicionei interação para ao passar o mouse por cima da bolinha aparecer informações sobre o país, a produção e a qualidade do café
tooltips = [("País", "@paises"),
            ("Produção em kg", "@producao"),
            ("Qualidade do Café", "@media")]
figure1.add_tools(HoverTool(tooltips=tooltips))

#Adicionei as tools de interação para o gráfico 1
figure1.add_tools('wheel_zoom')
figure1.add_tools('pan')
figure1.add_tools('reset')
figure1.add_tools('lasso_select')
figure1.toolbar.logo = None