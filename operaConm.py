import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

contador = 0
lock = threading.Lock()
def sumar(numero):
    global contador
    global lock
    #time.sleep(1)
    try:
        lock.acquire()
        contador += numero
        logging.info(contador)
    finally:
        lock.release()

def multiplicarPor(numero):
    global contador
    global lock
    #time.sleep(1)
    try:
        lock.acquire()
        contador *= numero
        logging.info(contador)
    finally:
        lock.release()

threadParaSumar = threading.Thread(target=sumar, args=[1])
threadParaMultiplicar = threading.Thread(target=multiplicarPor, args = [2])

threadParaSumar.start()

threadParaMultiplicar.start()

print(f"El resultado es: {contador}")