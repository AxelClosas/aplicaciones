import app.ProcesosLogica as PL
import app.Aplicaciones as APL
import app.Descomprimir as Des
import app.ProcesarDatosDeCatamarca as PDC
import os


def consultarExistenciaDeBaseDeDatosCompletaCOVID():
    ruta_carpeta_csv = PL.generar_ruta_carpeta_csv(carpeta_csv="CSV")
    nombre_archivo_base_completa = "BaseCompletaCOVID.csv"
    es_windows = PL.sistema_actual()
    ruta_completa_base_covid = f"{ruta_carpeta_csv}\\{nombre_archivo_base_completa}"
    if not es_windows:
        ruta_completa_base_covid = f"{ruta_carpeta_csv}/{nombre_archivo_base_completa}"

    base_existe = False

    with os.scandir(ruta_carpeta_csv) as ficheros:
        for fichero in ficheros:
            if nombre_archivo_base_completa == fichero.name:
                base_existe = True
                break

    return base_existe, ruta_completa_base_covid


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


def procesoObtenerListaDeVacunasDeCatamarca(lista_de_vacunas_completa: list) -> list:
    procesar_datos_catamarca = PDC.ProcesarDatosDeCatamarca(lista_de_vacunas_completa)

    lista_de_vacunas_catamarca = (
        procesar_datos_catamarca.obtener_base_arreglada_catamarca()
    )
    return lista_de_vacunas_catamarca
