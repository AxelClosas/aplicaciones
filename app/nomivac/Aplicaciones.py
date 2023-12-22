import app.FuncionesLogicaCSV as PL
from app.Configuraciones import nombre_carpeta_csv_nomivac
import csv
import os


# Se crea la clase aplicaciones
class Aplicaciones:
    # Definimos el constructor de nuestro programa
    def __init__(self, carpeta_csv=nombre_carpeta_csv_nomivac):
        self.carpeta_csv = carpeta_csv

    def obtener_nombres(self) -> list:
        nombres = []
        # Se obtiene la ruta absoluta hacia el directorio refuerzos
        ruta_carpeta_csv = PL.generar_ruta_carpeta_csv(self.carpeta_csv)
        print(f"Leyendo directorio: {ruta_carpeta_csv}")
        # Con with y la función os.scandir podemos trabajar en el contexto actual del directorio y obtener los nombres de todos los ficheros almacenandolo en la variable ficheros -> lista
        with os.scandir(ruta_carpeta_csv) as ficheros:
            for fichero in ficheros:
                if fichero.is_file() and ".csv" in fichero.name:
                    nombres.append(fichero.name)

        return nombres

    # Se hace uso de los nombres de archivos capturados para la ejecución de los mismos. Se retorna una lista con el contenido de cada archivo
    def generar_lista(self) -> list:
        # Se guarda la lista de nombres obtenida desde
        data = []
        es_windows = PL.sistema_actual()
        archivos = self.obtener_nombres()
        ruta_carpeta_csv = PL.generar_ruta_carpeta_csv(self.carpeta_csv)
        if es_windows:
            rutas_completas_archivos = [
                f"{ruta_carpeta_csv}\\{archivo}" for archivo in archivos if es_windows
            ]
        else:
            rutas_completas_archivos = [
                f"{ruta_carpeta_csv}/{archivo}"
                for archivo in archivos
                if not es_windows
            ]
        data.extend(list(map(PL.read_csv, rutas_completas_archivos)))
        # for archivo in rutas_completas_archivos:
        #     data.append(self.read_csv(archivo))

        return data

    # Se define la función transformar_datos que moldeará los datos que se requieran
    def transformar_datos(self) -> list:
        def cambiar_nombre(item) -> dict:
            cambiar_nombre = {
                "Astrazeneca": "AstraZeneca ChAdOx1 S recombinante",
                "Cansino": "Cansino Ad5 nCoV",
                "Covishield": "COVISHIELD ChAdOx1nCoV COVID 19",
                "Sinopharm": "Sinopharm Vacuna SARSCOV 2 inactivada",
                "Sputnik V": "Sputnik V COVID19 Instituto Gamaleya",
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
                # Datos personales
                "ID": int(item["ID_CMDB_PERSONA"]),
                "NRO_DOC": item["NRO_DOC"],
                "FECHA_NACIMIENTO": item["FECHA_NACIMIENTO"],
                # Datos de domicilio
                "ID_PROVINCIA_DOMICILIO": item["ID_PROVINCIA_DOMICILIO"],
                "PROVINCIA_DOMICILIO": item["PROVINCIA_DOMICILIO"],
                "ID_DEPTO_DOMICILIO": item["ID_DEPTO_DOMICILIO"],
                "DEPTO_DOMICILIO": item["DEPTO_DOMICILIO"],
                "ID_LOCALIDAD_DOMICILIO": item["ID_LOCALIDAD_DOMICILIO"],
                "LOCALIDAD_DOMICILIO": item["LOCALIDAD_DOMICILIO"],
                # Datos de establecimiento de aplicación
                "ID_LOCALIDAD_ESTABLECIMIENTO": int(
                    item["ID_LOCALIDAD_ESTABLECIMIENTO"]
                ),
                "LOCALIDAD_ESTABLECIMIENTO": item["LOCALIDAD_ESTABLECIMIENTO"],
                "COD_ESTABLECIMIENTO": item["COD_ESTABLECIMIENTO"],
                "ESTABLECIMIENTO": item["ESTABLECIMIENTO"],
                "ID_DEPTO_ESTABLECIMIENTO": item["ID_DEPTO_ESTABLECIMIENTO"],
                "DEPTO_ESTABLECIMIENTO": item["DEPTO_ESTABLECIMIENTO"],
                # Datos de Aplicación de la Vacuna
                "FECHA_APLICACION": item["FECHA_APLICACION"],
                "VACUNA": item["VACUNA"],
                "NOMBRE_DOSIS": item["NOMBRE_DOSIS"],
                "LOTE_VACUNA": item["LOTE_VACUNA"],
                # ESQUEMA
                "CODIGO_ESQUEMA": int(item["CODIGO_ESQUEMA"]),
                "ESQUEMA": item["ESQUEMA"],
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
        ruta_carpeta_csv = PL.generar_ruta_carpeta_csv(self.carpeta_csv)
        es_windows = PL.sistema_actual()

        print("Aguarda un momento, esto puede demorar entre 1 y 2 minutos...")
        lista_de_vacunas = self.transformar_datos()
        print("Exportando archivo BaseCompletaCOVID.csv")

        if es_windows:
            nuevo_archivo = f"{ruta_carpeta_csv}\\BaseCompletaCOVID.csv"
        else:
            nuevo_archivo = f"{ruta_carpeta_csv}/BaseCompletaCOVID.csv"

        with open(nuevo_archivo, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=";")
            writer.writerow(lista_de_vacunas[0].keys())
            for vacuna in lista_de_vacunas:
                writer.writerow(vacuna.values())
