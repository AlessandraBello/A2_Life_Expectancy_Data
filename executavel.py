import criar_plot as cp
import leitura_arquivo as la

grafico_1 = cp.grafico_de_dispercao("expectativa_de_vida_escolaridade.html", "Life expectancy ", "Schooling", 
                                    la.dados_grafico1, "blue", 0.6, "white" , "Expectativa de Vida e Escolaridade", 
                                    "Expectativa de Vida (em anos)", "Escolaridade (em anos)")

grafico_4 = cp.grafico_de_dispercao("exp_de_vida_investimento_saude.html", "Life expectancy", "percentage expenditure", la.dados_grafico4, "red", 0.5, "white", "Expectativa de Vida e Investimento do PIB em Saúde (por país)", "Expectativa de Vida (em anos)", "Investimento no Setor Saúde (em % do PIB)")