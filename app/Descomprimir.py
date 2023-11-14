import app.ProcesosLogica as PL
import zipfile
import os
import shutil
from platform import system


class Descomprimir:
    def __init__(self):
        self.sistema = system()

    def descomprimir(self):
        try:
            mi_archivo = "CATAMARCA.zip"
            nombre_de_archivos_comprimidos = []
            carpeta_csv = PL.directorio_actual_segun_sistema()
            # Descomprimir primer archivo "CATAMARCA.zip"
            print(f"Descomprimiendo archivo {mi_archivo}")
            with zipfile.ZipFile(f"{carpeta_csv}/{mi_archivo}", "r") as file:
                file.extractall(path=carpeta_csv)
            # Escanera directorio para recopilar nombres de los archivos que extraje desde CATAMARCA.zip
            with os.scandir(carpeta_csv) as ficheros:
                for fichero in ficheros:
                    # Comprueba que el nombre del archivo no sea CATAMARCA.zip y que contenga .zip dentro de su nombre y lo agrega a una lista de nombres
                    if mi_archivo != fichero.name and ".zip" in fichero.name:
                        nombre_de_archivos_comprimidos.append(fichero.name)
            # Recorre cada nombre para descomprimir los archivos
            for nombre_archivo in nombre_de_archivos_comprimidos:
                print(f"Descomprimiendo archivo {nombre_archivo}")
                with zipfile.ZipFile(f"{carpeta_csv}/{nombre_archivo}", "r") as file:
                    file.extractall(path=carpeta_csv)
        except zipfile.BadZipFile:
            print("Error: Archivo Zip corrupto.")

    def mover_archivos_csv(self):
        carpeta_csv = directorio_actual_segun_sistema()
        carpetas = []
        with os.scandir(carpeta_csv) as ficheros:
            for fichero in ficheros:
                if os.path.isdir(fichero):
                    carpetas.append(fichero.name)
        for carpeta in carpetas:
            with os.scandir(f"{carpeta_csv}/{carpeta}") as ficheros:
                for fichero in ficheros:
                    print(f"Moviendo archivo {fichero} a {carpeta_csv}")
                    shutil.move(fichero, f"{carpeta_csv}")

    def limpieza_de_directorio(self):
        carpeta_csv = directorio_actual_segun_sistema()

        print(f"Limpiando directorio {carpeta_csv}")
        with os.scandir(carpeta_csv) as ficheros:
            for fichero in ficheros:
                if ".zip" in fichero.name:
                    if self.sistema != "Windows":
                        os.remove(f"{carpeta_csv}/{fichero.name}")
                    else:
                        os.remove(f"{carpeta_csv}\\{fichero.name}")
                if os.path.isdir(fichero):
                    os.rmdir(fichero)


# def run():
#     d = Descomprimir()
#     d.limpieza_de_directorio()


# if __name__ == "__main__":
#     run()
