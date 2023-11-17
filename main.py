import app.ProcesosLogica as PL
import app.AnalisisAplicaciones as AP
import app.LogicaNegocio as LN
import time
import os
from menu import menu


def run():
    (
        base_existe,
        ruta_completa_base_covid,
    ) = LN.consultarExistenciaDeBaseDeDatosCompletaCOVID()

    # Si la base ya existe, aquí armamos el menú
    if base_existe:
        lista_de_vacunas_completa = PL.read_csv(ruta_completa_base_covid)
        lista_de_vacunas_catamarca = LN.procesoObtenerListaDeVacunasDeCatamarca(
            lista_de_vacunas_completa
        )
        print(menu())
        opcion = int(input("Opción => "))

        match opcion:
            case 1:
                print("Generando reporte...\n")
                LN.generarPrimerReporte(
                    lista_de_vacunas_completa, lista_de_vacunas_catamarca
                )
            case 2:
                print("Generando reporte...\n")
                LN.generarSegundoReporte(
                    lista_de_vacunas_completa, lista_de_vacunas_catamarca
                )
            case 3:
                print("Generando reporte...\n")
                LN.generarTercerReporte(
                    lista_de_vacunas_completa, lista_de_vacunas_catamarca
                )
            case _:
                print(
                    "Ups... El número que ingresaste no se encuentra en el menú. Por favor, elije otro."
                )
    else:
        try:
            print(
                "\nHola!, en unos segundos iniciará el proceso de descompresión del archivo principal que contiene las bases de datos..."
            )
            time.sleep(2)
            LN.desempaquetadoDeComprimidoZIP()
            print("Uniendo archivos para generar base de datos completa")
            LN.creacionDeBaseDeDatosCompletaCOVID()
            print(
                "Parece que todo salió bien!, ejecuta nuevamente el script para obtener los datos que precises. Hasta pronto!"
            )
            time.sleep(2)
            exit()

        except FileNotFoundError as e:
            LN.creacionDeBaseDeDatosCompletaCOVID()
            print(
                "Parece que todo salió bien!, ejecuta nuevamente el script para obtener los datos que precises. Hasta pronto!"
            )
            time.sleep(2)
            exit()


if __name__ == "__main__":
    inicio = time.time()
    run()
    final = time.time()
    print("Tiempo de ejecución => ", final - inicio)
