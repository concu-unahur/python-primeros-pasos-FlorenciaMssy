import threading
from operaNoConm import dividirPor
from operaConm import sumar

contador = 3
lock = threading.Lock

t1 = threading.Thread(target=dividirPor, args=[2])
t2 = threading.Thread(target=sumar, args=[1])

t1.start()
t2.start()

print(f"El resultado es {contador}")