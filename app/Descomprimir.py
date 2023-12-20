from app.Configuraciones import (
    nombre_archivo_comprimido_principal,
    nombre_carpeta_csv_nomivac,
)
import app.ProcesosLogica as PL
import zipfile
import os


class Descomprimir:
    def __init__(self, carpeta_csv=nombre_carpeta_csv_nomivac):
        self.carpeta_csv = carpeta_csv

    def comprobar_existencia_de_archivo(self):
        existe = False
        with os.scandir(self.carpeta_csv) as archivos:
            for archivo in archivos:
                if archivo.name == nombre_archivo_comprimido_principal:
                    existe = True

        return existe

    def descomprimir(self, nombre_comprimido=nombre_archivo_comprimido_principal):
        try:
            if self.comprobar_existencia_de_archivo():
                nombre_de_archivos_comprimidos = []
                # Genera ruta de carpeta CSV si es Windows o Linux
                es_windows = PL.sistema_actual()
                ruta_carpeta_csv = PL.generar_ruta_carpeta_csv(self.carpeta_csv)
                # Descomprimir primer archivo "CATAMARCA.zip"
                if es_windows:
                    ruta_comprimido = f"{ruta_carpeta_csv}\\{nombre_comprimido}"
                else:
                    ruta_comprimido = f"{ruta_carpeta_csv}/{nombre_comprimido}"

                print(f"Descomprimiendo archivo {nombre_comprimido}")

                with zipfile.ZipFile(ruta_comprimido, "r") as file:
                    file.extractall(path=ruta_carpeta_csv)
                # Escanera directorio para recopilar nombres de los archivos que extraje desde CATAMARCA.zip
                with os.scandir(ruta_carpeta_csv) as ficheros:
                    for fichero in ficheros:
                        # Comprueba que el nombre del archivo no sea CATAMARCA.zip y que contenga .zip dentro de su nombre y lo agrega a una lista de nombres
                        if nombre_comprimido != fichero.name and ".zip" in fichero.name:
                            nombre_de_archivos_comprimidos.append(fichero.name)
                # Recorre cada nombre para descomprimir los archivos
                for nombre_archivo in nombre_de_archivos_comprimidos:
                    if es_windows:
                        ruta_nombre_archivo = f"{ruta_carpeta_csv}\\{nombre_archivo}"
                    else:
                        ruta_nombre_archivo = f"{ruta_carpeta_csv}/{nombre_archivo}"
                    print(f"Descomprimiendo archivo {nombre_archivo}")
                    with zipfile.ZipFile(ruta_nombre_archivo, "r") as file:
                        file.extractall(path=ruta_carpeta_csv)
            else:
                raise Exception(
                    f"No se encuentra el archivo {nombre_archivo_comprimido_principal}"
                )
        except zipfile.BadZipFile:
            print("Error: Archivo Zip corrupto.")
        except Exception as e:
            print(e)
            exit()


# def run():
#     d = Descomprimir()
#     d.limpieza_de_directorio()


# if __name__ == "__main__":
#     run()
