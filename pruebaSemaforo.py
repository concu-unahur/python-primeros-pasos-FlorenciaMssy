import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

contador = 2
semaforo = threading.Semaphore(1)
def sumarUno():
    global contador
    global semaforo
    #time.sleep(1)

    try:    
        contador += 1
        logging.info(contador)
    finally:
        semaforo.release()
   

def multiplicarPorDos():
    global contador
    global semaforo
    #time.sleep(1)
    semaforo.acquire()
    try:   
        contador *= 2
        logging.info(contador)
    finally:
        semaforo.release()
        #lock2.release()


threadParaMultiplicar = threading.Thread(target=multiplicarPorDos)
threadParaSumar = threading.Thread(target=sumarUno)

semaforo.acquire()

threadParaMultiplicar.start()
threadParaSumar.start()
threadParaMultiplicar.join()


print(f"El resultado es: {contador}")