# Se importan los modulos necesarios para ejecutar los principales procesos del Programa
import app.ProcesosLogica as PL
import app.LogicaNegocio as LN
import time
from menu import menu


# Función llamada al ejecutar el Programa como script
def run():
    # Primero se ejecuta el proceso que consulta si existe la Base de Datos Completa de vacunas COVID
    # Se guarda en base_existe True o False dependiendo si existe o no la base en cuestión
    # Se guarda en ruta_completa_base_covid None si la base no existe, caso contrario, se guarda la ruta absoluta hacia el archivo de la base de datos completa para ser utilizada más adelante
    (
        base_existe,
        ruta_completa_base_covid,
    ) = LN.consultarExistenciaDeBaseDeDatosCompletaCOVID()

    # Se comprueba si la base existe para desarrollar la lógica principal
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
    # En caso de no existir, se busca obtener los archivos necesarios para crear la Base de Datos
    else:
        # Con el bloque try except capturamos potencionales errores como el no encontrar los archivos necesarios
        try:
            print(
                "\nHola!, en unos segundos iniciará el proceso de descompresión del archivo principal que contiene las bases de datos..."
            )
            time.sleep(2)
            # Se ejecuta el proceso de descomprimir el archivo descargado desde la nube
            LN.desempaquetadoDeComprimidoZIP()

            # Terminado el proceso de desempaquetado. Se inicia la ejecución del proceso de creación de la Base de Datos
            print("Uniendo archivos para generar base de datos completa")
            LN.creacionDeBaseDeDatosCompletaCOVID()
            print(
                "Parece que todo salió bien!, ejecuta nuevamente el script para obtener los datos que precises. Hasta pronto!"
            )
            # Esperamos 2 segundos antes de cortar la ejecución del Programa
            time.sleep(2)
            exit()

        except FileNotFoundError as e:
            LN.creacionDeBaseDeDatosCompletaCOVID()
            print(
                "Parece que todo salió bien!, ejecuta nuevamente el script para obtener los datos que precises. Hasta pronto!"
            )
            time.sleep(2)
            exit()


# Implementamos el condicional para poder ejecutar el programa desde la Consola de Comandos
if __name__ == "__main__":
    inicio = time.time()
    run()
    final = time.time()
    print("Tiempo de ejecución => ", final - inicio)
