import leitura_arquivo as la
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import HoverTool, PanTool, WheelZoomTool, ResetTool, Patch, ColumnDataSource
from bokeh.transform import dodge


def grafico_4():
    continent_colors = {"Africa": "#9C640C", "Asia": "#7B241C", "Europe": "#1A5276", "North America": "#5B2C6F", "Oceania": "#D35400", "South America": "#1E8449"}

    output_file("grafico_4_1.html")
    grafico = figure(tools = [HoverTool(tooltips= [ ("Ano", "@x"),("% da população", "@y")] ),  PanTool(), WheelZoomTool(), ResetTool()])
    
    for continent in la.anos_magreza59_continente["Continent"].unique():
        df_continent = la.anos_magreza59_continente[la.anos_magreza59_continente["Continent"] == continent]
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

    grafico.yaxis.axis_label = "Prevalência da Magreza Extrema (em % da população)"
    grafico.yaxis.axis_label_text_font = "Times New Roman"
    grafico.yaxis.axis_label_text_font_size = "15px"
    grafico.yaxis.major_label_orientation = "vertical"
    grafico.yaxis.minor_tick_line_color = (135, 54, 0)

    grafico.legend.location = "center_left"
    grafico.legend.label_text_font_size = "13px"
    grafico.legend.background_fill_alpha = 0.5
    
    return(show(grafico))


def grafico_51():

    output_file("grafico_5.html")

    grafico = figure(tools = [HoverTool(tooltips= [ ("Ano", "@Year"),("Consumo", "@Alcohol")] ),  PanTool(), WheelZoomTool(), ResetTool()])
        
    grafico.varea(x = "Year", y1 = "Alcohol", y2 = 0, fill_color = "#DECE0B" , source = la.dados_grafico5 )

    grafico.toolbar.logo = None
    grafico.background_fill_color = (238, 225, 69,0.3)
    grafico.width = 640
    grafico.height = 480
    
    grafico.title.text = "Alcoolismo no Brasil (2000-2014)"
    grafico.title.text_font = "Times New Roman"
    grafico.title.text_font_size = "25px"
    grafico.title.align = "center"
    grafico.title.text_color = (144, 90, 1)

    grafico.xaxis.axis_label = "Linha do tempo"
    grafico.xaxis.axis_label_text_font = "Times New Roman"
    grafico.xaxis.axis_label_text_font_size = "15px"
    grafico.xaxis.minor_text_color = (144, 90, 1)

    grafico.yaxis.axis_label = "Consumo de álcool puro per capta (em litros)"
    grafico.yaxis.axis_label_text_font = "Times New Roman"
    grafico.yaxis.axis_label_text_font_size = "15px"
    grafico.yaxis.major_label_orientation = "vertical"
    grafico.yaxis.minor_text_color = (144, 90, 1)

    return(show(grafico))


def grafico_52():

    continent_colors = {"Africa": "#9C640C", "Asia": "#7B241C", "Europe": "#1A5276", "North America": "#5B2C6F", "Oceania": "#D35400", "South America": "#1E8449"}

    output_file("grafico_52.html")
    grafico = figure(tools = [HoverTool(tooltips= [ ("Ano", "@x"),("Consumo", "@y")] ),  PanTool(), WheelZoomTool(), ResetTool()])
    
    square_data = ColumnDataSource(data=dict(x=[2006.5, 2006.5, 2007.5, 2007.5], y=[9.5, 10.5, 10.5, 9.5],))
    square_patch = Patch(x="x", y="y", fill_color= (144, 90, 1, 0.3))
    grafico.add_glyph(square_data, square_patch)


    for continent in la.anos_alcool_continente["Continent"].unique():
        df_continent = la.anos_alcool_continente[la.anos_alcool_continente["Continent"] == continent]
        grafico.line(df_continent["Year"], df_continent["Alcohol"], color = continent_colors[continent], legend_label=continent, line_width=3)

    grafico.toolbar.logo = None
    grafico.background_fill_color = (238, 225, 69, 0.3)
    grafico.width = 640
    grafico.height = 480
    
    grafico.title.text = "Alcoolismo no Mundo (2000-2014)"
    grafico.title.text_font = "Times New Roman"
    grafico.title.text_font_size = "25px"
    grafico.title.align = "center"
    grafico.title.text_color = (144, 90, 1)

    grafico.xaxis.axis_label = "Linha do tempo"
    grafico.xaxis.axis_label_text_font = "Times New Roman"
    grafico.xaxis.axis_label_text_font_size = "15px"
    grafico.xaxis.minor_text_color = (144, 90, 1)

    grafico.yaxis.axis_label = "Consumo médio de álcool puro per capta (em litros)"
    grafico.yaxis.axis_label_text_font = "Times New Roman"
    grafico.yaxis.axis_label_text_font_size = "15px"
    grafico.yaxis.major_label_orientation = "vertical"
    grafico.yaxis.minor_text_color = (144, 90, 1)

    grafico.legend.location = "bottom_left"
    grafico.legend.label_text_font_size = "13px"
    grafico.legend.background_fill_alpha = 0.5

    
    return(show(grafico))


def grafico_53():
    output_file("grafico_53.html")

    grafico = figure(x_range = la.anos_alcool_europa["Country"], y_range = (0,20), tools = [HoverTool(tooltips= [ ("País", "@Country"),("Consumo", "@Alcohol")] ),  PanTool(), WheelZoomTool(), ResetTool()])
    
    grafico.vbar(x = dodge("Country", -0.18, range=grafico.x_range), top = "Alcohol", source = la.dados_grafico53, width = 0.7, color = "#DECE0B")

    grafico.toolbar.logo = None
    grafico.background_fill_color = (238, 225, 69, 0.3)
    grafico.width = 1300
    grafico.height = 550
    
    grafico.title.text = "Alcoolismo na Europa (2007)"
    grafico.title.text_font = "Times New Roman"
    grafico.title.text_font_size = "25px"
    grafico.title.align = "center"
    grafico.title.text_color = (144, 90, 1)

    grafico.xaxis.axis_label = "Países"
    grafico.xaxis.axis_label_text_font = "Times New Roman"
    grafico.xaxis.axis_label_text_font_size = "15px"
    grafico.xaxis.major_label_orientation = "vertical"
    grafico.xaxis.minor_text_color = (144, 90, 1)

    grafico.yaxis.axis_label = "Consumo de álcool puro per capta (em litros)"
    grafico.yaxis.axis_label_text_font = "Times New Roman"
    grafico.yaxis.axis_label_text_font_size = "15px"
    grafico.yaxis.major_label_orientation = "vertical"
    grafico.yaxis.minor_text_color = (144, 90, 1)


    return(show(grafico))


def grafico_6():
    output_file("grafico_6.html")
    
    grafico = figure(tools=[HoverTool(tooltips=[("País", "@Country")]), PanTool(), WheelZoomTool(), ResetTool()])

    grafico.circle(x="Adult Mortality", y="Income composition of resources", source=la.dados_grafico6, color=(12, 18, 96, 0.3), size = 7)

    grafico.toolbar.logo = None
    grafico.background_fill_color = (195, 198, 234, 0.3)
    grafico.width = 640
    grafico.height = 480

    grafico.title.text = "Taxa de Mortalidade e IDH no Mundo (2015)"
    grafico.title.text_font = "Times New Roman"
    grafico.title.text_font_size = "25px"
    grafico.title.align = "center"
    grafico.title.text_color = "#26294C"

    grafico.xaxis.axis_label = "Taxa de Mortalidade"
    grafico.xaxis.axis_label_text_font = "Times New Roman"
    grafico.xaxis.axis_label_text_font_size = "15px"
    grafico.xaxis.minor_text_color = "#26294C"

    grafico.yaxis.axis_label = "Índice de Desenvolvimento Humano (por país)"
    grafico.yaxis.axis_label_text_font = "Times New Roman"
    grafico.yaxis.axis_label_text_font_size = "15px"
    grafico.yaxis.major_label_orientation = "vertical"
    grafico.yaxis.minor_text_color = "#26294C"

    return show(grafico)


# print(grafico_4())
# print(grafico_51())
# print(grafico_52())
# print(grafico_53())
# print(grafico_6())


