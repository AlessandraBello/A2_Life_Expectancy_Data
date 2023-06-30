from bokeh.plotting import figure
from bokeh.models import HoverTool
from bokeh.transform import dodge

#define a função para um gráfico de disperção, recebe vários parâmetros que serão utilizados para gerar o plot
def grafico_de_dispercao (range_x, range_y, eixo_x, eixo_y, dado_plot_1, dado_plot_2, dado_plot_3, dado_plot_4, dado_plot_5, 
                          dado_plot_6, cor_plot_1, cor_plot_2, cor_plot_3, cor_plot_4, cor_plot_5, cor_plot_6, 
                          transparencia_glifo, cor_fundo, titulo_grafico, titulo_eixo_x, titulo_eixo_y):
    #gera a figura com os ranges dos eixos e a barra de ferramentas
    grafico = figure(x_range = range_x, y_range = range_y,tools = "box_zoom, zoom_in, pan, reset, save")
    #retira a logo
    grafico.toolbar.logo = None
    #gera os gráficos de circulos
    grafico.circle(x=eixo_x, y=eixo_y, source = dado_plot_1, color = cor_plot_1, alpha = transparencia_glifo, size = 7, legend_label="Africa")
    grafico.circle(x=eixo_x, y=eixo_y, source = dado_plot_2, color = cor_plot_2, alpha = transparencia_glifo, size = 7,legend_label="América do Sul")
    grafico.circle(x=eixo_x, y=eixo_y, source = dado_plot_3, color = cor_plot_3, alpha = transparencia_glifo, size = 7, legend_label="América do Norte")
    grafico.circle(x=eixo_x, y=eixo_y, source = dado_plot_4, color = cor_plot_4, alpha = transparencia_glifo, size = 7, legend_label="Asia")
    grafico.circle(x=eixo_x, y=eixo_y, source = dado_plot_5, color = cor_plot_5, alpha = transparencia_glifo, size = 7, legend_label="Europa")
    grafico.circle(x=eixo_x, y=eixo_y, source = dado_plot_6, color = cor_plot_6, alpha = transparencia_glifo, size = 7, legend_label="Oceania")
    #ajusta tamanho do gráfico
    grafico.width = 640
    grafico.height = 480
    #ajusta a cor e transparencia do fundo do gráfico
    grafico.background_fill_color = cor_fundo
    grafico.background_fill_alpha = 0.2
    #arruma fonte, localização e caixa da legenda
    grafico.legend.label_text_font = "Arial"
    grafico.legend.border_line_width = 0
    grafico.legend.background_fill_alpha = 0.4
    grafico.legend.location = "bottom_right"
    #ativa ferramenta que permite ao usuário clicar na legenda para fazer os itens correspondentes ficarem mais claros
    grafico.legend.click_policy = "mute"
    #criação título com ajuste da sua fonte, tamanho e localização
    grafico.title.text = titulo_grafico
    grafico.title.text_font = "Arial"
    grafico.title.text_font_size = "20px"
    grafico.title.align = "center"
    #adição da ferramenta Hover, que permite ao usuário ver os dados ao passar o mouse sobre o gráfico
    hover = HoverTool(tooltips=[("Escolaridade", "@Schooling"),
                                ("Expectativa de Vida", "@{Life expectancy }")])
    grafico.add_tools(hover)
    #cria título dos eixos e ajusta fonte, tamanho e orientação
    grafico.xaxis.axis_label = titulo_eixo_x
    grafico.xaxis.axis_label_text_font = "Arial"
    grafico.xaxis.axis_label_text_font_size = "15px"
    grafico.yaxis.axis_label = titulo_eixo_y
    grafico.yaxis.axis_label_text_font = "Arial"
    grafico.yaxis.axis_label_text_font_size = "15px"
    grafico.yaxis.major_label_orientation = "vertical"
    #retorna o gráfico
    return grafico

#define a função para um gráfico de linha, recebe vários parâmetros que serão utilizados para gerar o plot
def grafico_de_linha(range_x, range_y, eixo_x, eixo_y, dados, cor_linha, cor_fundo, título_gráfico, titulo_eixo_x, 
                     titulo_eixo_y):
    #gera a figura com os ranges dos eixos e a barra de ferramentas
    grafico = figure(x_range = range_x, y_range = range_y, tools = "box_zoom, zoom_in, pan, reset, save")
    #retira a logo
    grafico.toolbar.logo = None
    #gera o gráfico de linha com os dados que recebe e ajusta o tamanho da linha
    grafico.line(x = eixo_x, y = eixo_y, source = dados, color = cor_linha, line_width = 2.5)
    #ajusta tamanho do gráfico
    grafico.width = 640
    grafico.height = 480
    #ajusta a cor e transparencia do fundo do gráfico
    grafico.background_fill_color = cor_fundo
    grafico.background_fill_alpha = 0.3
    #adição da ferramenta Hover, que permite ao usuário ver os dados ao passar o mouse sobre o gráfico
    hover = HoverTool(tooltips=[("Ano", "@Year"),
                                ("Expectativa de Vida", "@{Life expectancy }")])
    grafico.add_tools(hover)
    #criação título e ajuste da fonte, tamanho e localização
    grafico.title.text = título_gráfico
    grafico.title.text_font = "Arial"
    grafico.title.text_font_size = "20px"
    grafico.title.align = "center"
    #cria título dos eixos e ajuste da fonte, tamanho e orientação
    grafico.xaxis.axis_label = titulo_eixo_x
    grafico.xaxis.axis_label_text_font = "Arial"
    grafico.xaxis.axis_label_text_font_size = "15px"
    grafico.yaxis.axis_label = titulo_eixo_y
    grafico.yaxis.axis_label_text_font = "Arial"
    grafico.yaxis.axis_label_text_font_size = "15px"
    grafico.yaxis.major_label_orientation = "vertical"
    #retorna o gráfico
    return grafico

#define a função para um gráfico de barras, recebe vários parâmetros que serão utilizados para gerar o plot
def grafico_de_barras(range_x, range_y, eixo_x,  eixo_y1, eixo_y2, dados,cor_barras_1, cor_barras_2, transparencia, 
                      cor_fundo, titulo_grafico, titulo_eixo_x, titulo_eixo_y):
    #gera a figura com os ranges dos eixos e a barra de ferramentas
    grafico = figure(x_range = range_x, y_range = range_y, tools = "box_zoom, zoom_in, pan, reset, save")
    #retira a logo
    grafico.toolbar.logo = None
    #gera os gráficos de barra com os dados fornecidos
    grafico.vbar(x = dodge(eixo_x, -0.18, range=grafico.x_range), top = eixo_y1, source = dados, width = 0.3, 
                 color=cor_barras_1, alpha = transparencia, legend_label=eixo_y1)
    grafico.vbar(x = dodge(eixo_x, 0.18, range=grafico.x_range), top = eixo_y2, source = dados, width = 0.3, 
                 color=cor_barras_2, alpha = transparencia, legend_label=eixo_y2)
    #ajusta tamanho do gráfico
    grafico.width = 640
    grafico.height = 480
    #ajusta a cor e transparencia do fundo do gráfico
    grafico.background_fill_color = cor_fundo
    grafico.background_fill_alpha = 0.3
    #arruma fonte, localização e caixa da legenda
    grafico.legend.label_text_font = "Arial"
    grafico.legend.border_line_width = 0
    grafico.legend.background_fill_alpha = 0.4
    #criação título e ajuste da fonte, tamanho e localização
    grafico.title.text = titulo_grafico
    grafico.title.text_font = "Arial"
    grafico.title.text_font_size = "20px"
    grafico.title.align = "center"
    #cria título dos eixos e ajuste da fonte, tamanho e orientação
    grafico.xaxis.axis_label = titulo_eixo_x
    grafico.xaxis.axis_label_text_font = "Arial"
    grafico.xaxis.axis_label_text_font_size = "15px"
    grafico.yaxis.axis_label = titulo_eixo_y
    grafico.yaxis.axis_label_text_font = "Arial"
    grafico.yaxis.axis_label_text_font_size = "15px"
    grafico.yaxis.major_label_orientation = "vertical"
    #retorna o gráfico
    return grafico