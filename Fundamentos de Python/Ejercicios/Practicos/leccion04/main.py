
# Escribe un programa que pida un número por pantalla. A continuación, mediante un bucle se mostrarán 
# por pantalla todos los números enteros desde el 0 hasta el número introducido por pantalla.

num = int(input("Introduzca un número: "))
nums = ""

for i in range(num + 1):
    nums += str(i) + " "

print(f"\n{nums}\n")


#Crea un diccionario con unos valores cualquiera y muestra únicamente mediante un bucle for los valores de este.

arr = [1, 2, 3, "cuatro", False, 1.253]

dicc = {"clave1": "hola", "clave2": 15, "otraClave": True, "otraClave2": arr}

for c, v in dicc.items():
    print(c)
