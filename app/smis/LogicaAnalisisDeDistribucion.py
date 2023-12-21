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
