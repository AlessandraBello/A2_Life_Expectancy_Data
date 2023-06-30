import leitura_arquivo_giovanna as la
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import HoverTool, PanTool, WheelZoomTool, ResetTool, Patch, ColumnDataSource
from bokeh.transform import dodge
from giovanna_plots import grafico_51, grafico_52, grafico_53
from bokeh.layouts import gridplot

#criando as variáveis dos gráficos
grafico_5_1 = grafico_51()
grafico_5_2 = grafico_52()
grafico_5_3 = grafico_53()

#criando o gridplot
grid_alcoolismo1 = gridplot([[grafico_5_2, grafico_5_1]])

grid_alcoolismo1.toolbar.logo = None

grid_alcoolismo2 = gridplot([[grid_alcoolismo1],[grafico_5_3]])

grid_alcoolismo2.toolbar.logo = None

output_file("grid_alcoolismo2.html")

show(grid_alcoolismo2)

