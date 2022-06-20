
from msilib.schema import Class


class Animal:
    
    tipo = ""
    
    def __init__(self, nombre, tipo = None):
        self.nombre = nombre
        if tipo is not None: self.tipo = tipo

a1 = Animal("Tina", "gato")
a2 = Animal("Lomo")

print(a1.nombre)
print(a1.tipo)
print(a2.nombre)
print(a2.tipo)
print(Animal.tipo)