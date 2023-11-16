import app.ProcesosLogica as PL
import csv


# [1,2,3,4,5,6]
# ["axel" => "closas" ]
class AnalisisAplicaciones:
    def __init__(self, lista_de_vacunas_completa, lista_de_vacunas_catamarca):
        self.lista_de_vacunas_completa = lista_de_vacunas_completa
        self.lista_de_vacunas_catamarca = lista_de_vacunas_catamarca

    def total_aplicaciones(self) -> int:
        return len(self.lista_de_vacunas_completa)

    def total_aplicaciones_catamarca(self) -> int:
        return len(self.lista_de_vacunas_catamarca)

    def total_aplicaciones_por_departamento_csv(
        self,
        nombre_archivo="aplicaciones_por_id_depto.csv",
        carpeta_destino="Resultados",
    ) -> csv:
        deptos = PL.obtener_id_departamentos_desde_archivo()
        frecuencia = {}
        resultado = {}
        print("Analizando aplicaciones por id de departamento...")
        for item in self.lista_de_vacunas_catamarca:
            if int(item["ID_DEPTO_DOMICILIO"]) in frecuencia.keys():
                frecuencia[int(item["ID_DEPTO_DOMICILIO"])] += 1
            else:
                frecuencia[int(item["ID_DEPTO_DOMICILIO"])] = 1

        resultado = {
            deptos[key]: frecuencia[key]
            for key in frecuencia.keys()
            if key in deptos.keys()
        }

        if frecuencia and resultado:
            with open(
                f"{carpeta_destino}/{nombre_archivo}", "w", encoding="latin-1"
            ) as csvfile:
                csvfile.write("Provincia;Cantidad\n")
                for key, value in resultado.items():
                    csvfile.write(f"{key};{value}\n")

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
