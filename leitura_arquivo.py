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

#seleciona as colunas de anos e alcoolismo no brasil
alcoolismo_brasil = df[["Year","Alcohol"]][df["Country"]=="Brazil"][df["Year"] != 2015]

#transforma os dados de anos e alcoolismo no brasil  em um objeto ColumnDataSource
dados_grafico5 = ColumnDataSource(data = alcoolismo_brasil)

#seleciona as colunas de anos e alcool e tira a media de acordo com o continente
anos_alcool_continente = df[df["Year"] != 2015].groupby(["Year", "Continent"])["Alcohol"].mean().reset_index()

#transforma os dados de anos e alcoolismo por continente  em um objeto ColumnDataSource
dados_grafico52 = ColumnDataSource(data = anos_alcool_continente)

#seleciona as colunas de anos e alcool do continente europeu
anos_alcool_europa = df[["Year","Alcohol"]][df["Continent"]=="Europe"]

#transforma os dados de anos e alcoolismo europeu em um objeto ColumnDataSource
dados_grafico53 = ColumnDataSource(data = anos_alcool_europa)


