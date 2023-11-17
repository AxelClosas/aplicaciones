class AnalisisRefuerzo:
    def __init__(
        self, lista_de_vacunas_completa: list, lista_de_vacunas_catamarca: list
    ):
        self.lista_de_vacunas_completa = lista_de_vacunas_completa
        self.lista_de_vacunas_catamarca = lista_de_vacunas_catamarca

    def filtrar_refuerzos(self) -> list:
        filtro_ref_completa = []
        filtro_ref_catamarca = []

        filtro_ref_completa.extend(
            list(
                filter(
                    lambda item: "Refuerzo" in item["NOMBRE_DOSIS"],
                    self.lista_de_vacunas_completa,
                )
            )
        )

        filtro_ref_catamarca.extend(
            list(
                filter(
                    lambda item: "Refuerzo" in item["NOMBRE_DOSIS"],
                    self.lista_de_vacunas_catamarca,
                )
            )
        )

        return filtro_ref_completa, filtro_ref_catamarca

    def frecuencia(self) -> dict:
        lista_completa, lista_catamarca = self.filtrar_refuerzos()
        frecuencia_completa = {}
        frecuencia_catamarca = {}

        for item in lista_completa:
            if item["NRO_DOC"].isnumeric():
                if int(item["NRO_DOC"]) in frecuencia_completa.keys():
                    frecuencia_completa[int(item["NRO_DOC"])] += 1
                else:
                    frecuencia_completa[int(item["NRO_DOC"])] = 1
            else:
                if item["NRO_DOC"] in frecuencia_completa.keys():
                    frecuencia_completa[item["NRO_DOC"]] += 1
                else:
                    frecuencia_completa[item["NRO_DOC"]] = 1

        for item in lista_catamarca:
            if item["NRO_DOC"].isnumeric():
                if int(item["NRO_DOC"]) in frecuencia_catamarca.keys():
                    frecuencia_catamarca[int(item["NRO_DOC"])] += 1
                else:
                    frecuencia_catamarca[int(item["NRO_DOC"])] = 1
            else:
                if item["NRO_DOC"] in frecuencia_catamarca.keys():
                    frecuencia_catamarca[item["NRO_DOC"]] += 1
                else:
                    frecuencia_catamarca[item["NRO_DOC"]] = 1

        return frecuencia_completa, frecuencia_catamarca

    # def refuerzos_por_vacuna(self, nombre="refuerzos_por_vacuna"):
    #     ref_vacuna = {}
    #     vacunas = self.filtrar_refuerzos()
    #     for item in vacunas:
    #         if item["VACUNA"] in ref_vacuna:
    #             ref_vacuna[item["VACUNA"]] += 1
    #         else:
    #             ref_vacuna[item["VACUNA"]] = 1
    #     return ref_vacuna

    # def total_refuerzos(self) -> int:
    #     refuerzos = self.filtrar_refuerzos()
    #     return len(refuerzos)

    def calcular_completa(self):
        frecuencia_completa, frecuencia_catamarca = self.frecuencia()
        del frecuencia_catamarca

        def func_frecuencia_completa(frecuencia_completa: list):
            primer_completa = 0
            segundo_completa = 0
            tercer_completa = 0
            cuarto_completa = 0
            quinto_completa = 0
            sexto_completa = 0
            extra_completa = 0
            for cantidad in frecuencia_completa.values():
                match cantidad:
                    case 1:
                        primer_completa += 1
                    case 2:
                        primer_completa += 1
                        segundo_completa += 1
                    case 3:
                        primer_completa += 1
                        segundo_completa += 1
                        tercer_completa += 1
                    case 4:
                        primer_completa += 1
                        segundo_completa += 1
                        tercer_completa += 1
                        cuarto_completa += 1
                    case 5:
                        primer_completa += 1
                        segundo_completa += 1
                        tercer_completa += 1
                        cuarto_completa += 1
                        quinto_completa += 1
                    case 6:
                        primer_completa += 1
                        segundo_completa += 1
                        tercer_completa += 1
                        cuarto_completa += 1
                        quinto_completa += 1
                        sexto_completa += 1
                    case _:
                        extra_completa += 1
            return (
                primer_completa,
                segundo_completa,
                tercer_completa,
                cuarto_completa,
                quinto_completa,
                sexto_completa,
                extra_completa,
            )

        return func_frecuencia_completa(frecuencia_completa)

    def calcular_catamarca(self):
        frecuencia_completa, frecuencia_catamarca = self.frecuencia()
        del frecuencia_completa

        def func_frecuencia_catamarca(frecuencia_catamarca: list):
            primer_catamarca = 0
            segundo_catamarca = 0
            tercer_catamarca = 0
            cuarto_catamarca = 0
            quinto_catamarca = 0
            sexto_catamarca = 0
            extra_catamarca = 0
            for cantidad in frecuencia_catamarca.values():
                match cantidad:
                    case 1:
                        primer_catamarca += 1
                    case 2:
                        primer_catamarca += 1
                        segundo_catamarca += 1
                    case 3:
                        primer_catamarca += 1
                        segundo_catamarca += 1
                        tercer_catamarca += 1
                    case 4:
                        primer_catamarca += 1
                        segundo_catamarca += 1
                        tercer_catamarca += 1
                        cuarto_catamarca += 1
                    case 5:
                        primer_catamarca += 1
                        segundo_catamarca += 1
                        tercer_catamarca += 1
                        cuarto_catamarca += 1
                        quinto_catamarca += 1
                    case 6:
                        primer_catamarca += 1
                        segundo_catamarca += 1
                        tercer_catamarca += 1
                        cuarto_catamarca += 1
                        quinto_catamarca += 1
                        sexto_catamarca += 1
                    case _:
                        extra_catamarca += 1
            return (
                primer_catamarca,
                segundo_catamarca,
                tercer_catamarca,
                cuarto_catamarca,
                quinto_catamarca,
                sexto_catamarca,
                extra_catamarca,
            )

        return func_frecuencia_catamarca(frecuencia_catamarca)

    # def obtener_refuerzos(self, nombre_archivo="ref_aplicados"):
    #     primer, segundo, tercer, cuarto, quinto, sexto, extra = self.calcular()
    #     total_refuerzos = self.total_refuerzos()

    #     print(f"Exportando archivo: {nombre_archivo}")
    #     with open(f"{nombre_archivo}.txt", "w", encoding="utf-8") as file:
    #         file.write(
    #             f"Actualización: {str(input('Ingresa la fecha de corte de las bases: '))}\n\nPrimer refuerzo: {primer}\nSegundo refuerzo: {segundo}\nTercer refuerzo: {tercer}\nCuarto refuerzo: {cuarto}\nQuinto refuerzo: {quinto}\nSexto refuerzo: {sexto}\nValores extras: {extra}\n\nTotal Refuerzos: {total_refuerzos}"
    #     )
