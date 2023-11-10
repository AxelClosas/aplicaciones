import platform
import csv
import os


# Se crea la clase aplicaciones
class Aplicaciones:
    # Definimos el constructor de nuestro programa
    def __init__(self):
        # Capturo el sistema operativo para diseñar la ruta a la carpeta CSV
        self.sistema = platform.system()
        # Guardo el retorno de la función prev
        self.lista_de_vacunas = self.transformar_datos()

    # Se lee la carpeta CSV y retorna una lista con los nombres de los archivos
    def obtener_nombres(self) -> list:
        nombres = []
        # Se obtiene la ruta absoluta hacia el directorio refuerzos
        directorio_actual = os.getcwd()
        # Mediante una función lambda retornamos verdadero o falso si el sistema capturado coincide con el S.O enviado como argumento
        validar = lambda sys: self.sistema == sys
        if validar("Windows"):
            # Se crea la ruta hacia la carpeta CSV en Windows
            carpeta_csv = f"{directorio_actual}\\CSV"
        else:
            # Se crea la ruta hacia la carpeta CSV en Linux
            carpeta_csv = f"{directorio_actual}/CSV"
        # Log de ejecución
        print(f"Leyendo directorio: {carpeta_csv}")
        # Con with y la función os.scandir podemos trabajar en el contexto actual del directorio y obtener los nombres de todos los ficheros almacenandolo en la variable ficheros -> lista
        with os.scandir(carpeta_csv) as ficheros:
            for fichero in ficheros:
                if ".csv" in fichero.name:
                    nombres.append(fichero.name)
        return nombres

    # Se hace uso de los nombres de archivos capturados para la ejecución de los mismos. Se retorna una lista con el contenido de cada archivo
    def generar_lista(self) -> list:
        archivos = self.obtener_nombres()
        data = []
        for archivo in archivos:
            print(f"Recopilando datos de {archivo}")
            lista = self.read_csv(f"./CSV/{archivo}")
            data.append(lista)

        return data

    # Función que procesa la lectura y guardado de un archivo csv
    def read_csv(self, path) -> list:
        with open(path, "r", encoding="latin-1") as csvfile:
            reader = csv.reader(csvfile, delimiter=";")
            header = next(reader)
            data = []
            for row in reader:
                iterable = zip(header, row)
                vacuna_aplicada = {key: value for key, value in iterable}
                data.append(vacuna_aplicada)

        return data

    # Se define la función transformar_datos que moldeará los datos que se requieran
    def transformar_datos(self) -> list:
        def obtener(item) -> dict:
            n_dict = {
                "ID": item["ID_CMDB_PERSONA"],
                "DNI": item["NRO_DOC"],
                "VACUNA": item["VACUNA"],
                "FECHA_APLICACION": item["FECHA_APLICACION"],
                "DOSIS": item["NOMBRE_DOSIS"],
                "PROVINCIA": item["PROVINCIA_DOMICILIO"],
            }
            return n_dict

        data = self.generar_lista()
        nuevo = []
        for vacuna in data:
            nuevo.extend(list(map(obtener, vacuna)))
        return nuevo

    # Utilizamos para exportar el resultado del proceso
    def exportar_lista_vacunas(self):
        return self.lista_de_vacunas
