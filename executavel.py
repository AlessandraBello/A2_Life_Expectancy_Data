import criar_plot_alessandra as cp
import leitura_arquivo as la
import layout
import textos

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
graficos_alessandra = layout.agrupar("docs/Alessandra.html", grafico_1, textos.texto_grafico_1, grafico_2, 
                                     textos.texto_grafico_2, grafico_3, textos.texto_grafico_3)