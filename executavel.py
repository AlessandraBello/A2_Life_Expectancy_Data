import criar_plot_alessandra as cp
import leitura_arquivo as la
import layout
import textos
from bokeh.models import FactorRange

grafico_1 = cp.grafico_de_dispercao((50,90), (3,23), "Life expectancy ", "Schooling", la.dados_grafico1, "#27641D", 1, 
                                    "#EBF8E9" , "Expectativa de Vida e Escolaridade, 2015", "Expectativa de Vida (em anos)", 
                                    "Escolaridade (em anos)")

grafico_2 = cp.grafico_de_linha((1999,2016), (70,76), "Year", "Life expectancy ", la.dados_grafico2, "#27641D", "#EBF8E9", 
                                "Expectativa de vida no Brasil, de 2000 a 2015", "Ano", "Expectativa de Vida")

grafico_3 = cp.grafico_de_barras(la.doencas_e_medias_por_ano["doenca"], (0,110),"doenca","2000", "2015", la.dados_grafico3,"#0AA501","#27641D", 
                                 0.8,"#EBF8E9", "Média de vacinação nos anos de 2000 e 2015", "Doenças", 
                                 "Média de vacinação (em %)")

graficos_alessandra = layout.agrupar("graficos/Alessandra.html", grafico_1, textos.texto_grafico_1, grafico_2, 
                                     textos.texto_grafico_2, grafico_3, textos.texto_grafico_3)