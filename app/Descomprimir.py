import app.ProcesosLogica as PL
import zipfile
import os
import shutil


class Descomprimir:
    def __init__(self, carpeta_csv="CSV"):
        self.carpeta_csv = carpeta_csv

    def descomprimir(self, nombre_comprimido="CATAMARCA.zip"):
        try:
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
        except zipfile.BadZipFile:
            print("Error: Archivo Zip corrupto.")

    def mover_archivos_csv(self):
        carpeta_csv = PL.generar_ruta_carpeta_csv(self.carpeta_csv)
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
        carpeta_csv = PL.generar_ruta_carpeta_csv(self.carpeta_csv)
        es_windows = PL.sistema_actual()

        print(f"Limpiando directorio {carpeta_csv}")
        with os.scandir(carpeta_csv) as ficheros:
            for fichero in ficheros:
                if ".zip" in fichero.name:
                    if es_windows:
                        os.remove(f"{carpeta_csv}\\{fichero.name}")
                    else:
                        os.remove(f"{carpeta_csv}/{fichero.name}")
                if os.path.isdir(fichero):
                    os.rmdir(fichero)


# def run():
#     d = Descomprimir()
#     d.limpieza_de_directorio()


# if __name__ == "__main__":
#     run()
