
# Utiliza una lista para almacenar los números del 1 al 10 la cual debe ser rellenada con el uso de un bucle while. 
# Finalmente muestra la lista en orden inverso.

lista = []
i = 1

while i <= 10:
    lista.append(i)
    i += 1

print(list(reversed(lista)))


# Diccionarios:

#  1.Crea un diccionario con 4 valores.

dicc = {
    "c1": 1,
    "c2": 2,
    "c3": 3,
    "c4": 4,
}

#  2.Muestra los valores del diccionario.

for c in dicc.keys():
    print(dicc.get(c))
    #print(dicc[c])

#  3.Modifica el 3º valor del diccionario

dicc.update({"c3": True})

# También funciona:
# dicc["c3"] = "cambiado"

# Si no conociesemos la clave:
# keys = list(dicc.keys())
# dicc[keys[2]] = False

#  4.Añade un nuevo valor al diccionario de tipo lista

dicc["c5"] = ["esto", "es", "una", "lista"]

#  5.Muestra nuevamente los valores

print(dicc)