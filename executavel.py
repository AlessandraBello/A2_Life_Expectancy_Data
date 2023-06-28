import criar_plot as cp
import leitura_arquivo as la

grafico_1 = cp.grafico_de_dispercao("expectativa_de_vida_escolaridade.html","Life expectancy ", "Schooling", 
                                    la.dados_grafico1, "blue", "Expectativa de Vida e Escolaridade", 
                                    "expectativa de vida, em anos", "anos que passou na escola")