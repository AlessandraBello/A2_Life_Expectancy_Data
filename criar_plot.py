from bokeh.plotting import figure

def grafico_de_dispercao (dados_x, dados_y, banco_de_dados, cor_glifo, transparencia_glifo, cor_fundo, titulo_grafico, 
                          titulo_eixo_x, titulo_eixo_y):
    grafico = figure(x_range = (50,90), y_range = (3,23),tools = "box_zoom, zoom_in, pan, reset, save, wheel_zoom")
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

def grafico_de_linha(eixo_x, eixo_y, dados, cor_linha, cor_fundo, título_gráfico, titulo_eixo_x, titulo_eixo_y):
    grafico = figure(x_range = (1999,2016), y_range = (70,76), tools = "box_zoom, zoom_in, pan, reset, save, wheel_zoom")
    grafico.toolbar.logo = None
    grafico.line(x = eixo_x, y = eixo_y, source = dados, color = cor_linha)
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

def grafico_de_barras(nomes_eixo_x, dados_x, dados_y, dados, cor_barras, cor_fundo, titulo_grafico, titulo_eixo_x, titulo_eixo_y):
    grafico = figure(x_range = nomes_eixo_x, y_range = (0,100), tools = "box_zoom, zoom_in, pan, reset, save, wheel_zoom")
    grafico.toolbar.logo = None
    grafico.vbar(x = dados_x, top = dados_y, source = dados, width = 0.9, color = cor_barras)
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