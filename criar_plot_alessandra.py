from bokeh.plotting import figure
from bokeh.transform import dodge

def grafico_de_dispercao (range_x, range_y, dados_x, dados_y, banco_de_dados, cor_glifo, transparencia_glifo, cor_fundo, 
                          titulo_grafico, titulo_eixo_x, titulo_eixo_y):
    grafico = figure(x_range = range_x, y_range = range_y,tools = "box_zoom, zoom_in, pan, reset, save")
    grafico.toolbar.logo = None
    grafico.circle(x=dados_x, y=dados_y, source = banco_de_dados, color = cor_glifo, alpha = transparencia_glifo)
    grafico.width = 640
    grafico.height = 480
    grafico.background_fill_color = cor_fundo
    grafico.background_fill_alpha = 0.2
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
    grafico = figure(x_range = range_x, y_range = range_y, tools = "box_zoom, zoom_in, pan, reset, save")
    grafico.toolbar.logo = None
    grafico.line(x = eixo_x, y = eixo_y, source = dados, color = cor_linha, line_width = 2.5)
    grafico.width = 640
    grafico.height = 480
    grafico.background_fill_color = cor_fundo
    grafico.background_fill_alpha = 0.3
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

def grafico_de_barras(range_x, range_y, dados_x,  dados_y1, dados_y2, dados,cor_barras_1, cor_barras_2, transparencia, 
                      cor_fundo, titulo_grafico, titulo_eixo_x, titulo_eixo_y):
    grafico = figure(x_range = range_x, y_range = range_y, tools = "box_zoom, zoom_in, pan, reset, save")
    grafico.toolbar.logo = None
    grafico.vbar(x = dodge(dados_x, -0.18, range=grafico.x_range), top = dados_y1, source = dados, width = 0.3, 
                 color=cor_barras_1, alpha = transparencia, legend_label=dados_y1)
    grafico.vbar(x = dodge(dados_x, 0.18, range=grafico.x_range), top = dados_y2, source = dados, width = 0.3, 
                 color=cor_barras_2, alpha = transparencia, legend_label=dados_y2)
    grafico.width = 640
    grafico.height = 480
    grafico.background_fill_color = cor_fundo
    grafico.background_fill_alpha = 0.3
    grafico.title.text = titulo_grafico
    grafico.legend.label_text_font = "Arial"
    grafico.legend.border_line_width = 0
    grafico.legend.background_fill_alpha = 0.4
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