from functools import reduce


class AnalisisDistribucion:
    def __init__(self, movimientos):
        self.distribuidas = movimientos

    def filtrar_institucion_origen(self, cod_institucion: int) -> list:
        return list(
            filter(
                lambda item: item["Código institución origen"] == cod_institucion,
                self.distribuidas,
            )
        )

    def filtrar_institucion_destino(self, cod_institucion: int) -> list:
        return list(
            filter(
                lambda item: item["Código institución destino"] == cod_institucion,
                self.distribuidas,
            )
        )

    def filtrar_por_fecha_entrega(
        self, movimientos: list, fecha_minima, fecha_maxima
    ) -> list:
        return list(
            filter(
                lambda item: fecha_minima <= item["Fecha entrega"] <= fecha_maxima,
                movimientos,
            )
        )

    def filtrar_vacuna(self, movimientos: list, vacuna: str) -> list:
        return list(filter(lambda item: item["Producto origen"] == vacuna, movimientos))

    def sumar(self, movimientos: list):
        cantidades = [int(item["Cantidad origen"]) for item in movimientos]
        return reduce(lambda x, y: x + y, cantidades)

    def retornar_cantidad(self, movimientos: list):
        return len(movimientos)

    def retornar_registro_nro_remito(self, nro_remito: str):
        registro = list(
            filter(lambda item: nro_remito in item["Nro. remito"], self.distribuidas)
        )
        return registro[0]

    def filtrar_lote_vacuna(self, movimientos: list, lote: str) -> list:
        return list(filter(lambda item: item["Lote origen"] == lote, movimientos))

    def obtener_el_total_distribuido_por_Vacuna_a_cada_institucion(
        self,
        movimientos: list,
    ) -> list:
        # vacuna_por_institucion = [
        #     {
        #         "Institución destino": "Vacunatorio Central",
        #         "Vacunas": {
        #             "Moderna": 400,
        #             "Sinopharm": 300,
        #         },
        #         "Total distribuido": Sumatoria de salidasd
        #     },
        #     {
        #         "Institución destino": "Sanidad Municipal",
        #         "Vacunas": {
        #             "Moderna": 400,
        #             "Sinopharm": 300,
        #         },
        #         "Total distribuido": Sumatoria de salidasd
        #     },
        #     {
        #         "Institución destino": "Villa Dolores",
        #         "Vacunas": {
        #             "Moderna": 400,
        #             "Sinopharm": 300,
        #         },
        #         "Total distribuido": Sumatoria de salidasd
        #     },
        # ]
        instituciones = {item["Institución destino"] for item in movimientos}
        vacunas_por_institucion = []
        for institucion in instituciones:
            vacunas_por_institucion.append(
                {"Institución destino": institucion, "Vacunas": {}}
            )

        for mov in movimientos:
            for item in vacunas_por_institucion:
                if mov["Institución destino"] == item["Institución destino"]:
                    item["Código institución destino"] = mov[
                        "Código institución destino"
                    ]
                    if mov["Producto origen"] in item["Vacunas"].keys():
                        item["Vacunas"][mov["Producto origen"]] += mov[
                            "Cantidad origen"
                        ]
                    else:
                        item["Vacunas"][mov["Producto origen"]] = mov["Cantidad origen"]

        for item in vacunas_por_institucion:
            item["Total distribuido"] = reduce(
                lambda x, y: x + y, list(item["Vacunas"].values())
            )
        vacunas_por_institucion.append(
            {
                "Total distribuido": reduce(
                    lambda x, y: x + y,
                    [item["Total distribuido"] for item in vacunas_por_institucion],
                )
            }
        )

        return vacunas_por_institucion
