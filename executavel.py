import criar_plot_alessandra as cp
import leitura_arquivo as la
import layout
import textos
import giovanna_plots as gp
import grid_giovanna as gg
import manuela_plots as mp

#gera o gráfico 1, bastando apenas fornecer os parâmetros necessários
grafico_1 = cp.grafico_de_dispercao((50,90), (3,22), "Life expectancy ", "Schooling", la.dados_grafico1_1, 
                                    la.dados_grafico1_2, la.dados_grafico1_3, la.dados_grafico1_4, la.dados_grafico1_5, 
                                    la.dados_grafico1_6, "#000000", "#B71C1C","#9E9E9E","#FFEB3B", "#2196F3", "#F48FB1", 
                                    1, "#C8E6C9" , "Relaçao entre expectativa de vida e escolaridade, 2015", 
                                    "Expectativa de vida (em anos)", "Escolaridade (em anos)")

#gera o gráfico 2, bastando apenas fornecer os parâmetros necessários
grafico_2 = cp.grafico_de_linha((1999,2016), (70,76), "Year", "Life expectancy ", la.dados_grafico2, "#1B5E20", "#C8E6C9", 
                                "Expectativa de vida no Brasil, de 2000 a 2015", "Ano", "Expectativa de Vida (em anos)")

#gera o gráfico 3, bastando apenas fornecer os parâmetros necessários
grafico_3 = cp.grafico_de_barras(la.doencas_e_medias_por_ano["doenca"], (0,110),"doenca","2000", "2015", la.dados_grafico3,
                                 "#1B5E20","#303F9F", 0.8,"#C8E6C9", "Média de vacinação em crianças de até 1 ano", 
                                 "Doenças", "Média de vacinação (em %)")

#gera um único html com os 3 gráficos gerados e os 3 textos correspondentes
graficos_alessandra = layout.agrupar("Alessandra.html", grafico_1, textos.texto_grafico_1, grafico_2, 
                                     textos.texto_grafico_2, grafico_3, textos.texto_grafico_3)

#chama o gráfico 4
grafico4 = gp.grafico_4()

#chama o grid/gráfico 5
grafico5 = gg.grid_giovanna()

#chama o gráfico 6
grafico6 = gp.grafico_6()

#criando o html com os gráficos e os textos
graficos_giovanna = layout.agrupar("Giovanna.html", grafico4, textos.texto_grafico_4, grafico5, textos.texto_grafico_5, 
                                   grafico6, textos.texto_grafico_6)

# Chama a função do gráfico 7
grafico_7 = mp.grafico7()

# Chama a função do gráfico 8
grafico_8 = mp.grafico8()

# Chama a função do gráfico 9
grafico_9 = mp.grafico9()

# Cria um html com os gráficos e seus respectivos textos
graficos_manuela = layout.agrupar("Manuela.html", grafico_7, textos.texto_grafico_7, grafico_8, textos.texto_grafico_8, 
                                  grafico_9, textos.texto_grafico_9)