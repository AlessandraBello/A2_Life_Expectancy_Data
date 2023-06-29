import criar_plot as cp
import leitura_arquivo as la

grafico_1 = cp.grafico_de_dispercao("expectativa_de_vida_escolaridade.html", "Life expectancy ", "Schooling", 
                                    la.dados_grafico1, "blue", 0.6, "white" , "Expectativa de Vida e Escolaridade, 2015", 
                                    "Expectativa de Vida (em anos)", "Escolaridade (em anos)")

grafico_2 = cp.grafico_de_linha("evolucao_expectativa_brasil.html", "Year", "Life expectancy ", la.dados_grafico2, "white", "Expectativa de vida no Brasil, de 2000 a 2015", "Ano", "Expectativa de Vida")

grafico_4 = cp.grafico_de_dispercao("mortalidade_infantil_polio.html", "under-five deaths ", "Polio", la.dados_grafico4, 
                                    "red", 0.5, "white", "Mortalidade Infantil e Vacinação contra Polio em 2015", 
                                    "Mortalidade Infantil", "Vacinação contra poliomelite (em %)")

