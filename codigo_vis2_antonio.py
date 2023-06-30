from bokeh.plotting import figure, show
from bokeh.models import HoverTool
from cds_reader import source_para_vis_2, data_para_vis_2

quakers_aroma = figure(title="Quakers: Grãos imaturos prejudicam o aroma do café",
                       x_axis_label="Quakers",
                       y_axis_label="Nota do Aroma: 1 a 10",
                       width=513,
                       height=483
                       )

#Plotar os circulos
dados = source_para_vis_2(data_para_vis_2)
alpha = source_para_vis_2(data_para_vis_2).data['Alpha']

quakers_aroma.circle(source = dados, x='Quakers', y ='Aroma', fill_color='Blue',
                     line_color='Black',
                     fill_alpha = 'Alpha',
                     legend_label="Pontuação geral: Maior para menor, mais escuro para mais claro",
                     size=10
                     )

hover = HoverTool(tooltips=[("Quakers", "@Quakers"), ("Aroma", "@Aroma"), ("Pontuação Geral", "@Overall")])
quakers_aroma.add_tools(hover)

# Retirando logo do Bokeh
quakers_aroma.toolbar.logo = None

show(quakers_aroma)