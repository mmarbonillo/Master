
import _thread

def print_num(thread, num):
    print("entra")
    for i in range(1, num + 1):
        print("Thread", thread, ":", i)

try:
    _thread.start_new_thread(print_num, (1,5))
    print("Prueba")
    _thread.start_new_thread(print_num, (2,5))
except Exception as e:
    print(e)