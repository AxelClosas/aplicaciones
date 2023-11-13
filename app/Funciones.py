import os
import platform

sistema = platform.system()
# Capturo el sistema operativo para diseñar la ruta a la carpeta CSV


def directorio_actual_segun_sistema():
    directorio_actual = os.getcwd()
    # Mediante una función lambda retornamos verdadero o falso si el sistema capturado coincide con el S.O enviado como argumento
    validar = lambda sys: sistema == sys
    if validar("Windows"):
        # Se crea la ruta hacia la carpeta CSV en Windows
        carpeta_csv = f"{directorio_actual}\\CSV"
    else:
        # Se crea la ruta hacia la carpeta CSV en Linux
        carpeta_csv = f"{directorio_actual}/CSV"
    # Log de ejecución
    return carpeta_csv
