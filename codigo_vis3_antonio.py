import pandas as pd
from bokeh.plotting import figure, curdoc, show
from bokeh.models import ColumnDataSource, HoverTool, RangeSlider, Button, PanTool, BoxZoomTool, ResetTool
from bokeh.layouts import column
from bokeh.palettes import Category10
import pandas as pd
from bokeh.plotting import figure, curdoc, show
from bokeh.models import ColumnDataSource, HoverTool, RangeSlider, Button, PanTool, BoxZoomTool, ResetTool
from bokeh.layouts import column
from bokeh.transform import linear_cmap
from bokeh.palettes import Reds, Greens
import pandas as pd
from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource, HoverTool, RangeSlider, Button, PanTool, BoxZoomTool, ResetTool
from bokeh.layouts import column
from bokeh.transform import linear_cmap
from bokeh.palettes import Reds, Greens

# Carrega o arquivo de dados
df = pd.read_csv("cleaned_coffee_dataset.csv")

# Calcula a contagem de "Category Two Defects" por país e ordenar em ordem decrescente
paises_contagem = df.groupby('Country of Origin')['Category Two Defects'].sum()

# Extrair os países e contagens
paises = paises_contagem.index.tolist()
contagens = paises_contagem.tolist()

# Criar uma paleta de cores gradiente de vermelho a verde
palette = ['#fff5f0', '#fee0d2', '#fcbba1', '#fc9272', '#fb6a4a', '#ef3b2c', '#cb181d', '#a50f15', '#67000d']

# Ordenar os países e as contagens
sorted_paises_contagens = sorted(zip(paises, contagens), key=lambda x: x[1], reverse=True)
paises, contagens = zip(*sorted_paises_contagens)

# Criar a fonte de dados do Bokeh
source = ColumnDataSource(data=dict(paises=paises, contagens=contagens))

# Configurar a ferramenta Hover
hover = HoverTool(
    tooltips=[
        ("País", "@paises"),
        ("Contagem", "@contagens")
    ]
)

# Cria o gráfico de barras
bar_plot = figure(x_range=paises, height=600, width=850, tools=[hover, PanTool(), BoxZoomTool(), ResetTool()])
bar_plot.vbar(x='paises', top='contagens', width=0.8, source=source, fill_color=linear_cmap('contagens', palette, min(contagens), max(contagens)))

# Configurar coisas do eixo x
bar_plot.xaxis.major_label_orientation = 'vertical'

# Configurar o grid
bar_plot.grid.grid_line_color = "lightgray"
bar_plot.grid.grid_line_alpha = 0.5

# Configurar linhas dos eixos
bar_plot.xaxis.axis_line_width = 1.2
bar_plot.yaxis.axis_line_width = 1.2

# Configurar os labels dos eixos
bar_plot.xaxis.axis_label = "Países"
bar_plot.yaxis.axis_label = "Contagem"

# Configurar o título do gráfico
bar_plot.title.text = "Contagem de Defeitos de Categoria 2, por país produtor"
bar_plot.title.align = "center"

# Criar o controle deslizante de faixa
range_slider = RangeSlider(title="Faixa", start=0, end=30, value=(0, 30), step=1)

# Criar o botão de redefinir
reset_button = Button(label="Resetar", button_type="default")

# Função de redefinição para redefinir os valores do controle deslizante
def reset():
    range_slider.value = (0, 30)

# Função de filtro para filtrar os dados com base no controle deslizante
def filter_data(attr, old, new):
    lower, upper = range_slider.value
    filtered_data = df[df['Country of Origin'].isin(paises)]
    filtered_data = filtered_data.groupby('Country of Origin').filter(lambda x: lower < len(x) < upper)
    filtered_counts = filtered_data.groupby('Country of Origin')['Category Two Defects'].sum()
    filtered_paises = filtered_counts.index.tolist()
    source.data = dict(paises=filtered_paises, contagens=filtered_counts.tolist())
    bar_plot.x_range.factors = filtered_paises

# Associar a função de filtro ao evento de alteração do controle deslizante
range_slider.on_change('value', filter_data)

# Associar a função de redefinição ao clique do botão de redefinição
reset_button.on_click(reset)

# Criar o layout da aplicação
layout = column(bar_plot, range_slider, reset_button)

# Exibir a aplicação
curdoc().add_root(layout)