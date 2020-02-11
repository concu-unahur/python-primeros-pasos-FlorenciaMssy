import threading
import time
import logging
import clasesYfunciones
from definiciones import UnThread
from tiempo import Contador

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

# la función para usar para el thread
def dormir(tiempo):
    time.sleep(tiempo)

contador = Contador()

contador.iniciar()

listita = []

for i in range(10):
    i = threading.Thread(target=dormir, args=[1,5])
    i.start()
    listita.append(i)

for thread in listita:
    thread.join()


contador.finalizar()
contador.imprimir()