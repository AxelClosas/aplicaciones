from app.smis.AnalisisDistribucion import AnalisisDistribucion
from app.smis.Distribucion import Distribucion
from app.smis.Covid import Covid
from app.smis.Dicei import Dicei
from app.Configuraciones import (
    cod_institucion_pai_catamarca,
    nombre_carpeta_csv_smis,
    nombre_archivo_csv_smis,
    programa_covid,
    programa_dicei,
)
from datetime import datetime


def proceso_filtrar_origen_paicatamarca_a_instituciones_covid() -> list:
    """
    Retorna una lista de diccionarios
    [
        {
            "Código institución destino": "Código de institución de tipo Entero",
            "Institución destino": "Nombre de Institución",
            "Vacunas": {
                "Moderna": 300,
                "Sinopharm": 500,
                ...
            },
            "Total distribuidas": 800
        }
    ]
    """
    # Se crea una instancia de Distribucion
    distribucion = Distribucion(
        nombre_carpeta_csv_smis=nombre_carpeta_csv_smis,
        nombre_archivo_csv_smis=nombre_archivo_csv_smis,
    )

    # Almaceno los movimientos regulares
    movimientos_covid = distribucion.retornar_movimientos_de_programa_sanitario(
        programa_covid
    )

    covid = Covid(movimientos=movimientos_covid)
    movimientos_regulares_covid = covid.retornar_movimientos_regulares()

    # Se Crea una instancia de AnalisisDistribucion para trabajar
    analisis = AnalisisDistribucion(movimientos=movimientos_regulares_covid)

    # Filtramos por el Código de la institución Origen. El de Pai Catamarca es el 12
    mov_origen_pai_catamarca = analisis.filtrar_institucion_origen(
        cod_institucion_pai_catamarca
    )

    # Filtramos por el rango de todo 2023
    fecha_entrega_2023 = analisis.filtrar_por_fecha_entrega(
        movimientos=mov_origen_pai_catamarca,
        fecha_minima=datetime.strptime("01/01/2023", "%d/%m/%Y"),
        fecha_maxima=datetime.strptime("31/12/2023", "%d/%m/%Y"),
    )

    # Se obtiene el movimiento mediante el nro_remito con fecha incorrecta en SISA - Está cargando en Inventario interno con fecha correcta de 2023
    remito_2200 = analisis.retornar_registro_nro_remito("2200")
    # Se lo agrega a la lista de movimientos
    fecha_entrega_2023.append(remito_2200)

    # Pasamos como argumento la lista final para el analisis

    resultado = analisis.obtener_el_total_distribuido_por_Vacuna_a_cada_institucion(
        fecha_entrega_2023
    )
    return resultado


def proceso_filtrar_origen_paicatamarca_a_instituciones_dicei() -> list:
    """
    Retorna una lista de diccionarios
    [
        {
            "Código institución destino": "Código de institución de tipo Entero",
            "Institución destino": "Nombre de Institución",
            "Vacunas": {
                "BCG": 300,
                "VPH": 500,
                ...
            },
        }
    ]
    """
    distribucion = Distribucion(
        nombre_carpeta_csv_smis=nombre_carpeta_csv_smis,
        nombre_archivo_csv_smis=nombre_archivo_csv_smis,
    )
    movimientos_dicei = distribucion.retornar_movimientos_de_programa_sanitario(
        programa_dicei
    )
    dicei = Dicei(movimientos=movimientos_dicei)
    movimientos_regulares_dicei = dicei.retornar_movimientos_regulares()
    analisis_dicei = AnalisisDistribucion(movimientos=movimientos_regulares_dicei)

    mov_origen_pai_catamarca_dicei = analisis_dicei.filtrar_institucion_origen(
        cod_institucion_pai_catamarca
    )
    fecha_entrega_2023_dicei = analisis_dicei.filtrar_por_fecha_entrega(
        movimientos=mov_origen_pai_catamarca_dicei,
        fecha_minima=datetime.strptime("01/01/2023", "%d/%m/%Y"),
        fecha_maxima=datetime.strptime("31/12/2023", "%d/%m/%Y"),
    )
    resultado_dicei = (
        analisis_dicei.obtener_el_total_distribuido_por_Vacuna_a_cada_institucion(
            movimientos=fecha_entrega_2023_dicei
        )
    )

    return resultado_dicei
