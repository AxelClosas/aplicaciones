import app.nomivac.Aplicaciones as APL
import app.nomivac.ProcesarDatosDeCatamarca as PDC
from app.Configuraciones import nombre_carpeta_csv_nomivac, nombre_archivo_base_completa
import app.FuncionesLogicaCSV as FL
from app.nomivac.Filtro import Filtro
import os
from datetime import date


def consultarExistenciaDeBaseDeDatosCompletaCOVID(
    nombre_archivo_base_completa=nombre_archivo_base_completa,
):
    # Se obtiene la ruta a la carpeta CSV
    ruta_carpeta_csv = FL.generar_ruta_carpeta_csv(
        carpeta_csv=nombre_carpeta_csv_nomivac
    )
    # Se guarda en es_windows True en caso de que sea Windows el sistema operativo en donde se ejecuta el programa
    es_windows = FL.sistema_actual()
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


def proceso_obtener_esquema_completo_y_refuerzos_ultimos_6_meses_por_departamento_y_rango_etario(
    lista_de_vacunas_completa: list[dict],
) -> list[dict]:
    """Se devuelve una lista de diccionario con la estructura siguiente:
    [
        {
            ID_DEPTO_ESTABLECIMIENTO: 35,
            DEPTO_ESTABLECIMIENTO: Valle Viejo,
            # Los siguientes datos se obtienen desde el padrón de 2das dosis.
            ESQUEMA_COMPLETO: {
                RANGO_ETARIO_0_A_2: 100,
                RANGO_ETARIO_3_A_11: 100,
                RANGO_ETARIO_12_A_17: 100,
                RANGO_ETARIO_18_A_49: 100,
                RANGO_ETARIO_50_Y_MAS: 100,
            },
            # Los siguientes datos se obtienen desde el padrón de Refuerzos.
            REFUERZOS_ULTIMOS_6_MESES: {
                RANGO_ETARIO_0_A_2: 100,
                RANGO_ETARIO_3_A_11: 100,
                RANGO_ETARIO_12_A_17: 100,
                RANGO_ETARIO_18_A_49: 100,
                RANGO_ETARIO_50_Y_MAS: 100,
            }
        },
    ]
    """
    filtrar = Filtro()
    padron = filtrar.filtrar_segunda_dosis(lista_de_vacunas_completa)
    refuerzos = filtrar.filtrar_refuerzos(lista_de_vacunas_completa)
    fecha = input("Ingresa la fecha limite de 6 meses: ")
    refuerzos_ultimos_6_meses = filtrar.filtrar_por_fecha_de_aplicacion(
        refuerzos, fecha
    )

    id_departamentos = FL.obtener_id_departamentos_desde_archivo()

    estructura = [
        {
            "ID_DEPTO_ESTABLECIMIENTO": key,
            "DEPTO_ESTABLECIMIENTO": value,
            "ESQUEMA_COMPLETO": {
                "RANGO_ETARIO_0_A_2": 0,
                "RANGO_ETARIO_3_A_11": 0,
                "RANGO_ETARIO_12_A_17": 0,
                "RANGO_ETARIO_18_A_49": 0,
                "RANGO_ETARIO_50_Y_MAS": 0,
            },
            "REFUERZOS_ULTIMOS_6_MESES": {
                "RANGO_ETARIO_0_A_2": 0,
                "RANGO_ETARIO_3_A_11": 0,
                "RANGO_ETARIO_12_A_17": 0,
                "RANGO_ETARIO_18_A_49": 0,
                "RANGO_ETARIO_50_Y_MAS": 0,
            },
            "PENDIENTES": {
                "RANGO_ETARIO_0_A_2": 0,
                "RANGO_ETARIO_3_A_11": 0,
                "RANGO_ETARIO_12_A_17": 0,
                "RANGO_ETARIO_18_A_49": 0,
                "RANGO_ETARIO_50_Y_MAS": 0,
            },
        }
        for key, value in id_departamentos.items()
    ]
    # Se obtienen los esquemas completos por rango etario
    for item in padron:
        for depto in estructura:
            if (
                int(item["ID_DEPTO_ESTABLECIMIENTO"])
                == depto["ID_DEPTO_ESTABLECIMIENTO"]
            ):
                if 0 <= int(item["EDAD_APLICACION"]) <= 2:
                    depto["ESQUEMA_COMPLETO"]["RANGO_ETARIO_0_A_2"] += 1

                elif 3 <= int(item["EDAD_APLICACION"]) <= 11:
                    depto["ESQUEMA_COMPLETO"]["RANGO_ETARIO_3_A_11"] += 1

                elif 12 <= int(item["EDAD_APLICACION"]) <= 17:
                    depto["ESQUEMA_COMPLETO"]["RANGO_ETARIO_12_A_17"] += 1

                elif 18 <= int(item["EDAD_APLICACION"]) <= 49:
                    depto["ESQUEMA_COMPLETO"]["RANGO_ETARIO_18_A_49"] += 1

                else:
                    depto["ESQUEMA_COMPLETO"]["RANGO_ETARIO_50_Y_MAS"] += 1

    # Se obtienen los refuerzos por rango etario de los ultimos 6 meses
    for item in refuerzos_ultimos_6_meses:
        for depto in estructura:
            if (
                int(item["ID_DEPTO_ESTABLECIMIENTO"])
                == depto["ID_DEPTO_ESTABLECIMIENTO"]
            ):
                if 0 <= int(item["EDAD_APLICACION"]) <= 2:
                    depto["REFUERZOS_ULTIMOS_6_MESES"]["RANGO_ETARIO_0_A_2"] += 1

                elif 3 <= int(item["EDAD_APLICACION"]) <= 11:
                    depto["REFUERZOS_ULTIMOS_6_MESES"]["RANGO_ETARIO_3_A_11"] += 1

                elif 12 <= int(item["EDAD_APLICACION"]) <= 17:
                    depto["REFUERZOS_ULTIMOS_6_MESES"]["RANGO_ETARIO_12_A_17"] += 1

                elif 18 <= int(item["EDAD_APLICACION"]) <= 49:
                    depto["REFUERZOS_ULTIMOS_6_MESES"]["RANGO_ETARIO_18_A_49"] += 1

                else:
                    depto["REFUERZOS_ULTIMOS_6_MESES"]["RANGO_ETARIO_50_Y_MAS"] += 1

    for item in estructura:
        item["PENDIENTES"]["RANGO_ETARIO_0_A_2"] = (
            item["ESQUEMA_COMPLETO"]["RANGO_ETARIO_0_A_2"]
            - item["REFUERZOS_ULTIMOS_6_MESES"]["RANGO_ETARIO_0_A_2"]
        )
        item["PENDIENTES"]["RANGO_ETARIO_3_A_11"] = (
            item["ESQUEMA_COMPLETO"]["RANGO_ETARIO_3_A_11"]
            - item["REFUERZOS_ULTIMOS_6_MESES"]["RANGO_ETARIO_3_A_11"]
        )
        item["PENDIENTES"]["RANGO_ETARIO_12_A_17"] = (
            item["ESQUEMA_COMPLETO"]["RANGO_ETARIO_12_A_17"]
            - item["REFUERZOS_ULTIMOS_6_MESES"]["RANGO_ETARIO_12_A_17"]
        )
        item["PENDIENTES"]["RANGO_ETARIO_18_A_49"] = (
            item["ESQUEMA_COMPLETO"]["RANGO_ETARIO_18_A_49"]
            - item["REFUERZOS_ULTIMOS_6_MESES"]["RANGO_ETARIO_18_A_49"]
        )
        item["PENDIENTES"]["RANGO_ETARIO_50_Y_MAS"] = (
            item["ESQUEMA_COMPLETO"]["RANGO_ETARIO_50_Y_MAS"]
            - item["REFUERZOS_ULTIMOS_6_MESES"]["RANGO_ETARIO_50_Y_MAS"]
        )

    return estructura
