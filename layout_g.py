from bokeh.layouts import gridplot
from bokeh.plotting import figure
from bokeh.io import output_file, show

def agrupar (nome, plot1, texto1, plot2, texto2,  plot3, texto3):
    output_file (nome)
    grid = figure(tools = "box_zoom, zoom_in, pan, reset, save, wheel_zoom")
    grid.toolbar.logo = None
    grid = gridplot([[plot1, texto1], [plot2, texto2], [plot3, texto3]], merge_tools=False, 
                    toolbar_options=dict(logo=None))
    return show(grid)