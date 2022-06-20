# Crea un dataframe mediante el fichero CSV ‘data.csv’ adjunto a esta práctica.
# Haz un resumen de los datos que has cargado en el dataframe. Limpia los
# datos en el caso de que hayas valores vacíos y finalmente grafica los datos
# con cualquier tipo de plot.

import pandas as pd
import matplotlib.pyplot as mp

pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 200) 
pd.set_option('display.width', 200) 
# pd.set_option('precision', 3)

data = pd.read_csv('data.csv', sep = ',', decimal = '.')

data = data.fillna(0)

ax = mp.gca()

# data.plot(kind='line',x='Duration',y='Maxpulse',ax=ax)
data.plot(kind = 'line', x = 'Calories', y = 'Maxpulse', color = 'red', ax = ax, )


# data.plot(kind = 'hist', bins=[0,20,40,60,80,100], rwidth=0.8)
# mp.savefig('output.png')

mp.show()

# print(data)

# mp.show()

# print(data.describe())