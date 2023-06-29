import pandas as pd
from bokeh.plotting import ColumnDataSource

#lê o banco de dados csv
df = pd.read_csv("Life Expectancy Data.csv")

#seleciona as colunas de expectativa de vida e escolaridade do ano de 2015
expectativa_escolaridade = df[["Life expectancy ", "Schooling"]][df["Year"]==2015]

#transforma os dados de expectativa de vida e escolaridade em um objeto ColumnDataSource
dados_grafico1 = ColumnDataSource(data=expectativa_escolaridade)

#seleciona somente as linhas do Brasil e as colunas ano e expectativa de vida
dados_brasil = df[["Year","Life expectancy "]][df["Country"]=="Brazil"]

#transforma os dados em um objeto ColumnDataSource
dados_grafico2 = ColumnDataSource(data=dados_brasil)

#seleciona as colunas de morte antes dos 5 anos e vacinação contra a poliomelite
morte_infantil_poliomelite = df[["under-five deaths ", "Polio"]][df ["Year"] == 2015]

#transforma os dados de morte antes dos 5 anos e vacinação contra a poliomelite em um objeto ColumnDataSource
dados_grafico4 = ColumnDataSource(data=morte_infantil_poliomelite)



