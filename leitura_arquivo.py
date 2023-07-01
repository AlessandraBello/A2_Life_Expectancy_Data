import pandas as pd
from bokeh.plotting import ColumnDataSource
import numpy as np

#lê o banco de dados csv e transforma em DataFrame
df = pd.read_csv("Life Expectancy Data.csv")

#seleciona as colunas de expectativa de vida, escolaridade e continente do ano de 2015
selecao_ano = df[["Life expectancy ", "Schooling", "Continent"]][df["Year"]==2015]

#seleciona as colunas de expectativa de vida e escolaridade por cada continente
africa = selecao_ano[["Life expectancy ", "Schooling"]][selecao_ano["Continent"]=="Africa"]
america_sul = selecao_ano[["Life expectancy ", "Schooling"]][selecao_ano["Continent"]=="South America"]
america_norte = selecao_ano[["Life expectancy ", "Schooling"]][selecao_ano["Continent"]=="North America"]
asia = selecao_ano[["Life expectancy ", "Schooling"]][selecao_ano["Continent"]=="Asia"]
europa = selecao_ano[["Life expectancy ", "Schooling"]][selecao_ano["Continent"]=="Europe"]
oceania = selecao_ano[["Life expectancy ", "Schooling"]][selecao_ano["Continent"]=="Oceania"]

#transforma os dados de expectativa de vida e escolaridade em um objeto ColumnDataSource, separado por continente
dados_grafico1_1 = ColumnDataSource(data=africa)
dados_grafico1_2 = ColumnDataSource(data=america_sul)
dados_grafico1_3 = ColumnDataSource(data=america_norte)
dados_grafico1_4 = ColumnDataSource(data=asia)
dados_grafico1_5 = ColumnDataSource(data=europa)
dados_grafico1_6 = ColumnDataSource(data=oceania)

#seleciona somente as linhas do Brasil e as colunas ano e expectativa de vida
dados_brasil = df[["Year","Life expectancy "]][df["Country"]=="Brazil"]

#transforma os dados em um objeto ColumnDataSource
dados_grafico2 = ColumnDataSource(data=dados_brasil)

#Selecionando os dados de poliomielite, difteria e hepatite B do ano 2000 e exclui os NA, se houverem
polio_2000 = df[["Polio"]][df["Year"]==2000].dropna()
hepatiteb_2000 = df[["Hepatitis B"]][df["Year"]==2000].dropna()
difteria_2000 = df[["Diphtheria "]][df["Year"]==2000].dropna()

#faz a media de vacinacao das doenças, em 2000
media_vacinacao_polio_2000 = np.mean(list(polio_2000["Polio"]))
media_vacinacao_hepatiteb_2000 = np.mean(list(hepatiteb_2000["Hepatitis B"]))
media_vacinacao_difteria_2000 = np.mean(list(difteria_2000["Diphtheria "]))

#Selecionando os dados de poliomielite, difteria e hepatite B do ano 2015 e exclui os NA, se houverem
polio_2015 = df[["Polio"]][df["Year"]==2015].dropna()
hepatiteb_2015 = df[["Hepatitis B"]][df["Year"]==2015].dropna()
difteria_2015 = df[["Diphtheria "]][df["Year"]==2015].dropna()

#faz a media de vacinaçao das doenças, em 2015
media_vacinacao_polio_2015 = np.mean(list(polio_2015["Polio"]))
media_vacinacao_hepatiteb_2015 = np.mean(list(hepatiteb_2015["Hepatitis B"]))
media_vacinacao_difteria_2015 = np.mean(list(difteria_2015["Diphtheria "]))

#cria um dicionario com as doenças e as medias de cada ano
doencas_e_medias_por_ano = {"doenca": ["Poliomielite", "Hepatite B", "Difteria"],
                            "2000": [media_vacinacao_polio_2000, media_vacinacao_hepatiteb_2000, media_vacinacao_difteria_2000],
                            "2015": [media_vacinacao_polio_2015, media_vacinacao_hepatiteb_2015, media_vacinacao_difteria_2015]}

#converte os dados em um objeto ColumnDataSource
dados_grafico3 = ColumnDataSource(data=doencas_e_medias_por_ano)

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

#seleciona as colunas de paises e alcool do continente europeu
anos_alcool_europa = df[(df["Continent"] == "Europe") & (df["Year"] == 2007)][["Country", "Alcohol"]]

#transforma os dados de países e alcoolismo europeu em um objeto ColumnDataSource
dados_grafico53 = ColumnDataSource(data = anos_alcool_europa)

#seleciona as colunas de taxa de mortalidade e idh de 2015
mortalidade_idh = df[["Adult Mortality","Income composition of resources", "Country"]][df["Year"] == 2015]

#transforma os dados de taxa de mortalidade e idh em um objeto ColumnDataSource
dados_grafico6 = ColumnDataSource(data = mortalidade_idh)
