from time import sleep
from threading import Thread

class Contador:
    def __init__(self):
        self.contador = 0

    def incrementar(self, actualizar_ui):
        self.contador += 1
        actualizar_ui(self.contador)
