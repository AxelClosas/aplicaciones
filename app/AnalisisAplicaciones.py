class AnalisisAplicaciones:
    def __init__(self, lista_de_vacunas):
        self.lista_de_vacunas = lista_de_vacunas

    def total_aplicaciones(self) -> int:
        return len(self.lista_de_vacunas)

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
