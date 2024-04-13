from bot_app.app.utils.excel import ExcelController
from bot_app.bot.bot import driver,creacion_navegador
from threading import Thread

class Bot:
    def __init__(self):
        self.ejecutando = False
        self.thread = None
        self.navegador = None  # Referencia al navegador para poder cerrarlo

    def ejecutar_bot(self, callback_incrementar, callback_finalizar=None):
        self.ejecutando = True
        controlador_excel = ExcelController()
        empresas = controlador_excel.obtener_columnas_excel()

        for empresa in empresas:
            if not self.ejecutando:
                break
            print(empresa['nombre'])
            for palabra_clave in empresa['palabras_clave']:
                if not self.ejecutando:
                    break
                self.navegador = driver()  # Asumimos que bot devuelve la instancia del navegador
                creacion_navegador(self.navegador, self.ejecutando, palabra_clave)
                callback_incrementar()
        
        if callback_finalizar:
            callback_finalizar()
        self.ejecutando = False

    def iniciar(self, callback_incrementar, callback_finalizar=None):
        if not self.ejecutando:
            self.thread = Thread(target=self.ejecutar_bot, args=(callback_incrementar, callback_finalizar))
            self.thread.start()

    def detener(self):
        self.ejecutando = False
        if self.navegador:
            self.navegador.quit()  
        if self.thread:
            self.thread.join()
            self.thread = None