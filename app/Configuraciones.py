# Nombre de archivos en DocumentosClave
documentos_clave = "DocumentosClave"
archivo_id_departamentos = "id_departamentos.csv"

# Nombre de archivos en CSV
nombre_carpeta_csv_nomivac = "CSV_NOMIVAC"
nombre_carpeta_csv_smis = "CSV_SMIS"
nombre_archivo_csv_smis = "Base_SMIS.csv"
nombre_archivo_comprimido_principal = "CATAMARCA.zip"
nombre_archivo_base_completa = "BaseCompletaCOVID.csv"

# Variables para SMIS
cod_institucion_pai_catamarca = 12

# Programas sanitarios
programa_covid = "COVID"
programa_dicei = "DiCEI"
programa_epidemio = "Direccion de epidemiologia"


def creditos():
    return "Programa creado por: Axel Closas Agüero"


# COVID
# Nombres variables de vacunas por laboratorios
def retornar_diccionario_de_nombres_para_estandar() -> dict:
    return {
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


diccionario_de_vacunas = retornar_diccionario_de_nombres_para_estandar()
