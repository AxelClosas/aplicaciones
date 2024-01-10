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
        """
        vacuna_por_institucion = [
            {
                "Institución destino": "Vacunatorio Central",
                "Vacunas": {
                    "Moderna": 400,
                    "Sinopharm": 300,
                },
                "Total distribuido": Sumatoria de salidasd
            },
            {
                "Institución destino": "Sanidad Municipal",
                "Vacunas": {
                    "Moderna": 400,
                    "Sinopharm": 300,
                },
                "Total distribuido": Sumatoria de salidasd
            },
            {
                "Institución destino": "Villa Dolores",
                "Vacunas": {
                    "Moderna": 400,
                    "Sinopharm": 300,
                },
            },
        ]
        """
        # Creo un conjunto (o set) con las instituciones involucradas en los movimientos para evitar duplicados
        instituciones = {item["Institución destino"] for item in movimientos}
        # vacunas_por_institucion será la lista que contendra los items de las distribuciones
        vacunas_por_institucion = []
        # Creamos la estructura
        """
        vacunas_por_institucion = [
            {
                "Institución destino": "Villa Dolores",
                "Vacunas": {},
            },
        ]
        """
        for institucion in instituciones:
            vacunas_por_institucion.append(
                {"Institución destino": institucion, "Vacunas": {}}
            )
        # Generamos los datos
        # Recorremos cada movimiento
        for mov in movimientos:
            # Recorremos cada item de distribución por cada movimiento
            for item in vacunas_por_institucion:
                # Si la institución destino del movimiento es igual a la institución destino del item
                if mov["Institución destino"] == item["Institución destino"]:
                    # Guardamos el código de institución generando una nueva llave
                    item["Código institución destino"] = mov[
                        "Código institución destino"
                    ]
                    # Si el producto del movimiento se encuentra en las llaves de las vacunas del item
                    if mov["Producto origen"] in item["Vacunas"].keys():
                        # Acumulamos la cantidad
                        item["Vacunas"][mov["Producto origen"]] += mov[
                            "Cantidad origen"
                        ]
                    # Caso contrario, guardamos el primer valor encontrado generando una nueva llave según sea el producto
                    else:
                        item["Vacunas"][mov["Producto origen"]] = mov["Cantidad origen"]

        return vacunas_por_institucion
