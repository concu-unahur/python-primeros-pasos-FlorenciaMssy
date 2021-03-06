import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

contador = 5
lock = threading.Lock()
def dividirPor(numero):
    global contador
    global lock
    #time.sleep(1)
    try:
        lock.acquire()
        contador /= numero
        logging.info(contador)
    finally:
        lock.release()

def restar(numero):
    global contador
    global lock
    #time.sleep(1)
    try:
        lock.acquire()
        contador -= numero
        logging.info(contador)
    finally:
        lock.release()