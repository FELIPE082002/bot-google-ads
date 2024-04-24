import tkinter as tk
from bot_app.app.logica import Contador
from threading import Thread
from bot_app.bot.bot_controller import Bot  
import sys
sys.path.append('..') 

class InterfazContador:
    def __init__(self, master):
        self.master = master
        self.contador = Contador()
        self.bot = Bot()  # Crea una instancia del bot
        self.master.title("Contador")

        self.etiqueta_contador = tk.Label(master, text="0", font=("Arial", 24))
        self.etiqueta_contador.pack()

        self.etiqueta_estado = tk.Label(master, text="Detenido", fg="red", font=("Arial", 16))
        self.etiqueta_estado.pack()

        self.boton_ejecutar_bot = tk.Button(master, text="Iniciar Bot", command=self.iniciar_bot)
        self.boton_ejecutar_bot.pack(side=tk.LEFT, padx=10, pady=10)

        self.boton_detener_bot = tk.Button(master, text="Detener Bot", command=self.detener_bot)
        self.boton_detener_bot.pack(side=tk.RIGHT, padx=10, pady=10)

    def actualizar_ui(self, valor):
        self.etiqueta_contador.config(text=str(valor))

    def actualizar_estado(self, estado):
        if estado:
            self.etiqueta_estado.config(text="Corriendo", fg="green")
        else:
            self.etiqueta_estado.config(text="Detenido", fg="red")

    def iniciar_bot(self):
        self.bot.iniciar(self.incrementar, self.actualizar_estado_bot_detenido)
        self.actualizar_estado(True)

    def detener_bot(self):
        self.bot.detener()
        self.actualizar_estado_bot_detenido()  # Actualiza la etiqueta de estado a "Detenido"

    def incrementar(self):
        self.contador.incrementar(self.actualizar_ui)

    def actualizar_estado_bot_detenido(self):
        self.actualizar_estado(False)