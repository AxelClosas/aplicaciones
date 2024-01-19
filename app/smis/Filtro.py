from datetime import datetime, date


class Filtro:
    def filtrar_por_rango_de_fechas(
        self, movimientos, fecha_minima: str, fecha_maxima: str
    ):
        """Devuelve una lista de movimientos

        Args:
            movimientos (List[dict]): Lista de movimientos
            fecha_minima (str): Fecha minima
            fecha_maxima (str): Fecha maxima


        Returns:
            Lista filtrada: Lista de movimientos filtrada
        """
        formato = "%d/%m/%Y"

        fecha_minima = datetime.strptime(fecha_minima, formato)
        fecha_maxima = datetime.strptime(fecha_maxima, formato)

        return list(
            filter(
                lambda item: fecha_minima
                <= datetime.strptime(item["Fecha entrega"], formato)
                <= fecha_maxima,
                movimientos,
            )
        )
