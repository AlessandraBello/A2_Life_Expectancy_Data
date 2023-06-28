import criar_plot as cp
import leitura_arquivo as la

grafico_1 = cp.grafico_de_dispercao("expectativa_de_vida_escolaridade.html", "Life expectancy ", "Schooling", 
                                    la.dados_grafico1, "blue", "Expectativa de Vida e Escolaridade", 
                                    "Expectativa de Vida (em anos)", "Escolaridade (em anos)")