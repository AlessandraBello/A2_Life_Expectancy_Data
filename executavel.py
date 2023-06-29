import criar_plot as cp
import leitura_arquivo as la
import layout
import textos
from bokeh.models import FactorRange

grafico_1 = cp.grafico_de_dispercao("Life expectancy ", "Schooling", la.dados_grafico1, "blue", 0.6, "white" , 
                                    "Expectativa de Vida e Escolaridade, 2015", "Expectativa de Vida (em anos)", 
                                    "Escolaridade (em anos)")

grafico_2 = cp.grafico_de_linha("Year", "Life expectancy ", la.dados_grafico2, "white", 
                                "Expectativa de vida no Brasil, de 2000 a 2015", "Ano", "Expectativa de Vida")

grafico_3 = cp.grafico_de_barras( FactorRange(*la.doenca_ano), "eixo_x", "medias", la.dados_grafico3, "blue", "white", 
                                 "Média de vacinação nos anos de 2000 e 2015", "Doenças", "Média de vacinação (em %)")

graficos_alessandra = layout.agrupar("Alessandra.html", grafico_1, textos.texto_grafico_1, grafico_2, None, grafico_3, None)

grafico_4 = cp.grafico_de_dispercao("under-five deaths ", "Polio", la.dados_grafico4, "red", 0.5, "white", 
                                    "Mortalidade Infantil e Vacinação contra Polio em 2015", "Mortalidade Infantil", 
                                    "Vacinação contra poliomelite (em %)")