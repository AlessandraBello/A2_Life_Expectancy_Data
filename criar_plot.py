from bokeh.plotting import figure
from bokeh.io import output_file, show

def grafico_de_dispercao (nome_arquivo_final, dados_x, dados_y, banco_de_dados, cor_glifo, titulo_grafico, titulo_eixo_x, titulo_eixo_y):
    output_file(nome_arquivo_final)
    grafico = figure(tools = "box_zoom, zoom_in, pan, reset, save, wheel_zoom")
    grafico.toolbar.logo = None
    grafico.circle(x=dados_x, y=dados_y, source = banco_de_dados, color = cor_glifo)
    grafico.width = 640
    grafico.height = 480
    grafico.title.text = titulo_grafico
    grafico.title.text_font = "Arial"
    grafico.title.text_font_size = "20px"
    grafico.title.align = "center"
    grafico.xaxis.axis_label = titulo_eixo_x
    grafico.xaxis.axis_label_text_font = "Arial"
    grafico.xaxis.axis_label_text_font_size = "15px"
    grafico.yaxis.axis_label = titulo_eixo_y
    grafico.yaxis.axis_label_text_font = "Arial"
    grafico.yaxis.axis_label_text_font_size = "15px"
    grafico.yaxis.major_label_orientation = "vertical"

    return show(grafico)