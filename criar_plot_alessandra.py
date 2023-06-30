from bokeh.plotting import figure

def grafico_de_dispercao (range_x, range_y, dados_x, dados_y, banco_de_dados, cor_glifo, transparencia_glifo, cor_fundo, 
                          titulo_grafico, titulo_eixo_x, titulo_eixo_y):
    grafico = figure(x_range = range_x, y_range = range_y,tools = "box_zoom, zoom_in, pan, reset, save, wheel_zoom")
    grafico.toolbar.logo = None
    grafico.circle(x=dados_x, y=dados_y, source = banco_de_dados, color = cor_glifo, alpha = transparencia_glifo)
    grafico.width = 640
    grafico.height = 480
    grafico.background_fill_color = cor_fundo
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

    return grafico

def grafico_de_linha(range_x, range_y, eixo_x, eixo_y, dados, cor_linha, cor_fundo, título_gráfico, titulo_eixo_x, 
                     titulo_eixo_y):
    grafico = figure(x_range = range_x, y_range = range_y, tools = "box_zoom, zoom_in, pan, reset, save, wheel_zoom")
    grafico.toolbar.logo = None
    grafico.line(x = eixo_x, y = eixo_y, source = dados, color = cor_linha, line_width = 2.5)
    grafico.width = 640
    grafico.height = 480
    grafico.background_fill_color = cor_fundo
    grafico.title.text = título_gráfico
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

    return grafico

def grafico_de_barras(range_x, range_y, dados_x, dados_y, dados, cor_barras, transparencia, cor_fundo, titulo_grafico, 
                      titulo_eixo_x, titulo_eixo_y):
    grafico = figure(x_range = range_x, y_range = range_y, tools = "box_zoom, zoom_in, pan, reset, save, wheel_zoom")
    grafico.toolbar.logo = None
    grafico.vbar(x = dados_x, top = dados_y, source = dados, width = 0.8, color = cor_barras, alpha = transparencia)
    grafico.width = 640
    grafico.height = 480
    grafico.background_fill_color = cor_fundo
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
    
    return grafico