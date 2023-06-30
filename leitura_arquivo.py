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

#cria uma lista com as medias de vacinaçao dos anos 2000 e 2015
contagem_medias = sum(zip(doencas_e_medias_por_ano["2000"], doencas_e_medias_por_ano["2015"]), ())

#converte os dados em um objeto ColumnDataSource
dados_grafico3 = ColumnDataSource(data=dict(eixo_x=doenca_ano, medias=contagem_medias))

#seleciona as colunas de morte antes dos 5 anos e vacinação contra a poliomelite
morte_infantil_poliomelite = df[["under-five deaths ", "Polio"]][df ["Year"] == 2015]

#transforma os dados de morte antes dos 5 anos e vacinação contra a poliomelite em um objeto ColumnDataSource
dados_grafico4 = ColumnDataSource(data=morte_infantil_poliomelite)

#faz uma média da expectativa de vida por ano de cada continente
media_expectativa_por_continente = df.groupby(['Year', 'Continent'])['Life expectancy '].mean().reset_index()

#transforma os dados de expectativa de vida média por continente e ano em um objeto COlumnDataSource
dados_grafico7 = ColumnDataSource(media_expectativa_por_continente)

#filtra os países da América do Sul
america_do_sul = ["South America"]
df_america_do_sul = df[df["Continent"].isin(america_do_sul)]

#cria uma lista com os países da América do Sul
paises_america_sul = df_america_do_sul["Country"].unique().tolist()

#substitui os nomes da Bolivia e Venezuela para simplificar o gráfico
paises_america_sul = [pais.replace("Bolivia (Plurinational State of)", "Bolivia") for pais in paises_america_sul]
paises_america_sul = [pais.replace("Venezuela (Bolivarian Republic of)", "Venezuela") for pais in paises_america_sul]

#cria uma lista com os anos analisados e converte os expectativa_vida para strings
anos = list(range(2000, 2016))
anos_str = [str(ano) for ano in anos]

#cria uma lista vazia para armazenar os expectativa_vida de expectativa de vida
lista_america_sul = []

#cria uma lista com a expectativa de vida para cada país da América do Sul por ano
for ano in anos_str:
    expectativa_vida = df_america_do_sul[df_america_do_sul["Year"] == int(ano)]["Life expectancy "].values
    lista_america_sul.append(expectativa_vida.tolist())

#cria um dataframe para os valores do gráfico 
dados_heatmap = pd.DataFrame(lista_america_sul, columns = paises_america_sul, index = anos_str)

#cria um ColumnDaraSource ideal para fazer o heatmap
dados_grafico8 = ColumnDataSource(dados_heatmap.stack().reset_index().rename(columns={0: "valor"}))

#remove as linhas com valores de escolaridade e composição de renda iguais a 0 e valores faltantes de continente
dados_filtrados = df[(df['Schooling'] != 0) & (df['Income composition of resources'] != 0) & df['Continent'].notna()]

#filtra os dados para o ano de 2015
dados_filtrados_2015 = df[df['Year'] == 2015]

#cria um COlumnDataSource com os dados filtrados
dados_grafico9 = ColumnDataSource(dados_filtrados_2015)  



