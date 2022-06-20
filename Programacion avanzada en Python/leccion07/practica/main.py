# Crea un script el cual mediante la librería ‘threading’ 
# o ‘_thread’ permita ejecutar una funcion simple (por ejemplo una función con un print) 
# con diferentes hebras.

from threading import Thread
from time import sleep, perf_counter

def funcionPrint():
    print("Empieza la función")
    sleep(2)
    print("Termina la función")

# Inicializamos el contador de tiempo
start_time = perf_counter()

# funcionPrint()
# funcionPrint()
# funcionPrint()

hilo1 =Thread(target = funcionPrint)
hilo2 =Thread(target = funcionPrint)
hilo3 =Thread(target = funcionPrint)

hilo1.start()
hilo2.start()
hilo3.start()

hilo1.join()
hilo2.join()
hilo3.join()

end_time = perf_counter()
print(f"Tiempo total serie {end_time-start_time: 0.2f} segundos")
