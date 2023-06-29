import pandas as pd
from bokeh.plotting import ColumnDataSource
import numpy as np

#lê o banco de dados csv e transforma em DataFrame
df = pd.read_csv("Life Expectancy Data.csv")

#seleciona as colunas de expectativa de vida e escolaridade do ano de 2015
expectativa_escolaridade = df[["Life expectancy ", "Schooling"]][df["Year"]==2015]

#transforma os dados de expectativa de vida e escolaridade em um objeto ColumnDataSource
dados_grafico1 = ColumnDataSource(data=expectativa_escolaridade)

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

#tupla com os anos utilizados
anos = ["2000", "2015"]

#cria uma tupla de listas com as doencas e os anos, por exemplo, [("Poliomielite", "2000"), ("Poliomielite", "2015"), ...]
doenca_ano=[(doenca, ano) for doenca in doencas_e_medias_por_ano["doenca"] for ano in anos]

#cria uma lista com as medias dos anos 2000 e 2015
contagem_medias = sum(zip(doencas_e_medias_por_ano["2000"], doencas_e_medias_por_ano["2015"]), ())

print (contagem_medias)
#converte os dados em um objeto ColumnDataSource
dados_grafico3 = ColumnDataSource(data=dict(eixo_x=doenca_ano, medias=contagem_medias))

#seleciona as colunas de morte antes dos 5 anos e vacinação contra a poliomelite
morte_infantil_poliomelite = df[["under-five deaths ", "Polio"]][df ["Year"] == 2015]

#transforma os dados de morte antes dos 5 anos e vacinação contra a poliomelite em um objeto ColumnDataSource
dados_grafico4 = ColumnDataSource(data=morte_infantil_poliomelite)



