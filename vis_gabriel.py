from bokeh.io import show
from codigo_vis1_gabriel import figure1
from codigo_vis2_gabriel import figure2
from codigo_vis3_gabriel import figure3
from bokeh.layouts import column


show(column(figure1,figure2,figure3))