# Desarrolla un script que cargue el fichero cotizaciones.csv subido a la
# plataforma y cronstruya un dataframe en pandas. Muestra el mínimo,
# máximo y media de cada columna.

import pandas as pd

cotizacion = pd.read_csv('cotizacion.csv', sep = ';', decimal = ',')

def pasarFloat(elemento):
    contadorPuntos = 0
    contadorDecimales = 0
    for pos, valor in enumerate(elemento):
        if valor == '.': # COMPRUEBO SI EL CAMPO LLEVA PUNTOS
            contadorPuntos += 1 # CUENTO LA CANTIDAD DE PUNTOS
            contadorDecimales = len(elemento[pos:]) # MIRO CUANTOS DECIMALES TIENE
        
    if contadorPuntos > 1 : elemento = elemento.replace('.', '', contadorPuntos - 1) # QUITO TODOS LOS PUNTOS MENOS EL ÚLTIMO, QUE PODRÍA INDICAR DECIMALES
    if contadorDecimales > 3: elemento = elemento.replace('.', '') # SI EL ÚLTIMO PUNTO INDICA DECIMALES (SOLO 2 NÚMEROS TRAS EL PUNTO) LE PONGO PUNTO PARA RECONOCERLO
    elemento = elemento.replace(',', '.') # SI HAY ALGUNA COMA, LA CAMBIO POR PUNTO
    return float(elemento)

columna5 = cotizacion.iloc[:, 4] # RECOJO LA COLUMNA
columna5EnLista = columna5.tolist() # LA PASO A LISTA

# RECORRO LA LISTA PARA COMPROBAR CADA ELEMENTO
for i in range(0, len(columna5EnLista)):
    columna5EnLista[i] = pasarFloat(columna5EnLista[i])

# PASO LA LISTA A DATAFRAME
columna5 = pd.DataFrame(data = columna5EnLista)

# LE ASIGNO EL DATAFRAME A LA COLUMNA
cotizacion['Volumen'] = columna5


# print(cotizacion.dtypes)
print('--------------- DATAFRAME ---------------')
print('\n')
print(cotizacion)
#print(type(cotizacion))

# MÍNIMO DE LAS COLUMNAS USANDO APPLY
print('\n')
print('--------------- MÍNIMO ---------------\n')
print('COLUMNA  /  VALOR MÍNIMO\n')
print(cotizacion.apply(min, axis = 0))

# MÁXIMO DE LAS COLUMNAS CON LA FUNCIÓN MAX DE DATAFRAME
print('\n')
print('--------------- MÁXIMO ---------------\n')
print('COLUMNA  /  VALOR MÁXIMO\n')
print(cotizacion.max())

# MEDIA DE LAS COLUMNAS CON LAS FUNCIÓN MEAN DE DATAFRAME ESPECIFICANDO SOLO
# AQUELLAS QUE SEAN NÚMERICAS YA QUE NO PUEDE APLICAR LA MEDIA SOBRE LOS NOMBRES
print('\n')
print('--------------- MEDIA ---------------\n')
print('COLUMNA  /  VALOR MEDIO\n')
print(cotizacion.mean(numeric_only = True))
