from app import Funciones
import csv
import os


# Se crea la clase aplicaciones
class Aplicaciones:
    # Definimos el constructor de nuestro programa
    def __init__(self):
        # Guardo el retorno de la función prev
        self.lista_de_vacunas = self.transformar_datos()

    # Se lee la carpeta CSV y retorna una lista con los nombres de los archivos
    def obtener_nombres(self) -> list:
        nombres = []
        # Se obtiene la ruta absoluta hacia el directorio refuerzos
        carpeta_csv = Funciones.directorio_actual_segun_sistema()

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
        def cambiar_nombre(item) -> dict:
            cambiar_nombre = {
                "Moderna": "Moderna ARNm 020 mg mL",
                "Moderna Bivariante": "Moderna Bivariante BA 4 5",
                "Pfizer": "Pfizer BioNTech Comirnaty",
                "Pfizer Bivariante": "Pfizer Bivariante BA 4 5",
                "Pfizer Pediatrica": "Pfizer Pediátrica",
                "Moderna Pediatrica": "Moderna 010 mg mL",
            }
            for key, value in cambiar_nombre.items():
                if value in item["VACUNA"]:
                    item["VACUNA"] = key
            return item

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
        lista_de_vacunas = []
        for vacuna in data:
            lista_de_vacunas.extend(list(map(obtener, vacuna)))
        lista_de_vacunas = list(map(cambiar_nombre, lista_de_vacunas))

        return lista_de_vacunas

    # Utilizamos para exportar el resultado del proceso
    def exportar_lista_vacunas(self):
        return self.lista_de_vacunas
