from datetime import datetime, date


class Filtro:
    def __init__(self, aplicaciones):
        self.aplicaciones = aplicaciones

    def filtrar_primera_dosis(self):
        """Devuelve una lista de las primeras dosis.

        Returns:
            Retorna una lista de diccionarios
        """
        filtro = []

        def filtrar_nombre_dosis(item: dict) -> dict:
            if "1ra" in item["NOMBRE_DOSIS"]:
                return item

        filtro.extend(list(filter(filtrar_nombre_dosis, self.aplicaciones)))

        return filtro

    def filtrar_segunda_dosis(self):
        """Devuelve una lista de las segundas dosis.

        Returns:
            Retorna una lista de diccionarios
        """
        filtro = []

        def filtrar_nombre_dosis(item: dict) -> dict:
            if "2da" in item["NOMBRE_DOSIS"]:
                return item

        filtro.extend(list(filter(filtrar_nombre_dosis, self.aplicaciones)))

        return filtro

    def filtrar_dosis_adicional(self):
        """Devuelve una lista de las dosis adicionales.

        Returns:
            Retorna una lista de diccionarios
        """
        filtro = []

        def filtrar_nombre_dosis(item: dict) -> dict:
            if "Adicional" in item["NOMBRE_DOSIS"]:
                return item

        filtro.extend(list(filter(filtrar_nombre_dosis, self.aplicaciones)))

        return filtro

    def filtrar_dosis_unica(self):
        """Devuelve una lista de las dosis unicas.

        Returns:
            Retorna una lista de diccionarios
        """
        filtro = []

        def filtrar_nombre_dosis(item: dict) -> dict:
            if "Unica" in item["NOMBRE_DOSIS"]:
                return item

        filtro.extend(list(filter(filtrar_nombre_dosis, self.aplicaciones)))

        return filtro

    def filtrar_refuerzos(self):
        """Devuelve una lista de las dosis de refuerzo.

        Returns:
            Retorna una lista de diccionarios
        """
        filtro = []

        def filtrar_nombre_dosis(item: dict) -> dict:
            if "Refuerzo" in item["NOMBRE_DOSIS"]:
                return item

        filtro.extend(list(filter(filtrar_nombre_dosis, self.aplicaciones)))

        return filtro

    def filtrar_por_fecha_de_aplicacion(self, fecha_minima: str, fecha_maxima: str):
        formato = "%d/%m/%Y"
        fecha_minima = datetime.strptime(fecha_minima, formato)
        fecha_maxima = datetime.strptime(fecha_maxima, formato)

        def filtrar_fecha(item, fecha_minima, fecha_maxima) -> dict:
            if (
                fecha_minima
                <= datetime.strptime(item["FECHA_APLICACION"], formato)
                <= fecha_maxima
            ):
                return item

        return list(filter(filtrar_fecha, self.aplicaciones))
