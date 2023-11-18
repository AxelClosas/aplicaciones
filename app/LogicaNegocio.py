# Se importan los modulos necesarios
import app.ProcesosLogica as PL
import app.Aplicaciones as APL
import app.Descomprimir as Des
import app.ProcesarDatosDeCatamarca as PDC
import os
import app.AnalisisAplicaciones as AP
import app.AnalisisRefuerzo as AR
import app.MoverArchivos as MA
import app.Limpieza as LIMP
from app.Configuraciones import nombre_carpeta_csv, nombre_archivo_base_completa


def creditos():
    return "Programa creado por: Axel Closas Agüero"


# Proceso para consultar la existencia de la Base de Datos
def consultarExistenciaDeBaseDeDatosCompletaCOVID(
    nombre_archivo_base_completa=nombre_archivo_base_completa,
):
    # Se obtiene la ruta a la carpeta CSV
    ruta_carpeta_csv = PL.generar_ruta_carpeta_csv(carpeta_csv=nombre_carpeta_csv)
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


# Proceso para descomprimir el archivo CATAMARCA.zip
def desempaquetadoDeComprimidoZIP():
    # Instanciamos las clases necesarias para ejecutar la lógica
    descompresor = Des.Descomprimir()
    mover_archivos = MA.MoverArchivos()
    limpieza = LIMP.Limpieza()
    # Ejecutamos el metodo descomprimir el objeto descompresor
    descompresor.descomprimir()

    # Ejecutamos el metodo mover_archivos_csv del objeto mover_archivos
    print("Moviendo archivos...")
    mover_archivos.mover_archivos_csv()

    # Ejecutamos el metodo limpieza_de_directorio del objeto limpieza
    print("Limpiando directorio...")
    limpieza.limpieza_de_directorio()

    # Eliminamos las instancias para liberar memoria
    del descompresor, mover_archivos, limpieza


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


def generarPrimerReporte(
    lista_completa: list,
    lista_catamarca: list,
    carpeta_destino="Resultados",
    nombre_archivo="Primer_reporte.csv",
):
    Ap = AP.AnalisisAplicaciones(lista_completa, lista_catamarca)
    total_general = Ap.total_aplicaciones()
    total_catamarca = Ap.total_aplicaciones_catamarca()
    total_departamento = Ap.total_aplicaciones_por_departamento()
    with open(
        f"{carpeta_destino}/{nombre_archivo}", "w", encoding="latin-1", newline=""
    ) as csvfile:
        csvfile.write(f"Total de vacunas aplicadas en general;{total_general}")
        csvfile.write("\n")
        csvfile.write(
            f"Total de vacunas aplicadas a la población de Catamarca (Provincia de domicilio = Catamarca);{total_catamarca}"
        )
        csvfile.write("\n")
        csvfile.write("\n\n")
        csvfile.write("Departamento;Aplicaciones")
        csvfile.write("\n")
        for key, value in total_departamento.items():
            csvfile.write(f"{key};{value}")
            csvfile.write("\n")

        csvfile.write("\n")
        csvfile.write(creditos())

    print("Reporte generado correctamente.")
    print(f"El archivo se encuentra en {carpeta_destino} y se llama {nombre_archivo}")


def generarSegundoReporte(
    lista_completa: list,
    lista_catamarca: list,
    carpeta_destino="Resultados",
    nombre_archivo="Segundo_reporte.csv",
):
    Ap = AP.AnalisisAplicaciones(lista_completa, lista_catamarca)

    total_general = Ap.total_aplicaciones_por_vacuna()
    total_catamarca = Ap.total_aplicaciones_por_vacuna_catamarca()
    with open(
        f"{carpeta_destino}/{nombre_archivo}", "w", encoding="latin-1", newline=""
    ) as csvfile:
        csvfile.write("Total General")
        csvfile.write("\n")
        csvfile.write("Vacuna;Cantidad")
        csvfile.write("\n")
        for key, value in total_general.items():
            csvfile.write(f"{key};{value}")
            csvfile.write("\n")

        csvfile.write("\n")
        csvfile.write("\n")

        csvfile.write("Total Catamarca")
        csvfile.write("\n")
        csvfile.write("Vacuna;Cantidad")
        csvfile.write("\n")
        for key, value in total_catamarca.items():
            csvfile.write(f"{key};{value}")
            csvfile.write("\n")

        csvfile.write("\n")
        csvfile.write(creditos())


def generarTercerReporte(
    lista_completa: list,
    lista_catamarca: list,
    carpeta_destino="Resultados",
    nombre_archivo="Tercer_reporte.csv",
):
    Ap = AP.AnalisisAplicaciones(lista_completa, lista_catamarca)
    Ar = AR.AnalisisRefuerzo(lista_completa, lista_catamarca)

    # Esquemas completos
    lista_completa_primera, lista_catamarca_primera = Ap.filtrar_primera_dosis()
    lista_completa_segunda, lista_catamarca_segunda = Ap.filtrar_segunda_dosis()
    lista_completa_unica, lista_catamarca_unica = Ap.filtrar_dosis_unica()
    lista_completa_adicional, lista_catamarca_adicional = Ap.filtrar_dosis_adicional()

    # Refuerzos

    refuerzos_completa = Ar.calcular_completa()
    refuerzos_catamarca = Ar.calcular_catamarca()

    with open(
        f"{carpeta_destino}/{nombre_archivo}", "w", encoding="latin-1", newline=""
    ) as csvfile:
        csvfile.write("Tipo y Cantidad de Dosis Aplicadas en General")
        csvfile.write("\n")
        csvfile.write("\n")
        csvfile.write(f"Primera dosis;{len(lista_completa_primera)}")
        csvfile.write("\n")
        csvfile.write(f"Segunda dosis;{len(lista_completa_segunda)}")
        csvfile.write("\n")
        csvfile.write(f"Dosis Unica;{len(lista_completa_unica)}")
        csvfile.write("\n")
        csvfile.write(f"Dosis Adicional;{len(lista_completa_adicional)}")
        csvfile.write("\n")
        csvfile.write(f"Primer Refuerzo;{refuerzos_completa[0]}")
        csvfile.write("\n")
        csvfile.write(f"Segundo Refuerzo;{refuerzos_completa[1]}")
        csvfile.write("\n")
        csvfile.write(f"Tercer Refuerzo;{refuerzos_completa[2]}")
        csvfile.write("\n")
        csvfile.write(f"Cuarto Refuerzo;{refuerzos_completa[3]}")
        csvfile.write("\n")
        csvfile.write(f"Quinto Refuerzo;{refuerzos_completa[4]}")
        csvfile.write("\n")
        csvfile.write(f"Sexto Refuerzo;{refuerzos_completa[5]}")
        csvfile.write("\n")
        csvfile.write(f"Extras;{refuerzos_completa[6]}")
        csvfile.write("\n")
        csvfile.write("\n")

        csvfile.write("Tipo y Cantidad de Dosis Aplicadas en Catamarca")
        csvfile.write("\n")
        csvfile.write("\n")
        csvfile.write(f"Primera dosis;{len(lista_catamarca_primera)}")
        csvfile.write("\n")
        csvfile.write(f"Segunda dosis;{len(lista_catamarca_segunda)}")
        csvfile.write("\n")
        csvfile.write(f"Dosis Unica;{len(lista_catamarca_unica)}")
        csvfile.write("\n")
        csvfile.write(f"Dosis Adicional;{len(lista_catamarca_adicional)}")
        csvfile.write("\n")
        csvfile.write(f"Primer Refuerzo;{refuerzos_catamarca[0]}")
        csvfile.write("\n")
        csvfile.write(f"Segundo Refuerzo;{refuerzos_catamarca[1]}")
        csvfile.write("\n")
        csvfile.write(f"Tercer Refuerzo;{refuerzos_catamarca[2]}")
        csvfile.write("\n")
        csvfile.write(f"Cuarto Refuerzo;{refuerzos_catamarca[3]}")
        csvfile.write("\n")
        csvfile.write(f"Quinto Refuerzo;{refuerzos_catamarca[4]}")
        csvfile.write("\n")
        csvfile.write(f"Sexto Refuerzo;{refuerzos_catamarca[5]}")
        csvfile.write("\n")
        csvfile.write(f"Extras;{refuerzos_catamarca[6]}")
        csvfile.write("\n")
        csvfile.write("\n")

        csvfile.write(creditos())
