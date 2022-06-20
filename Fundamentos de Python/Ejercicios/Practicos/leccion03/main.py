
# PARA RECOGER ESPECÍFICAMENTE DOS CADENAS

cad1 = input("Escriba un texto: ")
cad2 = input("Escriba un texto: ")
result = cad1 + " " + cad2


print(f"\nResultado: {result}")

print(f"Longitud: {len(result)}\n")

# PARA HACERLO MÁS GENÉRICO Y RECOGER X CADENAS

texto = ""

num = int(input("¿Cuántas cadenas quiere escribir? "))

for i in range(num):
    texto += input("Escriba un texto: ")
    if(i < num - 1):
        texto += " "

print(f"Resultado: {texto}")

print(f"Longitud: {len(texto)}")