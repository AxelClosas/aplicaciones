import app.ProcesosLogica as PL
import os
import shutil
from app.Configuraciones import nombre_carpeta_csv_nomivac


class MoverArchivos:
    def __init__(self, carpeta_csv=nombre_carpeta_csv_nomivac):
        self.carpeta_csv = carpeta_csv

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
