from bokeh.layouts import gridplot
from bokeh.plotting import figure
from bokeh.io import output_file, show

#cria o html com os gráficos e os textos
#recebe como parametros 3 gráficos e tres textos
def agrupar (nome, plot1, texto1, plot2, texto2,  plot3, texto3):
    # gera o arquivo de saida
    output_file (nome)
    #cria o html e retira a logo
    grid = figure()
    grid.toolbar.logo = None
    #adiciona os gráficos e textos
    grid = gridplot([[plot1, texto1], [plot2, texto2], [plot3, texto3]], merge_tools=False, 
                    toolbar_options=dict(logo=None))
    #retorna a visualização do html
    return show(grid)