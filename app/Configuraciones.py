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
def retornar_diccionario_de_nombres_para_estandar_covid() -> dict:
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


def retornar_nombres_de_vacunas_covid() -> list:
    return [
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


diccionario_de_vacunas_covid = retornar_diccionario_de_nombres_para_estandar_covid()
lista_de_vacunas_covid = retornar_nombres_de_vacunas_covid()


# DiCEI
# Nombres variables de vacunas por laboratorios
def retornar_diccionario_de_nombres_para_estandar_dicei() -> dict:
    return {
        # Diccionario de vacunas con sus diferentes nombres según laboratorio para ser reemplazados
        "Antigripal Adulto Trivalente": [
            "ANTIGRIPAL ADULTO TRIVALENTE SOLUCIÓN INYECTABLE (0.5 ML) - Jeringa prellenada 1 DOSIS - LIA",
            "ANTIGRIPAL ADULTO TRIVALENTE SOLUCIÓN INYECTABLE (0.5 ML) - Jeringa prellenada 1 DOSIS - SINERGIUM BIOTECH",
        ],
        "Antigripal Adyuvantada  Adulto": [
            "ANTIGRIPAL ADYUVANTADA  ADULTO SOLUCIÓN INYECTABLE (0.5 ML) - Jeringa prellenada 1 DOSIS - SINERGIUM BIOTECH",
        ],
        "Antigripal Pediatrica Trivalente": [
            "ANTIGRIPAL PEDIATRICA TRIVALENTE SOLUCIÓN INYECTABLE (0.25 ML) - Jeringa prellenada 1 DOSIS - SINERGIUM BIOTECH",
        ],
        "Antineumococcica Conjugada (PNEUMO 13)": [
            "ANTINEUMOCOCCICA CONJUGADA (PNEUMO 13) SOLUCIÓN INYECTABLE (0.5 ML) - Jeringa prellenada 1 DOSIS - PFIZER ELEA",
            "ANTINEUMOCOCCICA CONJUGADA (PNEUMO 13) SOLUCIÓN INYECTABLE (0.5 ML) - Jeringas Prellenadas 1 DOSIS - PECC",
        ],
        "Antineumococcica Polisacarida (PNEUMO 23)": [
            "ANTINEUMOCOCCICA POLISACARIDA (PNEUMO 23) SUSPENSIÓN INYECTABLE (0.5 ML) - Vial 1 DOSIS - MSD",
        ],
        "HIB- Haemophilus Influenzae Tipo B": [
            "HIB- HAEMOPHILUS INFLUENZAE TIPO B POLVO PARA INYECTABLE (- ..) - Vial 1 DOSIS - SERUM"
        ],
        "Inmunoglobulina Antihepatitis B": [
            "INMUNOGLOBULINA ANTIHEPATITIS B SOLUCIÓN INYECTABLE (200/1 UI/ML) - Vial 1 DOSIS - GREEN CROSS",
            "INMUNOGLOBULINA ANTIHEPATITIS B SOLUCIÓN INYECTABLE (200/1 UI/ML) - Vial 1 DOSIS - KEDRION",
        ],
        "Inmunoglobulina Antirrabica Humana": [
            "INMUNOGLOBULINA ANTIRRABICA HUMANA POLVO PARA INYECTABLE (- ..) - Vial 1 DOSIS - KAMADA",
        ],
        "Inmunoglobulina Antitetanica": [
            "INMUNOGLOBULINA ANTITETANICA SOLUCIÓN INYECTABLE (250 UI/ML) - Jeringa prellenada 1 DOSIS - CSL BEHRING",
            "INMUNOGLOBULINA ANTITETANICA SOLUCIÓN INYECTABLE (250 UI/ML) - Vial 1 DOSIS - GREEN CROSS",
        ],
        "Inmunoglobulina Antivaricela Zoster": [
            "INMUNOGLOBULINA ANTIVARICELA ZOSTER SOLUCIÓN INYECTABLE (- ..) - Vial 1 DOSIS - GREEN CROSS"
        ],
        "Rotavirus": [
            "ROTAVIRUS - Jeringa prellenada 1 DOSIS - GSK",
        ],
        "Sextuple Acelular": [
            "SEXTUPLE ACELULAR - Frasco 1 DOSIS - SANOFI PASTEUR",
        ],
        "Antirrabica  Humana": [
            "VACUNA ANTIRRABICA  HUMANA POLVO PARA INYECTABLE (2,5 UI) - Vial 1 DOSIS - SERUM",
        ],
        "BCG": [
            "VACUNA BCG POLVO PARA INYECTABLE (- ..) - Vial 10 DOSIS - ajvaccines",
            "VACUNA BCG POLVO PARA INYECTABLE (- ..) - Vial 10 DOSIS - SERUM",
        ],
        "Doble Adulto Bacteriana DTA": [
            "VACUNA DOBLE ADULTO BACTERIANA DTA SOLUCIÓN INYECTABLE (0,5 ML) - Vial 10 DOSIS - SERUM",
        ],
        "Doble Viral": [
            "VACUNA DOBLE VIRAL POLVO PARA INYECTABLE (- ..) - Vial 10 DOSIS - SERUM",
        ],
        "Fiebre Amarilla": [
            "VACUNA FIEBRE AMARILLA POLVO PARA INYECTABLE (- ..) - Vial 10 DOSIS - FIOTEC",
            "VACUNA FIEBRE AMARILLA POLVO PARA INYECTABLE (- ..) - Vial 10 DOSIS - SANOFI PASTEUR",
        ],
        "Hepatitis A Adulto": [
            "VACUNA HEPATITIS A ADULTO SUSPENSIÓN INYECTABLE (50/1 UI/ML) - Vial 1 DOSIS - MSD",
        ],
        "Hepatitis A Pediatrica": [
            "VACUNA HEPATITIS A PEDIATRICA SUSPENSIÓN INYECTABLE (720/0.5 UI/ML) - Vial 1 DOSIS - GSK",
        ],
        "Hepatitis B Adulto": [
            "VACUNA HEPATITIS B ADULTO SOLUCIÓN INYECTABLE (- ..) - Vial 10 DOSIS - LG",
        ],
        "Hepatitis B Pediatrica": [
            "VACUNA HEPATITIS B PEDIATRICA SOLUCIÓN INYECTABLE (0,5 ML) - Vial 1 DOSIS - LG",
            "VACUNA HEPATITIS B PEDIATRICA SOLUCIÓN INYECTABLE (0,5 ML) - Vial 1 DOSIS - SERUM",
        ],
        "Meningococo Conjugada a,c,w-135": [
            "VACUNA MENINGOCOCO CONJUGADA A,C,W-135, Y SOLUCIÓN INYECTABLE (- ..) - Vial 1 DOSIS - GSK",
        ],
        "Pentavalente": [
            "VACUNA PENTAVALENTE SOLUCIÓN INYECTABLE (- ..) - Vial 1 DOSIS - SERUM",
        ],
        "Poliomelitica Inactivada": [
            "VACUNA POLIOMELITICA INACTIVADA SOLUCIÓN INYECTABLE (- ..) - Vial 5 DOSIS - Bilthoven Biologicals B.V",
        ],
        "Triple Bacteriana Acelular- DPTa": [
            "VACUNA TRIPLE BACTERIANA ACELULAR- DPTa SOLUCIÓN INYECTABLE (0,5 ML) - Frasco 1 DOSIS - SANOFI PASTEUR",
            "VACUNA TRIPLE BACTERIANA ACELULAR- DPTa SOLUCIÓN INYECTABLE (0,5 ML) - Vial 1 DOSIS - GSK",
        ],
        "Triple Bacteriana Celular- DPT": [
            "VACUNA TRIPLE BACTERIANA CELULAR- DPT SOLUCIÓN INYECTABLE (0,5 ML) - Vial 10 DOSIS - SERUM",
        ],
        "Triple Viral SRP": [
            "VACUNA TRIPLE VIRAL SRP POLVO PARA INYECTABLE (- ..) - Vial 1 DOSIS - GSK",
            "VACUNA TRIPLE VIRAL SRP POLVO PARA INYECTABLE (- ..) - Vial 1 DOSIS - MSD",
            "VACUNA TRIPLE VIRAL SRP POLVO PARA INYECTABLE (- ..) - Vial 10 DOSIS - FIOCRUZ",
        ],
        "Varicela": [
            "VACUNA VARICELA SOLUCIÓN INYECTABLE (- ..) - Vial 1 DOSIS - MSD",
        ],
        "VPH": [
            "VACUNA VPH SUSPENSIÓN INYECTABLE (- ..) - Jeringa prellenada 1 DOSIS - SINERGIUM BIOTECH",
        ],
    }


def retornar_nombres_de_vacunas_dicei() -> list:
    return [
        # Lista de vacunas, nombres estandarizados
        "Antigripal Adulto Trivalente",
        "Antigripal Adyuvantada  Adulto",
        "Antigripal Pediatrica Trivalente",
        "Antineumococcica Conjugada (PNEUMO 13)",
        "Antineumococcica Polisacarida (PNEUMO 23)",
        "HIB- Haemophilus Influenzae Tipo B",
        "Inmunoglobulina Antihepatitis B",
        "Inmunoglobulina Antirrabica Humana",
        "Inmunoglobulina Antitetanica",
        "Inmunoglobulina Antivaricela Zoster",
        "Rotavirus",
        "Sextuple Acelular",
        "Antirrabica  Humana",
        "BCG",
        "Doble Adulto Bacteriana DTA",
        "Doble Viral",
        "Fiebre Amarilla",
        "Hepatitis A Adulto",
        "Hepatitis A Pediatrica",
        "Hepatitis B Adulto",
        "Hepatitis B Pediatrica",
        "Meningococo Conjugada a,c,w-135",
        "Pentavalente",
        "Poliomelitica Inactivada",
        "Triple Bacteriana Acelular- DPTa",
        "Triple Bacteriana Celular- DPT",
        "Triple Viral SRP",
        "Varicela",
        "VPH",
    ]


diccionario_de_vacunas_dicei = retornar_diccionario_de_nombres_para_estandar_dicei()
lista_de_vacunas_dicei = retornar_nombres_de_vacunas_dicei()
