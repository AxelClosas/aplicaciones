import app.ProcesosLogica as PL
import os
from app.Configuraciones import nombre_carpeta_csv_nomivac


class Limpieza:
    def __init__(self, carpeta_csv=nombre_carpeta_csv_nomivac):
        self.carpeta_csv = carpeta_csv

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
