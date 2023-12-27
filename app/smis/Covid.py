class Covid:
    def __init__(self, movimientos: list):
        # Al instanciar la clase Covid, recibimos los movimientos para procesarlos luego
        self.movimientos = movimientos

    # Declaramos la función cambiar_nombre para recorrer item por item e ir estandarizando los nombres

    # Procesamos los datos para obtener los movimientos estandarizados y solamente de vacunas
    def procesar_datos(self) -> list:
        def cambiar_nombre(item) -> dict:
            cambiar_nombre = {
                "Astrazeneca": [
                    "COVID 19 VACCINE ASTRAZENECA (CHADOX1-S RECOMBINANTE) - Vial 10 DOSIS - WUXI - UNIVERSAL",
                    "COVID 19 VACCINE ASTRAZENECA (CHADOX1-S RECOMBINANTE) - Vial 10 DOSIS - LIOM",
                    "COVID 19 VACCINE ASTRAZENECA (CHADOX1-S RECOMBINANTE) - Vial 10 DOSIS - MABX- BIO- AMY",
                    "COVID 19 VACCINE ASTRAZENECA (CHADOX1-S RECOMBINANTE) - Vial 8 DOSIS - AB - PHARM",
                    "COVID 19 VACCINE ASTRAZENECA (CHADOX1-S RECOMBINANTE) - Vial 10 DOSIS - SKB CAT",
                    "COVID 19 VACCINE ASTRAZENECA (CHADOX1-S RECOMBINANTE) - Vial 10 DOSIS - AZ - AMYLIN - AZ CAN",
                    "COVID 19 VACCINE ASTRAZENECA (CHADOX1-S RECOMBINANTE) - Vial 10 DOSIS - BV",
                    "COVID 19 VACCINE ASTRAZENECA (CHADOX1-S RECOMBINANTE) - Vial 10 DOSIS - SKBIOSCIENCE - KOREA",
                ],
                "Covishield": [
                    "CHADOX1 NCOV-19 RECOMBINANTE - Vial 10 DOSIS - SERUM",
                ],
                "Sputnik V": [
                    "GAM-COVID-VAC C1 - Vial 5 DOSIS - RICHMOND",
                    "GAM-COVID-VAC C1 - Vial 2 DOSIS - BIOCAD-PHARM-UFAVITA",
                    "GAM-COVID-VAC C1 - Vial 5 DOSIS - JSC R-PHARM",
                    "GAM-COVID-VAC C1 - Vial 5 DOSIS - JSC BIOCAD",
                    "GAM-COVID-VAC C1 - Vial 5 DOSIS - JSC GENERIUM",
                    "GAM-COVID-VAC C1 - Vial 5 DOSIS - CJSC LEKKO",
                    "GAM-COVID-VAC C1 - Vial 1 DOSIS - PHARMSTANDARD-UFAVITA",
                    "GAM-COVID-VAC C2 - Vial 5 DOSIS - RICHMOND",
                    "GAM-COVID-VAC C2 - Vial 2 DOSIS - GENERIUM-PHARM-UFAVITA",
                    "GAM-COVID-VAC C2 - Vial 5 DOSIS - JSC BIOCAD",
                    "GAM-COVID-VAC C2 - Vial 1 DOSIS - PHARMSTANDARD-UFAVITA",
                    "GAM-COVID-VAC C2 - Vial 5 DOSIS - JSC GENERIUM",
                    "GAM-COVID-VAC C2 - Vial 5 DOSIS - CJSC LEKKO",
                    "GAM-COVID-VAC C2 - Vial 1 DOSIS - JSC BINNOPHARM",
                ],
                "Sputnik Light": [
                    "SPUTNIK LIGHT SOLUCIÓN INYECTABLE (0,5 ML) - Vial 1 DOSIS - MED GAMALEYA"
                ],
                "Sinopharm": [
                    "SARS-COV-2-VACCINE - Vial 1 DOSIS - BEIJING INSTITUTE",
                    "SARS-COV-2-VACCINE - Vial 2 DOSIS - BEIJING INSTITUTE",
                ],
                "Cansino": [
                    "CONVIDECIA RECOMBINANT NOVEL VACCINE - Vial 1 DOSIS - CANSINO",
                    "CONVIDECIA RECOMBINANT NOVEL VACCINE - Vial 3 DOSIS - CANSINO",
                ],
                "Moderna": [
                    "MODERNA COVID-19 (MRNA1273) DISPERSION INYECTABLE (0,2 MG/ML) - Vial 10 DOSIS - MOD - CAT",
                    "MODERNA COVID-19 (MRNA1273) DISPERSION INYECTABLE (0,2 MG/ML) - Vial 14 DOSIS - LON-BAX PHARM",
                    "MODERNA COVID-19 (MRNA1273) DISPERSION INYECTABLE (0,2 MG/ML) - Vial 14 DOSIS - MOD - CAT",
                    "MODERNA COVID-19 (MRNA1273) DISPERSION INYECTABLE (0,2 MG/ML) - Vial 14 DOSIS - MOD-BAX PHARM",
                ],
                "Moderna Pediatrica": [
                    "MODERNA Pediátrica COVID-19 (MRNA1273) DISPERSION INYECTABLE (0,1 MG/ML) - Vial 10 DOSIS - CAT - MOD",
                    "MODERNA Pediátrica COVID-19 (MRNA1273) DISPERSION INYECTABLE (0,1 MG/ML) - Vial 10 DOSIS - ROV - MOD",
                ],
                "Moderna Bivariante": [
                    "MODERNA BIVALENTE Original/Omicron COVID-19 (MRNA1273) DISPERSION INYECTABLE (0,1 MG/ML) - Vial 5 DOSIS - MOD - CAT",
                    "MODERNA BIVALENTE Original/Omicron COVID-19 (MRNA1273) DISPERSION INYECTABLE (0,1 MG/ML) - Vial 5 DOSIS - LON - ROV",
                ],
                "Pfizer": [
                    "COVID-19 MRNA VACCINE BNT162B2 POLVO PARA INYECTABLE (30 MCG/DOSIS) - Vial 6 DOSIS - BIONTECH",
                    "COVID-19 MRNA VACCINE BNT162B2 POLVO PARA INYECTABLE (30 MCG/DOSIS) - Vial 6 DOSIS - PFIZER",
                ],
                "Pfizer Pediatrica": [
                    "COVID-19 MRNA VACCINE BNT162B2 PEDIATRICA POLVO PARA INYECTABLE (10 MCG/DOSIS) - Vial 10 DOSIS - PFIZER"
                ],
                "Pfizer Bivariante": [
                    "COVID-19 MRNA BNT162B2 BIVALENTE Original/Omicron DISPERSION INYECTABLE (30 MCG/DOSIS) - Vial 6 DOSIS - BIONTECH",
                    "COVID-19 MRNA BNT162B2 BIVALENTE Original/Omicron DISPERSION INYECTABLE (30 MCG/DOSIS) - Vial 6 DOSIS - PFIZER",
                ],
            }

            for nombre, nombres_variables in cambiar_nombre.items():
                for nombre_variable in nombres_variables:
                    if nombre_variable in item["Producto origen"]:
                        item["Producto origen"] = nombre
            return item

        # Declaramos la función obtener_vacunas para filtrar unicamente las vacunas
        def obtener_vacunas(item) -> dict:
            vacunas = [
                "Astrazeneca",
                "Covishield",
                "Sputnik V",
                "Sputnik Light",
                "Sinopharm",
                "Cansino",
                "Moderna",
                "Moderna Pediatrica",
                "Moderna Bivariante",
                "Pfizer",
                "Pfizer Pediatrica",
                "Pfizer Bivariante",
            ]
            for vacuna in vacunas:
                if vacuna in item["Producto origen"]:
                    return item

        # Mapeamos la lista de movimientos inicializada para dar origen a una nueva lista estandarizada
        nueva_lista_vacunas = list(map(cambiar_nombre, self.movimientos))

        # Filtramos la nueva lista para extraer unicamente las vacunas
        movimientos_vacunas = list(filter(obtener_vacunas, nueva_lista_vacunas))

        # Retornamos los movimientos de vacunas unicamente
        return movimientos_vacunas

    # Declaramos la función retornar_movimientos_regulares
    def retornar_movimientos_regulares(self) -> list:
        # Obtenemos los movimientos de vacunas
        movimientos = self.procesar_datos()
        # Retornamos una lista de movimientos regulares
        return list(
            filter(lambda item: item["Tipo movimiento"] == "Regular", movimientos)
        )

    # Declaramos la función retornar_movimientos_internos
    def retornar_movimientos_internos(self):
        # Obtenemos los movimientos de vacunas
        movimientos = self.procesar_datos()
        # Retornamos una lista de movimientos regulares
        return list(
            filter(lambda item: item["Tipo movimiento"] == "Interno", movimientos)
        )
