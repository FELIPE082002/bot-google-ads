import pandas as pd

class ExcelController:
    def __init__(self, archivo='Empresas.xlsx'):

        self.df = pd.read_excel(archivo, engine='openpyxl')
        
    def obtener_columnas_excel(self):
        resultados = self.df
        
        palabras_object = []
    
        if not resultados.empty:
            for _, fila in resultados.iterrows():
                url = fila['url']
                palabras_clave = fila['Palabras Clave']
                palabras_clave_arrary = palabras_clave.split(',')
                url_form = fila['url Form']
                palabras_object.append(
                    {
                        "url" : url,
                        "palabras_clave" : palabras_clave_arrary,
                        "url_form" : url_form
                    }
                )
        else:
            print("No se encontraron resultados.")
            
        return palabras_object