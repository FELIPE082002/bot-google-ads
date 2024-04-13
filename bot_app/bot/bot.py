from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def driver():
    try:
        service = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=service)
        return navegador
    except Exception as e:
        print(e)


def creacion_navegador(navegador, ejecutando, palabra_clave):
    print(f"Palabra Clave: {palabra_clave}")

    if ejecutando:
            navegador.get('http://www.google.com')
            try:
                inputNavegador = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, '//textarea')))
                inputNavegador.clear()
                inputNavegador.send_keys(palabra_clave)
                inputNavegador.send_keys(Keys.ENTER)
            except Exception as e:
                print("Error: ", e)