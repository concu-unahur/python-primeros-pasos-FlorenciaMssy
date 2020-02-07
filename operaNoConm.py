import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

cantidad = 5
lock = threading.Lock()

def sumarUno():
    global cantidad
    global lock

    try:
        lock.acquire()
        cantidad +=1
    finally:
        lock.release()

def multiplicarPorDos():
    global cantidad
    global lock

    try:
        lock.acquire()
        cantidad *=2
    finally:
        lock.release()


t1 = threading.Thread(target=sumarUno)
t2 = threading.Thread(target=multiplicarPorDos)

t1.start
t2.start

print(f"cantidad vale {cantidad}")


