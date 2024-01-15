import app.FuncionesLogicaCSV as FL
from functools import reduce
from datetime import datetime, date


# [1,2,3,4,5,6]
# ["axel" => "closas" ]
class AnalisisAplicaciones:
    def __init__(
        self, lista_de_vacunas_completa: list, lista_de_vacunas_catamarca: list
    ):
        self.lista_de_vacunas_completa = lista_de_vacunas_completa
        self.lista_de_vacunas_catamarca = lista_de_vacunas_catamarca

    def total_aplicaciones(self) -> int:
        return len(self.lista_de_vacunas_completa)

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
        for item in self.lista_de_vacunas_completa:
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

    def total_aplicaciones_por_vacuna_y_por_departamento_en_un_rango_de_fecha_determinado(
        self, fecha_minima: str, fecha_maxima: str
    ) -> list:
        # Busco crear la siguiente estructura
        # [
        #     {
        #         "ID_DEPTO_DOMICILIO": 12,
        #         "Departamento": "Ambato",
        #         "Aplicaciones": {"Moderna": 4000, "Sinopharm": 3000},
        #         "Total de Aplicaciones": 7000,
        #     },
        #     {
        #         "ID_DEPTO_DOMICILIO": 12,
        #         "Departamento": "Valle Viejo",
        #         "Aplicaciones": {"Moderna": 4000, "Sinopharm": 3000},
        #         "Total de Aplicaciones": 7000,
        #     },
        # ]
        id_departamentos = FL.obtener_id_departamentos_desde_archivo()
        aplicaciones_departamentos_completa = [
            {
                "ID_DEPTO_ESTABLECIMIENTO": key,
                "DEPTO_ESTABLECIMIENTO": value,
                "Aplicaciones": {},
            }
            for key, value in id_departamentos.items()
        ]
        movimientos = self.filtrar_por_fecha_de_aplicacion(
            self.lista_de_vacunas_completa, fecha_minima, fecha_maxima
        )
        for item in movimientos:
            for depto in aplicaciones_departamentos_completa:
                if (
                    int(item["ID_DEPTO_ESTABLECIMIENTO"])
                    == depto["ID_DEPTO_ESTABLECIMIENTO"]
                ):
                    if item["VACUNA"] in depto["Aplicaciones"].keys():
                        depto["Aplicaciones"][item["VACUNA"]] += 1
                    else:
                        depto["Aplicaciones"][item["VACUNA"]] = 1

        # aplicaciones = [
        #     depto["Aplicaciones"].values()
        #     for depto in aplicaciones_departamentos_completa
        # ]
        # print(aplicaciones)

        return aplicaciones_departamentos_completa
