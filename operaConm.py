import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

contador = 2
lock = threading.Lock()
lock2 = threading.Lock()
def sumarUno():
    global contador
    global lock
    #time.sleep(1)

    try:    
    #lock2.acquire()
        contador += 1
        logging.info(contador)
    finally:
        lock.release()
   

def multiplicarPorDos():
    global contador
    global lock
    #time.sleep(1)
    lock.acquire()
    try:   
        contador *= 2
        logging.info(contador)
    finally:
        lock.release()
        #lock2.release()


threadParaMultiplicar = threading.Thread(target=multiplicarPorDos)
threadParaSumar = threading.Thread(target=sumarUno)

lock.acquire()

threadParaMultiplicar.start()
threadParaSumar.start()
threadParaMultiplicar.join()


print(f"El resultado es: {contador}")