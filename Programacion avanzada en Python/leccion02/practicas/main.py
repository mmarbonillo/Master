# Escribe una función que acepte dos variables numéricas y calcule la suma y
# la resta de dichas cifras. La función devolverá tanto la suma como la resta.
# Utiliza las excepciones para controlar algún posible error dentro de la
# función.
# Crea una función en la cual el segundo parámetro sea un argumento
# predeterminado. Ejemplo de llamada:
# Mifuncion(20,30)
# Mifuncion(20)

# La función en la que el segundo parámetro es predeterminado, es la propia función que suma y resta los dos números

# FUNCIÓN QUE RECOGE DOS NÚMEROS
def recogerNums():
    x = 0
    y = 0
    caracterNum = False
    
    # CONTROL DEL TIPO DE DATO INTRODUCIDO REDONDEANDO A DOS CARÁCTERES
    while not caracterNum:
        try:
            x = round(float(input("Introduce un número: ")), 2)
            caracterNum = True
        except ValueError:
            print("Has introducido un caracter no numérico, vuelve a probar")

    caracterNum = False

    # CONTROL DEL TIPO DE DATO INTRODUCIDO REDONDEANDO A DOS CARÁCTERES
    while not caracterNum:
        try:
            y = round(float(input("Introduce un segundo número: ")), 2)
            caracterNum = True
        except ValueError:
            print("Has introducido un caracter no numérico, vuelve a probar")
    # RETURN DE LA FUNCIÓN QUE DEVUELVE UNA LISTA
    return [x, y]

# FUNCIÓN QUE RECOGE UN NÚMERO
def recogerNum():
    x = 0
    caracterNum = False
    
    # CONTROL DEL TIPO DE DATO INTRODUCIDO REDONDEANDO A DOS CARÁCTERES
    while not caracterNum:
        try:
            x = round(float(input("Introduce un número: ")), 2)
            caracterNum = True
        except ValueError:
            print("Has introducido un caracter no numérico, vuelve a probar")
    return x

# FUNCIÓN PARA SUMAR Y RESTAR EN LA QUE EL SEGUNDO PARÁMETRO NO ES OBLIGATORIO, PUEDE SER PREDEFINIDO O NO, DEPENDE DE LOS ARGUMENTOS QUE LE PASEMOS
def sumaResta(n1, n2 = None):
    # DICCIONARIO PARA ALMACENAR LOS RESULTADOS
    result = {}
    # COMPROBAR SI SE LE HAN PASADO UNO O DOS ARGUMENTOS A LA FUNCIÓN
    if not n2:
        # SI SE LE HA PASADO SOLO UN ARGUMENTO, SE PREDEFINE EL VALOR DE n2 (y)
        y = 20.35
        result["suma"] = round(n1 + y, 2)
        result["resta"] = round(n1 - y, 2)
        result["y"] = y
    else:
        result["suma"] = round(n1 + n2, 2)
        result["resta"] = round(n1 - n2, 2)
    return result

# VARIABLE PARA CONTROLAR CUÁNTOS ARGUMENTOS SE LE PASARÁN A LA FUNCIÓN sumaResta()
numCaract = 0

# CONTROL DE QUE EL USUARIO ELIJA PASARLE UNO O DOS PARÁMETROS
while numCaract != 1 and numCaract != 2:
    # COMPROBAR QUE EL USUARIO INTRODUCE UN NÚMERO ENTERO Y QUE ESTE NÚMERO SEA 1 O 2
    try:
        numCaract = int(input("¿Cuántos números quieres introducir? (1/2): "))
    except ValueError:
        print("Lo siento, las únicas opciones son 1 o 2")

# SENTENCIA MATCH PARA VER SI HAY QUE PEDIR UNO O DOS NÚMEROS Y LLAMAR CORRECTAMENTE A LA FUNCIÓN sumaResta()
match numCaract:
    case 1:
        num = recogerNum()
        result = sumaResta(num)
        print(f"La suma de {num} + {result['y']} es: {result['suma']}")
        print(f"La resta de {num} + {result['y']} es: {result['resta']}")
    case 2:
        nums = recogerNums()
        result = sumaResta(nums[0], nums[1])
        print(f"La suma de {nums[0]} + {nums[1]} es: {result['suma']}")
        print(f"La resta de {nums[0]} - {nums[1]} es: {result['resta']}")
    case _:
        pass
        


