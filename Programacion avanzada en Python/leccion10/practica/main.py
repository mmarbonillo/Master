# Crea un dataframe mediante el fichero CSV ‘data.csv’ adjunto a esta práctica.
# Haz un resumen de los datos que has cargado en el dataframe. Limpia los
# datos en el caso de que hayas valores vacíos y finalmente grafica los datos
# con cualquier tipo de plot.

import pandas as pd
import matplotlib.pyplot as plt

# Leo el archivo CSV
data = pd.read_csv('data.csv', sep = ',', decimal = '.')

# Resumen de los datos
print(data.describe())

# Configuración pandas para que muestre el Dataframe entero al hacerle print
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 200) 
pd.set_option('display.width', 200) 

# Relleno a 0 los vacíos y ordeno el dataframe por el campo que usaré en la X
data = data.fillna(0)
data = data.sort_values("Duration")

# Le damos un tamaño a nuestra gráfica y le decimos que se ajuste al total de la ventana
plt.rcParams["figure.figsize"] = [15, 5]
plt.rcParams["figure.autolayout"] = True

# Marcamos los rangos de la X y la Y para poder elegir de cuanto es el salto entre valores
maxDuracion = data["Duration"].max()
rangox = range(0, maxDuracion + 1, 15)
plt.xticks(rangox)

maxCalorias = data["Calories"].max()
rangoy = range(0, int(maxCalorias) + 100, 100)
plt.yticks(rangoy)

# Recogemos el AXIS para que todas las líneas se escriban sobre la misma gráfica
ax = plt.gca()

# Le asignamos al Dataframe sobre el mismo AXIS una X (que será siempre la misma) y tantas líneas Y como tengamos o queramos
data.plot(kind = 'line', x = 'Duration', y = 'Pulse', ax = ax)
data.plot(kind = 'line', x = 'Duration', y = 'Maxpulse',  color = 'red', ax = ax)
data.plot(kind = 'line', x = 'Duration', y = 'Calories',  color = 'green', ax = ax)

# Guardamos la gráfica en un archivo de imagen
plt.savefig('grafica.png')

# Mostramos la gráfica
plt.show()