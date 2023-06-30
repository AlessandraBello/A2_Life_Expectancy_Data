import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, HoverTool, PanTool, WheelZoomTool, ResetTool, LinearColorMapper, ColorBar
from bokeh.palettes import Magma256
import leitura_arquivo as la


def grafico7():

    # Define uma cor para cada continente
    continent_colors = {"Africa": "#E74C3C", "Asia": "#F39C12", "Europe": "#3498DB", "North America": "#DD1491", "Oceania": "#8E44AD", "South America": "#1ABC9C"}

    # Cria o gráfico e configura as ferramentas usadas
    grafico7 = figure(tools = [HoverTool(tooltips=[("Ano", "@x"), ("Expectativa de Vida", "@y")]), PanTool(), WheelZoomTool(), ResetTool(), ])

    # Plota as linhas para cada continente
    for continent in la.media_expectativa_por_continente["Continent"].unique():
        df_continent = la.media_expectativa_por_continente[la.media_expectativa_por_continente["Continent"] == continent]
        grafico7.line(df_continent["Year"], df_continent["Life expectancy "], color = continent_colors[continent], legend_label = continent, line_width = 2)

    # Configurações gerais do gráfico:

    # Barra de ferramentas
    grafico7.toolbar.logo = None
    grafico7.toolbar.autohide = True
    # Dimensões
    grafico7.width = 640
    grafico7.height = 480
    # Título e rótulos de linha
    grafico7.title.text = "Média de Expectativa de Vida por Ano para Cada Continente"
    grafico7.title.text_font = "Arial Black"
    grafico7.title.text_font_size = "18px"
    grafico7.title.align = "center"
    grafico7.xaxis.axis_label = "Ano"
    grafico7.xaxis.axis_label_text_font = "Verdana"
    grafico7.xaxis.axis_label_text_font_size = "15px"
    grafico7.yaxis.axis_label = "Expectativa de Vida"
    grafico7.yaxis.axis_label_text_font = "Verdana"
    grafico7.yaxis.axis_label_text_font_size = "15px"
    grafico7.yaxis.major_label_orientation = "vertical"
    # Cores
    grafico7.background_fill_color = "white"
    # Eixos
    grafico7.xaxis.ticker.num_minor_ticks = 2
    grafico7.yaxis.ticker.num_minor_ticks = 5
    # Grid
    grafico7.ygrid.minor_grid_line_dash = "dotted"
    grafico7.ygrid.grid_line_color = "#F2DFF2"
    grafico7.xgrid.grid_line_color = "#F2DFF2"
    grafico7.ygrid.minor_grid_line_color = "#F2DFF2"
    grafico7.xgrid.minor_grid_line_color = "#F2DFF2"
    grafico7.ygrid.minor_grid_line_alpha = 0.5
    grafico7.xgrid.minor_grid_line_alpha = 0.6
    # Legenda
    grafico7.legend.location = "bottom_left"

    return show(grafico7)


def grafico8():

    # Definine a paleta de cores usada no gráfico
    cores = Magma256[::-1]  

    # Obtém o valor mínimo e máximo dos dados
    valor_min = la.dados_heatmap.min().min()
    valor_max = la.dados_heatmap.max().max()

    # Cria uma paleta de cores para o heatmap baseada nos valores máximo e mínimo
    paleta_heatmap = LinearColorMapper(palette = cores, low = valor_min, high = valor_max)

    # Cria um objeto de figura para o heatmap
    heatmap = figure(x_range = la.anos_str, y_range = la.paises_america_sul, tools = "box_zoom, wheel_zoom, reset, save")

    # Adiciona os retângulos coloridos ao heatmap
    retangulos = heatmap.rect(x = "level_0", y = "level_1", width = 1, height = 1, fill_color = {"field": "valor", "transform": paleta_heatmap}, line_color = None, source = la.dados_grafico8)

    # Adiciona a legenda de cores ao lado direito do heatmap
    legenda_cores = ColorBar(color_mapper = paleta_heatmap)
    heatmap.add_layout(legenda_cores, "right")

    # Adiciona e configura a ferramenta hover
    hover = HoverTool(renderers = [retangulos], tooltips = [("País", "@level_1"), ("Expectativa de Vida", "@valor")])
    heatmap.add_tools(hover)

    # Configurações gerais do gráfico: 

    # Barra de ferramentas
    heatmap.toolbar.logo = None
    heatmap.toolbar.autohide = True
    # Título e rótulos de linha
    heatmap.title.text = "Expectativa de Vida - América do Sul"
    heatmap.title.text_font = "Arial Black"
    heatmap.title.text_font_size = "18px"
    heatmap.title.align = "center"
    heatmap.xaxis.axis_label = "Ano"
    heatmap.xaxis.axis_label_text_font = "Verdana"
    heatmap.xaxis.axis_label_text_font_size = "15px"
    heatmap.yaxis.axis_label = "País"
    heatmap.yaxis.axis_label_text_font = "Verdana"
    heatmap.yaxis.axis_label_text_font_size = "15px"
    heatmap.xaxis.major_label_text_font_size = "10px"
    # Dimensões 
    heatmap.width = 640
    heatmap.height = 480

    return heatmap

