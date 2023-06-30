import pandas as pd
from bokeh.plotting import ColumnDataSource
import numpy as np

#lê o banco de dados csv e transforma em DataFrame
df = pd.read_csv("Life Expectancy Data.csv")

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



