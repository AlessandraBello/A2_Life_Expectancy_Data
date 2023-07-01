import giovanna_plots as gp
import leitura_arquivo_giovanna as la
import grid_giovanna as gg
import textos_giovanna
import layout_g

#chama o gráfico 4
grafico4 = gp.grafico_4()

#chama o grid/gráfico 5
grafico5 = gg.grid_giovanna()

#chama o gráfico 6
grafico6 = gp.grafico_6()

#criando o html com os gráficos e os textos
graficos_giovanna = layout_g.agrupar("Giovanna.html", grafico4, textos_giovanna.texto_grafico_4, grafico5, textos_giovanna.texto_grafico_5, grafico6, textos_giovanna.texto_grafico_6)






