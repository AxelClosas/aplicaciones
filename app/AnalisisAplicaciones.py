import app.ProcesosLogica as PL


class AnalisisAplicaciones:
    def __init__(self, path_base_covid_completa):
        self.lista_de_vacunas = PL.read_csv(path_base_covid_completa)

    def mostrar_lista_de_vacunas(self) -> list:
        return self.lista_de_vacunas

    def total_aplicaciones(self) -> int:
        return len(self.lista_de_vacunas)

    def total_aplicaciones_catamarca_domicilio(self) -> int:
        return len(self.filtrar_provincia_catamarca())

    def total_aplicaciones_por_departamento(self) -> dict:
        return self.filtrar_departamentos()

    def filtrar_departamentos(self) -> list:
        aplicaciones = self.filtrar_provincia_catamarca()
        ap_deptos_domicilio = set()
        ap_deptos_establecimiento = set()
        for aplicacion in aplicaciones:
            ap_deptos_establecimiento.add(aplicacion["DEPTO_ESTABLECIMIENTO"])
            ap_deptos_domicilio.add(aplicacion["DEPTO_DOMICILIO"])
        return ap_deptos_domicilio, ap_deptos_establecimiento

    def filtrar_provincia_catamarca(self) -> list:
        filtro = []
        filtro.extend(
            filter(
                lambda item: "Catamarca" in item["PROVINCIA_DOMICILIO"],
                self.lista_de_vacunas,
            )
        )
        return filtro

    def filtrar_primera_dosis(self) -> list:
        filtro_primera = []
        filtro_primera.extend(
            list(filter(lambda item: "1ra" in item["DOSIS"], self.lista_de_vacunas))
        )
        return filtro_primera

    def filtrar_segunda_dosis(self) -> list:
        filtro_segunda = []
        filtro_segunda.extend(
            list(filter(lambda item: "2da" in item["DOSIS"], self.lista_de_vacunas))
        )
        return filtro_segunda

    def filtrar_dosis_unica(self) -> list:
        filtro_unica = []
        filtro_unica.extend(
            list(filter(lambda item: "Unica" in item["DOSIS"], self.lista_de_vacunas))
        )
        return filtro_unica

    def filtrar_dosis_adicional(self) -> list:
        filtro_adicional = []
        filtro_adicional.extend(
            list(
                filter(lambda item: "Adicional" in item["DOSIS"], self.lista_de_vacunas)
            )
        )
        return filtro_adicional
