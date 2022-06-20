from functools import reduce
#elimina repetidos
lista = [2, 3, 9, 4, 2, 4, 5, 6, 7, 7, 9]

# i = len(lista) - 1

# while i > 0:
#     for x in range(i - 1, - 1, -1):
#         try:
#             if lista[i] == lista[x]:
#                 lista.pop(i)
#         except:
#             pass
#     i -= 1

#RECORREMOS LA LISTA AL REVÉS PARA QUE SIEMPRE ELIMINE EL QUE SE ENCUENTRE EN ÚLTIMO LUGAR EN LA LISTA
for i in range(len(lista) - 1, 0, -1):
    for x in range(i - 1, -1, -1):
        try: # COMO SE QUE EN LA PRIMERA VUELTA ME VA A DAR UN ERROR INDEX OUT OF RANGE PORQUE VA A ELIMINAR LA POSICIÓN 10 (VALOR DE I) PERO X SIGUE ITERANDO
             # PONGO UN TRY PARA CAPTURAR DICHA EXCEPCIÓN Y QUE SIGA EJECUTANDO. ¿PUEDO HACER BREAK DEL FOR DESDE DENTRO DEL IF?
            if lista[i] == lista[x]:
                lista.pop(i)
        except:
            pass

# HACIA ALANTE
# for i in range(len(lista) -1):
#     for x in range(i + 1, len(lista)):
#         try:
#             if lista[i] == lista[x]:
#                 lista.pop(x)
#         except:
#             pass

#print(lista)


#comprobar que existe la clave
# dicc = {"a": 1, "b": 2, "c":4}

# clave = input("Intruduzca una clave: ")
# existe = False

# for i in dicc.keys():
#     if i == clave:
#         existe = True

# if existe:
#     print(f"La clave {clave} sí existe")
# else:
#     print(f"La clave {clave} no existe")

d= {"a":1,"b":2,"c":3}
listaClaves = list(d.keys())
clave = input("Introduzca la clave que desea buscar: ")

if listaClaves.count(clave) > 0:
    print(f"La palabra '{clave}' ES una clave dentro del diccionario")
else:
    print(f"La palabra '{clave}' NO ES una clave dentro del diccionario")