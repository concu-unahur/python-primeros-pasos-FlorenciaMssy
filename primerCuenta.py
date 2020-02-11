import threading
from operaConm import sumar
from operaNoConm import dividirPor

contador = 1
#lock = threading.Lock()

threadDividir = threading.Thread(target=dividirPor, args=[2])
threadSumar = threading.Thread(target=sumar, args=[3])

threadDividir.start()

threadSumar.start()

print(f"El resultado es {contador}")






