import criar_plot as cp
import leitura_arquivo as la
import layout
import textos
from bokeh.models import FactorRange

grafico_1 = cp.grafico_de_dispercao((50,90), (3,23), "Life expectancy ", "Schooling", la.dados_grafico1, "#27641D", 1, "#EBF8E9" , 
                                    "Expectativa de Vida e Escolaridade, 2015", "Expectativa de Vida (em anos)", 
                                    "Escolaridade (em anos)")

grafico_2 = cp.grafico_de_linha((1999,2016), (70,76), "Year", "Life expectancy ", la.dados_grafico2, "#27641D", "#EBF8E9", 
                                "Expectativa de vida no Brasil, de 2000 a 2015", "Ano", "Expectativa de Vida")

grafico_3 = cp.grafico_de_barras(FactorRange(*la.doenca_ano), (0,100), "eixo_x", "medias", la.dados_grafico3, "#27641D", 0.8,"#EBF8E9",
                                 "Média de vacinação nos anos de 2000 e 2015", "Doenças", "Média de vacinação (em %)")

graficos_alessandra = layout.agrupar("Alessandra.html", grafico_1, textos.texto_grafico_1, grafico_2, None, grafico_3, None)