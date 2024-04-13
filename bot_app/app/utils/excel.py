import pandas as pd

class ExcelController:
    def __init__(self, archivo='Test.xlsx'):

        self.df = pd.read_excel(archivo, engine='openpyxl')
        
    def obtener_columnas_excel(self):
        resultados = self.df
        
        palabras_object = []
    
        if not resultados.empty:
            for _, fila in resultados.iterrows():
                nombre = fila['Nombre']
                palabras_clave = fila['Palabras Clave']
                palabras_clave_arrary = palabras_clave.split(',')
                palabras_object.append(
                    {
                        "nombre" : nombre,
                        "palabras_clave" : palabras_clave_arrary
                    }
                )
        else:
            print("No se encontraron resultados.")
            
        return palabras_object

# if __name__ == "__main__":
#     controlador_excel = ExcelController() 
#     print(controlador_excel.buscar_por_palabra_clave())