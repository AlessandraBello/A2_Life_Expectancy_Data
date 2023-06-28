from bokeh.plotting import figure
from bokeh.io import output_file, show

def grafico_de_dispercao (nome_arquivo, dados_x, dados_y, banco_de_dados, cor_glifo, titulo, nome_eixo_x, nome_eixo_y):
    output_file(nome_arquivo)
    grafico = figure()
    grafico.circle(x=dados_x, y=dados_y, source = banco_de_dados, color = cor_glifo)
    grafico.width = 1200
    grafico.height = 720
    grafico.title.text = titulo
    grafico.title.text_font = "Times New Roman"
    grafico.title.text_font_size = "20px"
    grafico.xaxis.axis_label = nome_eixo_x
    grafico.yaxis.axis_label = nome_eixo_y
    grafico.yaxis.major_label_orientation = "vertical"

    return show(grafico)