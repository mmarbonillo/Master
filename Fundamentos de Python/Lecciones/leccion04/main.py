
# Con la palabra reservada PASS podemos dejar una sentencia vacía

a = 1
b = 2

if a == 2:
    pass

if a < b:
    pass
elif a > b:
    pass

# Recorrer una lista al revés

lista = [1, 2, 3, 4]

for i in reversed(lista):
    #print(i)
    pass

#for i in lista.index(2):
    #print(i)
#    pass


#Ejercicio: tabla de multiplicar
# Preguntar dos números; uno para cuantas tablas de multiplicar quiere y otro que indique desde cual se empieza
# Hacer un for anidado para sacar esas tablas de multiplicar
# #

cant = int(input("Indica cuantas tablas quieres: "))
inicio = int(input("¿Desde cual quieres empezar?: "))


for i in range(inicio, inicio + cant + 1):
    print(f"Tabla del {i}:")
    for x in range(1, 11):
        print(f"{i} x {x} = {i * x}")
    print("\n")