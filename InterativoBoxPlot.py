#bibliotecas utilizadas
from myfunctions import generate_boxplot
from bokeh.models import TabPanel, Tabs
from bokeh.plotting import show

#Criando os intens pra usar no tabpanel
plot1=generate_boxplot("Aroma")
plot2=generate_boxplot("Flavor")
plot3=generate_boxplot("Aftertaste")
plot4=generate_boxplot("Acidity")
plot5=generate_boxplot("Balance")
plot6=generate_boxplot("Uniformity")
plot7=generate_boxplot("Overall")

#criando os tabpanel
tab1 = TabPanel(child=plot1, title="Aroma")
tab2 = TabPanel(child=plot2, title="Flavor")
tab3 = TabPanel(child=plot3, title="Aftertaste")
tab4 = TabPanel(child=plot4, title="Acidity")
tab5 = TabPanel(child=plot5, title="Balance")
tab6 = TabPanel(child=plot6, title="Uniformity")
tab7 = TabPanel(child=plot7, title="Overall")

#função show pra mostrar o resultado final
show(Tabs(tabs=[tab1, tab2, tab3, tab4, tab5, tab6, tab7]))

