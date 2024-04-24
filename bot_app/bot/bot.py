from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def obtener_driver():
    try:
        service = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=service)
        return navegador
    except Exception as e:
        print(f"Error al iniciar el navegador: {e}")
        return None

def buscar_palabra_clave(navegador, palabra_clave, url):

    if navegador is None:
        print("Navegador no iniciado.")
        return 

    try:
        navegador.get('http://www.google.com')
        input_navegador = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.NAME, 'q')))
        input_navegador.clear()
        input_navegador.send_keys(palabra_clave + Keys.ENTER)
        
        click_enlaces(navegador,url)
    except Exception as e:
        print(f"Error durante la búsqueda: {e}")

def click_enlaces(navegador, url):
    try:
        WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.v5yQqb")))
        
        enlaces = navegador.find_elements(By.XPATH, "//div[@class='v5yQqb']//a")
        
        for enlace in enlaces:
            href = enlace.get_attribute('data-pcu')
            if href:
                
                if url in href:
                    print("Coincide: ",href)
                    enlace.click()
                    
            else:
                print("Enlace sin href detectado.")

    except Exception as e:
        print(f"Error al mostrar enlaces: {e}")