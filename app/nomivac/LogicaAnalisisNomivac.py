import app.nomivac.Aplicaciones as APL
import app.nomivac.ProcesarDatosDeCatamarca as PDC
from app.Configuraciones import nombre_carpeta_csv_nomivac, nombre_archivo_base_completa
import app.FuncionesLogicaCSV as PL
import os


def consultarExistenciaDeBaseDeDatosCompletaCOVID(
    nombre_archivo_base_completa=nombre_archivo_base_completa,
):
    # Se obtiene la ruta a la carpeta CSV
    ruta_carpeta_csv = PL.generar_ruta_carpeta_csv(
        carpeta_csv=nombre_carpeta_csv_nomivac
    )
    # Se guarda en es_windows True en caso de que sea Windows el sistema operativo en donde se ejecuta el programa
    es_windows = PL.sistema_actual()
    # Por defecto, dado que en el contexto que se ejecuta el programa Siempre se trabaja con Windows, creo la ruta por defecto para Windows
    ruta_completa_base_covid = f"{ruta_carpeta_csv}\\{nombre_archivo_base_completa}"
    # En caso de que no sea Windows, generamos una ruta estandar para Linux
    if not es_windows:
        ruta_completa_base_covid = f"{ruta_carpeta_csv}/{nombre_archivo_base_completa}"
    # Se crea una bandera para guardar el resultado de la lógica que analizar la existencia de la Base de Datos
    base_existe = False
    # Se analiza el directorio de la carpeta CSV
    with os.scandir(ruta_carpeta_csv) as ficheros:
        # Por cada fichero en ficheros
        for fichero in ficheros:
            # Consultamos si el nombre del fichero coincide con el parametro nombre_archivo_base_completa
            if nombre_archivo_base_completa == fichero.name:
                # Guardamos el valor booleano True en base_existe y cortamos la el bucle con break
                base_existe = True
                break

    # Retornamos la bandera base_existe y ruta_completa_base_covid
    return base_existe, ruta_completa_base_covid


# Proceso de creación de la base de datos Completa
def creacionDeBaseDeDatosCompletaCOVID():
    # Instanciamos la clase Aplicaciones del Modulo Aplicaciones
    aplicaciones = APL.Aplicaciones()

    # Ejecutamos el metodo exportar_lista_vacunas del objeto aplicaciones para generar la Base de Datos Completa
    aplicaciones.exportar_lista_vacunas()


# Proceso para Obtener la lista de vacunas de Catamarca
def procesoObtenerListaDeVacunasDeCatamarca(lista_de_vacunas_completa: list) -> list:
    # Instanciamos la clase ProcesarDatosDeCatamarca
    procesar_datos_catamarca = PDC.ProcesarDatosDeCatamarca(lista_de_vacunas_completa)

    # Se recibe en lista_de_vacunas_catamarca el resultado de ejecutar el metodo obtener_base_arreglada_catamarca
    lista_de_vacunas_catamarca = (
        procesar_datos_catamarca.obtener_base_arreglada_catamarca()
    )
    # Retornamos el resultado
    return lista_de_vacunas_catamarca
