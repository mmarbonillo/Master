#abrir fichero
fichero = open('ejemplo.txt','r')

#leer todo fichero
#print(fichero.read())

#leer determinado número de líneas
#print(fichero.readline())
#print(fichero.readline())

# caracter  = fichero.readline(1)

# while caracter != "":
#     print(caracter)
#     caracter = fichero.readline(1)

#leer el fichero por lineas
""" lineas = fichero.readlines()
#print(lineas)

for linea in lineas:
    print(linea)
    
#argumentos de open()
'''
Modos de apertura

r: opción por defecto, leer fichero
w: para escribir en el fichero, si existe el fichero lo borra
x: para crearlo, si existe dará un error
a: para añadir contenido a un fichero existente
b: abrir modo binario
'''

#cerrar fichero
fichero.close()

fichero = open('ejemplo.txt','r')
try:
    #usaremos el fichero
    pass
except:
    pass
finally:
    #siempre será ejecutado
    fichero.close()

with open('ejemplo.txt', 'r') as fichero:
    linea = fichero.readline()
    while linea != '':
        print(linea)
        linea = fichero.readline()

with open('ejemplo.txt','r') as fichero:
    for linea in fichero.readlines():
        print(linea) """
        

#escribir ficheros en python
#abrir un nuevo
fichero = open("nuevo.txt",'w')
#abrir un fichero y añadir contenido al final
fichero_ = open("nuevo_a.txt",'a')

#método write()
fichero.write("Hello world\n")
fichero.write("Hello world\n")
fichero.close()

fichero = open("nuevo.txt",'w')
lista=["ejem1","ejem2","ejem3"]

for elem in lista:
    fichero.write(elem+"\n")

fichero.close()

#método writelines
fichero = open("nuevo.txt",'w')
lista=["ejem1\n","ejem2\n","ejem3\n"]

fichero.writelines(lista)
fichero.close()

with open("nuevo.txt",'w') as fichero:
    fichero.writelines(lista)
    
#fichero = open('nuevo.txt','x')

import pandas as pd
import sqlite3

""" data = pd.read_csv('ejemplo.csv',sep=',')#,decimal=',',delimiter='.')
#print(data)
print(data.loc[data['name']=='James'])
print(data["name"])
con = sqlite3.connect('ex1.db')
data = pd.read_sql("select *  from tabla1",con)
 """
frame_data = {'name': ['James', 'Jason', 'Rogers'], 'age': [18, 20, 22], 'job':
['Assistant', 'Manager', 'Clerk']}

df = pd.DataFrame(frame_data)
df.to_csv('exe1.csv', index=False)