import csv
import os

class Refuerzos:
    def obtener_nombres(self):
        nombres = []
        # Obtengo la ruta absoluta del directorio actual
        directorio_actual = os.getcwd()
        carpeta_csv = f'{directorio_actual}\\CSV'

        # Con with podemos trabajar en el contexto actual del directorio y obtener los nombres de todos los ficheros
        with os.scandir(carpeta_csv) as ficheros:
            for fichero in ficheros:
                # Si el archivo es main.py simplemente lo pasa por alto continuando con el ciclo
                if fichero.name == 'main.py': continue
                nombres.append(fichero.name)
        return nombres
    
    def read_csv(self, path):
        with open(path, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            header = next(reader)
            data = []
            for row in reader:
                iterable = zip(header, row)
                vacuna_aplicada = {key:value for key, value in iterable}
                data.append(vacuna_aplicada)
        return data
    
    def generar_lista(self):
        archivos = self.obtener_nombres()
        data = []
        for archivo in archivos:
            lista = self.read_csv(f'./CSV/{archivo}')
            data.append(lista)
        return data
    
    def transformar_datos(self):
        def obtener(item):
            n_dict = {
                'DNI': item['NRO_DOC'],
                'VACUNA': item['VACUNA'],
                'FECHA_APLICACION': item['FECHA_APLICACION'],
                'DOSIS': item['NOMBRE_DOSIS']
                }
            return n_dict
        
        data = self.generar_lista()
        nuevo = []
        for vacuna in data:
            nuevo.append(list(map(obtener, vacuna)))
        return nuevo