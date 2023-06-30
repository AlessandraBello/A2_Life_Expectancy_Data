import leitura_arquivo as la
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import HoverTool, PanTool, WheelZoomTool, ResetTool
import pandas as pd

def grafico_linhadotempo1():
    continent_colors = {"Africa": "#9C640C", "Asia": "#7B241C", "Europe": "#1A5276", "North America": "#5B2C6F", "Oceania": "#D35400", "South America": "#1E8449"}

    output_file("grafico_4_1.html")
    grafico = figure(tools = [HoverTool(tooltips= [ ("Year", "@x"),(" thinness 5-9 years", "@y")] ),  PanTool(), WheelZoomTool(), ResetTool()])
    
    for continent in la.dados_grafico4.data["Continent"].unique():
        df_continent = la.dados_grafico4[la.dados_grafico4["Continent"] == continent]
        grafico.line(df_continent["Year"], df_continent[" thinness 5-9 years"], color = continent_colors[continent], legend_label=continent, line_width=3)

    grafico.toolbar.logo = None
    grafico.background_fill_color = (237, 187, 153, 0.2)
    grafico.width = 640
    grafico.height = 480
    
    grafico.title.text = "Magreza Extrema entre 5 e 9 Anos no Mundo"
    grafico.title.text_font = "Times New Roman"
    grafico.title.text_font_size = "25px"
    grafico.title.align = "center"
    grafico.title.text_color = (135, 54, 0)

    grafico.xaxis.axis_label = "Linha do tempo"
    grafico.xaxis.axis_label_text_font = "Times New Roman"
    grafico.xaxis.axis_label_text_font_size = "15px"
    grafico.xaxis.minor_tick_line_color = (135, 54, 0)

    grafico.yaxis.axis_label = "Prevalência da Magreza Extrema (em %)"
    grafico.yaxis.axis_label_text_font = "Times New Roman"
    grafico.yaxis.axis_label_text_font_size = "15px"
    grafico.yaxis.major_label_orientation = "vertical"
    grafico.yaxis.minor_tick_line_color = (135, 54, 0)

    grafico.legend.location = "bottom_left"
    
    
    return(show(grafico))

print(grafico_linhadotempo1())




