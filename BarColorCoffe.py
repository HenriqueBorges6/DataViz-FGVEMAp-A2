from myfunctions import barplot, vertical_bar
from bokeh.plotting import figure, show
from bokeh.models import TabPanel, Tabs

p = barplot()
tab1 = TabPanel(child=p, title="Horizontal")
q = vertical_bar()
tab2 = TabPanel(child=q, title="Vertical")

show(Tabs(tabs=[tab1, tab2]))