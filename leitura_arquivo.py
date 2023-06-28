import pandas as pd
from bokeh.plotting import ColumnDataSource

#lê o banco de dados csv
df = pd.read_csv("Life Expectancy Data.csv")

#seleciona as colunas de expectativa de vida e escolaridade
expectativa_escolaridade = df[["Life expectancy ", "Schooling"]]

#transforma os dados de expectativa de vida e escolaridade em um objeto ColumnDataSource
dados_grafico1 = ColumnDataSource(data=expectativa_escolaridade)

#seleciona as colunas de expectativa de vida e investimento em saúde
expectativa_investimento = df[["Life expectancy","percentage expenditure"]]

#transforma os dados de expectativa de vida e investimento em saude em um objeto ColumnDataSource
dados_grafico4 = ColumnDataSource(data=expectativa_investimento)



