import datetime


class GenerarReporte:
    def __init__(self, aplicaciones, refuerzos):
        self.analisis_aplicaciones = aplicaciones
        self.analisis_refuerzo = refuerzos

    def generar_reporte_de_dosis_aplicadas_y_refuerzos(
        self, nombre_reporte=f"Reporte_general_{datetime.date.today()}"
    ):
        # Se obtiene los datos pertinentes

        # Modulo AnalisisAplicaciones
        primera_dosis = len(self.analisis_aplicaciones.filtrar_primera_dosis())
        segunda_dosis = len(self.analisis_aplicaciones.filtrar_segunda_dosis())
        unica_dosis = len(self.analisis_aplicaciones.filtrar_dosis_unica())
        dosis_adicional = len(self.analisis_aplicaciones.filtrar_dosis_adicional())
        total_aplicaciones = self.analisis_aplicaciones.total_aplicaciones()

        # Modulo AnalisisRefuerzos
        (
            primer,
            segundo,
            tercer,
            cuarto,
            quinto,
            sexto,
            extra,
        ) = self.analisis_refuerzo.calcular()
        total_refuerzos = self.analisis_refuerzo.total_refuerzos()
        refuerzos_por_vacuna = self.analisis_refuerzo.refuerzos_por_vacuna()

        with open(f"{nombre_reporte}.csv", "w", encoding="utf-8") as csvfile:
            csvfile.write(
                f'Fecha de corte: {str(input("Ingrese fecha de corte de las bases de datos: "))}\n\n'
            )
            print("Exportando cantidad de refuerzo por vacuna...")

            csvfile.write("Cantidad de refuerzos aplicados por Vacuna\n\n")
            for key, value in refuerzos_por_vacuna.items():
                csvfile.write(f"{key};{value}\n")

            csvfile.write("\n\nResumen de tipo y cantidad de dosis aplicadas\n\n")
            print("Exportando primera dosis...")
            csvfile.write(f"Primera dosis;{primera_dosis}\n")

            print("Exportando segunda dosis...")
            csvfile.write(f"Segunda dosis;{segunda_dosis}\n")

            print("Exportando dosis unicas...")
            csvfile.write(f"Unica dosis;{unica_dosis}\n")

            print("Exportando dosis adicionales...")
            csvfile.write(f"Dosis Adicional;{dosis_adicional}\n")

            print("Exportando refuerzos...")
            csvfile.write("\n\nTipo y cantidad de refuerzos aplicados\n\n")
            csvfile.write(f"Primer refuerzo;{primer}\n")
            csvfile.write(f"Segundo refuerzo;{segundo}\n")
            csvfile.write(f"Tercer refuerzo;{tercer}\n")
            csvfile.write(f"Cuarto refuerzo;{cuarto}\n")
            csvfile.write(f"Quinto refuerzo;{quinto}\n")
            csvfile.write(f"Sexto refuerzo;{sexto}\n")
            csvfile.write(f"Extra;{extra}\n")

            print("Exportando resumen de aplicaciones...")
            csvfile.write("\nResumen de aplicaciones\n\n")
            csvfile.write(f"Total de Aplicaciones;{total_aplicaciones}\n")
            csvfile.write(f"Total de Refuerzos;{total_refuerzos}\n")

            csvfile.write(
                f"\n\nFecha y hora de generación de reporte: {datetime.datetime.now()}"
            )
            csvfile.write("\n\n\nScript creado por Closas Aguero Axel.")
