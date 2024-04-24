from bot_app.app.utils.excel import ExcelController
from bot_app.bot.bot import obtener_driver, buscar_palabra_clave
from threading import Thread

class Bot:
    def __init__(self):
        self.ejecutando = False
        self.thread = None
        self.navegador = None

    def ejecutar_bot(self, callback_incrementar, callback_finalizar=None):
        self.ejecutando = True
        controlador_excel = ExcelController()
        
        while self.ejecutando:
            empresas = controlador_excel.obtener_columnas_excel()
            try:
                for empresa in empresas:
                    if not self.ejecutando:
                        break
                    self.navegador = obtener_driver()
                    for palabra_clave in empresa['palabras_clave']:
                        if not self.ejecutando:
                            break
                        buscar_palabra_clave(self.navegador, palabra_clave, empresa['url'],callback_incrementar)

                    if self.navegador:
                        self.navegador.quit()
                        self.navegador = None
            except Exception as e:
                print(f"Error: {e}")
            finally:
                if self.navegador:
                    self.navegador.quit()

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
            self.thread.join(5)  # Espera hasta 5 segundos para que el hilo termine
            if self.thread.is_alive():
                print("El hilo no pudo terminar correctamente.")
            self.thread = None