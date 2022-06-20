
class Calculadora:
    
    def __init__(self, n1, n2):
        if (type(n1) != int or type(n1) != float) and (type(n2) != float or type(n2) != float):
            print("Ambos argumentos han de ser numéricos")
        else:
            self.n1 = n1
            self.n2 = n2
    
    def sumar(self):
        return self.n1 + self.n2
    
    def multiplicar(self):
        return self.n1 * self.n2
    
    def restar(self):
        return self.n1 - self.n2
    
    def dividir(self):
        return self.n1 / self.n2


print("Introduce dos valores numéricos: ")

v1 = 0
v2 = 0

caracterNum = False

while not caracterNum:
    try:
        v1 = round(float(input("1: ")), 2)
        caracterNum = True
    except ValueError:
        print("Introduce un carácter numérico")

caracterNum = False

while not caracterNum:
    try:
        v2 = round(float(input("2: ")), 2)
        caracterNum = True
    except ValueError:
        print("Introduce un carácter numérico")

calc = Calculadora(v1, v2)

print(f"La suma de {v1} + {v2} es: {calc.sumar()}")
print(f"La multiplicación de {v1} * {v2} es: {calc.multiplicar()}")
print(f"La resta de {v1} - {v2} es: {calc.restar()}")
print(f"La división de {v1} / {v2} es: {calc.dividir()}")

