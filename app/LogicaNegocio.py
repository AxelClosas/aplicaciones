import app.ProcesosLogica as PL
import app.Aplicaciones as APL
import app.Descomprimir as Des
import app.ProcesarDatosDeCatamarca as PDC
import os
import app.AnalisisAplicaciones as AP
import app.AnalisisRefuerzo as AR


def creditos():
    return "Programa creado por: Axel Closas Agüero"


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
