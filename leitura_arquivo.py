import pandas as pd
from bokeh.plotting import ColumnDataSource

#lê o banco de dados csv
df = pd.read_csv("Life Expectancy Data.csv")

#seleciona as colunas de expectativa de vida e escolaridade
expectativa_escolaridade = df[["Life expectancy ", "Schooling"]]

#transforma os dados de expectativa de vida e escolaridade em um objeto ColumnDataSource
dados_grafico1 = ColumnDataSource(data=expectativa_escolaridade)

#seleciona as colunas de anos e magreza extrema de 5-9 anos e tira a media de acordo com o continente
anos_magreza59_continente = df.groupby(["Year", "Continent"])[" thinness 5-9 years"].mean().reset_index()

#transforma os dados de anos e magreza extrema de 5-9 anos em um objeto ColumnDataSource
dados_grafico4 = ColumnDataSource(data=anos_magreza59_continente)



