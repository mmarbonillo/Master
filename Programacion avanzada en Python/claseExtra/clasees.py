
# Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. 
# Construye los siguientes métodos para la clase:

# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# mostrar(): Muestra los datos de la persona.
# esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona:
    
    def __init__(self, nombre:str = 'No se ha proporcionado nombre para esta persona', edad:int = 0, dni:str = 'No se ha proporcionado DNI para esta persona'):
        assert isinstance(nombre, str), "El nombre debe ser un texto"
        assert isinstance(edad, int), "La edad debe ser un número"
        assert isinstance(dni, str), "El DNI debe ser un texto"
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
    # p1 = Persona("Lucía", 30, '56985214C')
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad
    
    @property
    def dni(self):
        return self.__dni
    
    @nombre.setter
    def nombre(self, n):
        assert isinstance(n, str), "El nombre debe ser un texto"
        self.__nombre = n
        return self.__nombre
    
    @edad.setter
    def edad(self, e:int):
        assert isinstance(e, int), "La edad debe ser un número"
        self.__edad = e
        return self.__edad
    
    @dni.setter
    def dni(self, d:str):
        assert isinstance(d, str), "El DNI debe ser un texto"
        self.__dni = d
        return self.__dni
    
    def mostrar(self):
        texto = ''
        if self.__edad == 0: texto = f"Nombre: {self.__nombre}\nEdad: No se ha proporcionado edad para esta persona\nDNI: {self.__dni}"
        else: texto = f"Nombre: {self.__nombre}\nEdad: {self.__edad}\nDNI: {self.__dni}"
        print(texto)
    
    def esMayorDeEdad(self):
        mayor = False
        if self.__edad == 0: print("No se ha dado el dato de la edad de la persona")
        elif self.__edad >= 18: mayor = True
        return mayor
    
    
    
    # def __str__(self):
    #     return (f"Soy {self.__nombre}, tengo {self.__edad} y ni DNI es {self.__dni}")
    

p1 = Persona('Lucía', 30, '56985214C')
p1.mostrar()
p2 = Persona()
p2.mostrar()