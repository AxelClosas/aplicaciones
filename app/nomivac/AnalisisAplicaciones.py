import app.FuncionesLogicaCSV as FL


# [1,2,3,4,5,6]
# ["axel" => "closas" ]
class AnalisisAplicaciones:
    def __init__(
        self, lista_de_vacunas_comFLeta: list, lista_de_vacunas_catamarca: list
    ):
        self.lista_de_vacunas_comFLeta = lista_de_vacunas_comFLeta
        self.lista_de_vacunas_catamarca = lista_de_vacunas_catamarca

    def total_aplicaciones(self) -> int:
        return len(self.lista_de_vacunas_comFLeta)

    def total_aplicaciones_catamarca(self) -> int:
        return len(self.lista_de_vacunas_catamarca)

    def total_aplicaciones_por_departamento(self) -> dict:
        deptos = FL.obtener_id_departamentos_desde_archivo()
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
        return resultado

    def total_aplicaciones_por_vacuna(self) -> dict:
        frecuencia = {}
        for item in self.lista_de_vacunas_comFLeta:
            if item["VACUNA"] in frecuencia.keys():
                frecuencia[item["VACUNA"]] += 1
            else:
                frecuencia[item["VACUNA"]] = 1
        return frecuencia

    def total_aplicaciones_por_vacuna_catamarca(self) -> dict:
        frecuencia = {}
        for item in self.lista_de_vacunas_catamarca:
            if item["VACUNA"] in frecuencia.keys():
                frecuencia[item["VACUNA"]] += 1
            else:
                frecuencia[item["VACUNA"]] = 1
        return frecuencia

    def filtrar_primera_dosis(self) -> list:
        filtro_primera_comFLeta = []
        filtro_primera_catamarca = []

        filtro_primera_comFLeta.extend(
            list(
                filter(
                    lambda item: "1ra" in item["NOMBRE_DOSIS"],
                    self.lista_de_vacunas_comFLeta,
                )
            )
        )

        filtro_primera_catamarca.extend(
            list(
                filter(
                    lambda item: "1ra" in item["NOMBRE_DOSIS"],
                    self.lista_de_vacunas_catamarca,
                )
            )
        )

        return filtro_primera_comFLeta, filtro_primera_catamarca

    def filtrar_segunda_dosis(self) -> list:
        filtro_segunda_comFLeta = []
        filtro_segunda_catamarca = []

        filtro_segunda_comFLeta.extend(
            list(
                filter(
                    lambda item: "2da" in item["NOMBRE_DOSIS"],
                    self.lista_de_vacunas_comFLeta,
                )
            )
        )
        filtro_segunda_catamarca.extend(
            list(
                filter(
                    lambda item: "2da" in item["NOMBRE_DOSIS"],
                    self.lista_de_vacunas_catamarca,
                )
            )
        )
        return filtro_segunda_comFLeta, filtro_segunda_catamarca

    def filtrar_dosis_unica(self) -> list:
        filtro_unica_comFLeta = []
        filtro_unica_catamarca = []

        filtro_unica_comFLeta.extend(
            list(
                filter(
                    lambda item: "Unica" in item["NOMBRE_DOSIS"],
                    self.lista_de_vacunas_comFLeta,
                )
            )
        )

        filtro_unica_catamarca.extend(
            list(
                filter(
                    lambda item: "Unica" in item["NOMBRE_DOSIS"],
                    self.lista_de_vacunas_catamarca,
                )
            )
        )
        return filtro_unica_comFLeta, filtro_unica_catamarca

    def filtrar_dosis_adicional(self) -> list:
        filtro_adicional_comFLeta = []
        filtro_adicional_catamarca = []

        filtro_adicional_comFLeta.extend(
            list(
                filter(
                    lambda item: "Adicional" in item["NOMBRE_DOSIS"],
                    self.lista_de_vacunas_comFLeta,
                )
            )
        )

        filtro_adicional_catamarca.extend(
            list(
                filter(
                    lambda item: "Adicional" in item["NOMBRE_DOSIS"],
                    self.lista_de_vacunas_catamarca,
                )
            )
        )
        return filtro_adicional_comFLeta, filtro_adicional_catamarca
