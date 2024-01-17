import app.nomivac.AnalisisAplicaciones as AP
import app.nomivac.AnalisisRefuerzo as AR
from app.smis.LogicaAnalisisDeDistribucion import (
    proceso_filtrar_origen_paicatamarca_a_instituciones_covid,
    proceso_filtrar_origen_paicatamarca_a_instituciones_dicei,
)
import csv
from app.nomivac.Filtro import Filtro
import app.FuncionesLogicaCSV as FL

from app.Configuraciones import (
    creditos,
    nombre_carpeta_csv_smis,
    nombre_archivo_csv_smis,
)

from app.nomivac.Filtro import Filtro
from app.nomivac.LogicaAnalisisNomivac import (
    proceso_obtener_esquema_completo_y_refuerzos_ultimos_6_meses_por_departamento_y_rango_etario,
)


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


# Necesita ser refactorizado
def generarSegundoReporte(
    lista_completa: list,
    lista_catamarca: list,
    carpeta_destino="Resultados",
    nombre_archivo="Segundo_reporte.csv",
):
    Ap = AP.AnalisisAplicaciones(lista_completa, lista_catamarca)
    resultado_distribuidas = proceso_filtrar_origen_paicatamarca_a_instituciones_covid()

    resultado_aplicaciones_por_departamento = Ap.total_aplicaciones_por_vacuna_y_por_departamento_en_un_rango_de_fecha_determinado(
        "01/01/2023", "31/12/2023"
    )

    with open(
        f"{carpeta_destino}/{nombre_archivo}", "w", encoding="latin-1", newline=""
    ) as csvfile:
        reporte = csv.writer(csvfile, delimiter=";")
        reporte.writerow(["Departamento", "Vacunas", "Cantidad"])
        for depto in resultado_aplicaciones_por_departamento:
            for vacuna, cantidad in depto["Aplicaciones"].items():
                reporte.writerow([depto["DEPTO_ESTABLECIMIENTO"], vacuna, cantidad])

        reporte.writerow(["\n", "\n", "\n"])

        reporte.writerow(["Institución", "Vacuna", "Cantidad"])

        for depto_dist in resultado_distribuidas:
            for vacuna, cantidad in depto_dist["Vacunas"].items():
                # print(vacuna, cantidad)
                reporte.writerow([depto_dist["Institución destino"], vacuna, cantidad])


def generarTercerReporte(
    lista_completa: list,
    lista_catamarca: list,
    carpeta_destino="Resultados",
    nombre_archivo="Tercer_reporte.csv",
):
    Ap = AP.AnalisisAplicaciones(lista_completa, lista_catamarca)
    Ar = AR.AnalisisRefuerzo(lista_completa, lista_catamarca)
    filtrar = Filtro()
    lista_completa_primera = filtrar.filtrar_primera_dosis(lista_completa)
    lista_completa_segunda = filtrar.filtrar_segunda_dosis(lista_completa)
    lista_completa_unica = filtrar.filtrar_dosis_unica(lista_completa)
    lista_completa_adicional = filtrar.filtrar_dosis_adicional(lista_completa)

    lista_catamarca_primera = filtrar.filtrar_primera_dosis(lista_catamarca)
    lista_catamarca_segunda = filtrar.filtrar_segunda_dosis(lista_catamarca)
    lista_catamarca_unica = filtrar.filtrar_dosis_unica(lista_catamarca)
    lista_catamarca_adicional = filtrar.filtrar_dosis_adicional(lista_catamarca)

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


def generarCuartoReporte(
    carpeta_destino="Resultados",
    nombre_archivo="Cuarto_reporte.csv",
):
    with open(
        f"{carpeta_destino}/{nombre_archivo}", "w", encoding="latin-1", newline=""
    ) as csvfile:
        resultado_distribuidas = (
            proceso_filtrar_origen_paicatamarca_a_instituciones_dicei()
        )

        reporte = csv.writer(csvfile, delimiter=";")
        reporte.writerow(["Institución", "Vacuna", "Cantidad"])

        for depto_dist in resultado_distribuidas:
            for vacuna, cantidad in depto_dist["Vacunas"].items():
                # print(vacuna, cantidad)
                reporte.writerow([depto_dist["Institución destino"], vacuna, cantidad])


def generarQuintoReporte(
    lista_de_vacunas_completa,
    carpeta_destino="Resultados",
    nombre_archivo="Quinto_reporte.csv",
):
    with open(
        f"{carpeta_destino}/{nombre_archivo}", "w", encoding="latin-1", newline=""
    ) as csvfile:
        estructura = proceso_obtener_esquema_completo_y_refuerzos_ultimos_6_meses_por_departamento_y_rango_etario(
            lista_de_vacunas_completa
        )

        reporte = csv.writer(csvfile, delimiter=";")
        reporte.writerow(
            [
                "",
                "0 a 2",
                "",
                "",
                "3 a 11",
                "",
                "",
                "12 a 17",
                "",
                "",
                "18 a 49",
                "",
                "",
                "50 y más",
            ]
        )
        reporte.writerow(
            [
                "Departamento",
                "Esquema completo",
                "Refuerzos ultimos 6 meses",
                "Pendientes",
                "Esquema completo",
                "Refuerzos ultimos 6 meses",
                "Pendientes",
                "Esquema completo",
                "Refuerzos ultimos 6 meses",
                "Pendientes",
                "Esquema completo",
                "Refuerzos ultimos 6 meses",
                "Pendientes",
                "Esquema completo",
                "Refuerzos ultimos 6 meses",
                "Pendientes",
            ]
        )
        for item in estructura:
            reporte.writerow(
                [
                    item["DEPTO_ESTABLECIMIENTO"],
                    # 0 a 2
                    item["ESQUEMA_COMPLETO"]["RANGO_ETARIO_0_A_2"],
                    item["REFUERZOS_ULTIMOS_6_MESES"]["RANGO_ETARIO_0_A_2"],
                    item["PENDIENTES"]["RANGO_ETARIO_0_A_2"],
                    # 3 a 11
                    item["ESQUEMA_COMPLETO"]["RANGO_ETARIO_3_A_11"],
                    item["REFUERZOS_ULTIMOS_6_MESES"]["RANGO_ETARIO_3_A_11"],
                    item["PENDIENTES"]["RANGO_ETARIO_3_A_11"],
                    # 12 a 17
                    item["ESQUEMA_COMPLETO"]["RANGO_ETARIO_12_A_17"],
                    item["REFUERZOS_ULTIMOS_6_MESES"]["RANGO_ETARIO_12_A_17"],
                    item["PENDIENTES"]["RANGO_ETARIO_12_A_17"],
                    # 18 a 49
                    item["ESQUEMA_COMPLETO"]["RANGO_ETARIO_18_A_49"],
                    item["REFUERZOS_ULTIMOS_6_MESES"]["RANGO_ETARIO_18_A_49"],
                    item["PENDIENTES"]["RANGO_ETARIO_18_A_49"],
                    # 50 y más
                    item["ESQUEMA_COMPLETO"]["RANGO_ETARIO_50_Y_MAS"],
                    item["REFUERZOS_ULTIMOS_6_MESES"]["RANGO_ETARIO_50_Y_MAS"],
                    item["PENDIENTES"]["RANGO_ETARIO_50_Y_MAS"],
                ]
            )
