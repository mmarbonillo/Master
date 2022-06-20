""" from concurrent.futures import thread
from time import sleep, perf_counter

def task():
    #print("Entrando a la función")
    sleep(1)
    #print("Done")


start_time = perf_counter()
task()
task()
end_time = perf_counter()

print(f"Tiempo total serie {end_time-start_time: 0.2f} segundos")


from threading import Thread


start_time = perf_counter()

#inicializar hilo
new_thread_1 = Thread(target=task)
new_thread_2 = Thread(target=task)
new_thread_3 = Thread(target=task)
new_thread_4 = Thread(target=task)

#lanzar hilo
new_thread_1.start()
new_thread_2.start()
new_thread_3.start()
new_thread_4.start()

#esperar/bloquear hilo
new_thread_1.join()
new_thread_2.join()
new_thread_3.join()
new_thread_4.join()

end_time = perf_counter()

print(f"Tiempo total concurrente {end_time-start_time: 0.2f} segundos")

import threading

start_time = perf_counter()


def task_args(id):
    print(f"Entrando la hebra {id}")
    print(threading.current_thread().getName())
    sleep(1)
    
threads = []
for n in range(1,11):
    #inicializamos
    t = Thread(target=task_args,args=(n,),name='th_'+str(n))
    threads.append(t)
    #lanzamos
    t.start()


for t in threads:
    t.join()


end_time = perf_counter()

print(f"Tiempo total concurrente con args {end_time-start_time: 0.2f} segundos")
 """

import logging

logging.basicConfig(format="%(asctime)s %(message)s",datefmt='%m/%d/%Y %H:%M:%S',filename='ejemplo.log',filemode='w',level=logging.DEBUG)

logging.warning("Hola soy un warning")
logging.info("Hola soy un info")
logging.error("Hola soy un error")
logging.debug("Hola soy un debug")