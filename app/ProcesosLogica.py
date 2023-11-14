import app.Aplicaciones as APL
import app.Descomprimir as Des

from platform import system
import os
import csv


def desempaquetadoDeComprimidoZIP():
    descompresor = Des.Descomprimir()
    print("Descomprimiendo archivo...")
    descompresor.descomprimir()
    print("Moviendo archivos...")
    descompresor.mover_archivos_csv()
    print("Limpiando directorio...")
    descompresor.limpieza_de_directorio()


def creacionDeBaseDeDatosCompletaCOVID():
    aplicaciones = APL.Aplicaciones()
    aplicaciones.exportar_lista_vacunas()


def sistema_actual():
    # Retorna True si es Windows o False si no lo es
    sistema = system()
    return True if sistema == "Windows" else False


def generar_ruta_carpeta_csv(carpeta_csv):
    # Recibe True si es Windows o False si no lo és
    es_windows = sistema_actual()
    directorio_actual = os.getcwd()
    if es_windows:
        ruta_carpeta_csv = f"{directorio_actual}\\{carpeta_csv}"
    else:
        ruta_carpeta_csv = f"{directorio_actual}/{carpeta_csv}"
    return ruta_carpeta_csv

    # Función que procesa la lectura y guardado de un archivo csv


def read_csv(path) -> list:
    with open(path, "r", encoding="latin-1") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            vacuna_aplicada = {key: value for key, value in iterable}
            data.append(vacuna_aplicada)

    return data
