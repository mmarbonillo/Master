# Crea un dataframe mediante el fichero CSV ‘data.csv’ adjunto a esta práctica.
# Haz un resumen de los datos que has cargado en el dataframe. Limpia los
# datos en el caso de que hayas valores vacíos y finalmente grafica los datos
# con cualquier tipo de plot.

import pandas as pd
import matplotlib.pyplot as plt

# Configuración pandas para que muestre el Dataframe entero
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 200) 
pd.set_option('display.width', 200) 

data = pd.read_csv('data.csv', sep = ',', decimal = '.')

data = data.fillna(0)
data = data.sort_values("Duration")

plt.rcParams["figure.figsize"] = [15, 5]
plt.rcParams["figure.autolayout"] = True

ax = plt.gca()

data.plot(kind='line',x='Duration',y='Pulse',ax=ax)
data.plot(kind='line',x='Duration',y='Maxpulse', color='red', ax=ax)
data.plot(kind='line',x='Duration',y='Calories', color='green', ax=ax)

plt.show()