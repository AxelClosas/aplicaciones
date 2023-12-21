from app.Configuraciones import nombre_carpeta_csv_smis, nombre_archivo_csv_smis
import app.FuncionesLogicaCSV as FL
from datetime import date


class Distribucion:
    def __init__(self, nombre_carpeta_csv_smis: str, nombre_archivo_csv_smis: str):
        self.nombre_carpeta_csv_smis = nombre_carpeta_csv_smis
        self.nombre_archivo_csv_smis = nombre_archivo_csv_smis

    def obtener_datos(self):
        carpeta_csv_smis = FL.generar_ruta_carpeta_csv(self.nombre_carpeta_csv_smis)
        data = FL.read_csv(f"{carpeta_csv_smis}/{self.nombre_archivo_csv_smis}")
        return data

    def transformar_datos(self):
        def obtener(item):
            n_dict = {
                "Tipo movimiento": item["Tipo movimiento"],
                "Motivo movimiento interno": item["Motivo movimiento interno"],
                "Fecha entrega": item["Fecha entrega"],
                "Nro. remito": item["Nro. remito"],
                "Código institución origen": int(item["Código institución origen "]),
                "Institución origen": item["Institución origen"],
                "Depósito origen": item["Depósito origen"],
                "Código institución destino": int(item["Código institución destino"]),
                "Código depósito destino": int(item["Código depósito destino"]),
                "Institución destino": item["Institución destino"],
                "Depósito destino": item["Depósito destino"],
                "Programa sanitario": item["Programa sanitario"],
                "Producto origen": item["Producto origen"],
                "Lote origen": item["Lote origen"],
                "Fecha vto. origen": item["Fecha vto. origen"],
                "Cantidad origen": int(item["Cantidad origen"]),
            }
            return n_dict

        def cambiar_nombre(item):
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
                "Sputnik V - C1": [
                    "GAM-COVID-VAC C1 - Vial 5 DOSIS - RICHMOND",
                    "GAM-COVID-VAC C1 - Vial 2 DOSIS - BIOCAD-PHARM-UFAVITA",
                    "GAM-COVID-VAC C1 - Vial 5 DOSIS - JSC R-PHARM",
                    "GAM-COVID-VAC C1 - Vial 5 DOSIS - JSC BIOCAD",
                    "GAM-COVID-VAC C1 - Vial 5 DOSIS - JSC GENERIUM",
                    "GAM-COVID-VAC C1 - Vial 5 DOSIS - CJSC LEKKO",
                    "GAM-COVID-VAC C1 - Vial 1 DOSIS - PHARMSTANDARD-UFAVITA",
                ],
                "Sputnik V - C2": [
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

        def transformar_fecha_entrega(item):
            item_copia = item.copy()
            fecha_entrega = str(item_copia["Fecha entrega"])
            dia, mes, anio = fecha_entrega.split("/")
            dia, mes, anio = int(dia), int(mes), int(anio)

            item_copia["Fecha entrega"] = date(anio, mes, dia)
            return item_copia

        data = self.obtener_datos()
        datos_minimos = list(map(obtener, data))
        cambio_de_nombres_de_vacunas = list(map(cambiar_nombre, datos_minimos))
        nueva_data = list(map(transformar_fecha_entrega, cambio_de_nombres_de_vacunas))
        return nueva_data

    def obtener_vacunas(self):
        def obtener(item):
            vacunas = [
                "Astrazeneca",
                "Covishield",
                "Sputnik V - C1",
                "Sputnik V - C2",
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

        data = self.transformar_datos()
        data_vacunas = list(filter(obtener, data))
        return data_vacunas

    def retornar_movimientos_regulares(self):
        data = self.obtener_vacunas()
        return list(filter(lambda item: item["Tipo movimiento"] == "Regular", data))

    def retornar_movimientos_internos(self):
        data = self.obtener_vacunas()
        return list(filter(lambda item: item["Tipo movimiento"] == "Interno", data))


test = Distribucion(nombre_carpeta_csv_smis, nombre_archivo_csv_smis)
