import platform
import csv
import os

class Refuerzo:
    def __init__(self):
        def __init__(self):
            self.sistema = platform.system()
            self.lista_de_vacunas = self.transformar_datos()

    def transformar_datos(self) -> list:
        def obtener(item) -> dict:
            n_dict = {
                'ID': item['ID_CMDB_PERSONA'],
                'DNI': item['NRO_DOC'],
                'VACUNA': item['VACUNA'],
                'FECHA_APLICACION': item['FECHA_APLICACION'],
                'DOSIS': item['NOMBRE_DOSIS'],
                'PROVINCIA': item['PROVINCIA_DOMICILIO']
                }
            return n_dict
        
        data = self.generar_lista()
        nuevo = []
        for vacuna in data:
            nuevo.extend(list(map(obtener, vacuna)))
        return nuevo
    
    def obtener_nombres(self) -> list:
        nombres = []
        # Obtengo la ruta absoluta del directorio actual
        directorio_actual = os.getcwd()        
        if self.sistema == 'Windows':
            carpeta_csv = f'{directorio_actual}\\CSV'
            print(carpeta_csv)
        else:
            carpeta_csv = f'{directorio_actual}/CSV'
            print(carpeta_csv)

        print(f'Leyendo directorio: {carpeta_csv}')
        # Con with podemos trabajar en el contexto actual del directorio y obtener los nombres de todos los ficheros
        with os.scandir(carpeta_csv) as ficheros:
            for fichero in ficheros:
                if '.csv' in fichero.name:
                    nombres.append(fichero.name)
        return nombres
    
    def read_csv(self, path) -> list:
        with open(path, 'r', encoding='latin-1') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            header = next(reader)
            data = []
            for row in reader:
                iterable = zip(header, row)
                vacuna_aplicada = {key:value for key, value in iterable}
                data.append(vacuna_aplicada)
            
        return data
    
    def generar_lista(self) -> list:
        archivos = self.obtener_nombres()
        data = []
        for archivo in archivos:
            print(f'Recopilando datos de {archivo}')
            lista = self.read_csv(f'./CSV/{archivo}')
            data.append(lista)
        
        return data