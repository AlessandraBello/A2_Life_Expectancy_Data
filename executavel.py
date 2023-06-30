import manuela_plots as mp
import leitura_arquivo as la
import layout
import textos
from bokeh.models import FactorRange

# Chama a função do gráfico 7
grafico_7 = mp.grafico7()

# Chama a função do gráfico 8
grafico_8 = mp.grafico8()

# Chama a função do gráfico 9
grafico_9 = mp.grafico9()

# Cria um html com os gráficos e seus respectivos textos
graficos_manuela = layout.agrupar("Manuela.html", grafico_7, textos.texto_grafico_7, grafico_8, None, grafico_9, None)