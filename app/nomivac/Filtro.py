from datetime import datetime, date


class Filtro:
    def filtrar_primera_dosis(self, aplicaciones):
        """Devuelve una lista de aplicaciones

        Args:
            aplicaciones (List[dict]): Lista de aplicaciones

        Returns:
            Lista filtrada: Lista de aplicaciones filtrada
        """
        filtro = []

        def filtrar_nombre_dosis(item: dict) -> dict:
            if "1ra" in item["NOMBRE_DOSIS"]:
                return item

        filtro.extend(list(filter(filtrar_nombre_dosis, aplicaciones)))

        return filtro

    def filtrar_segunda_dosis(self, aplicaciones):
        """Devuelve una lista de aplicaciones

        Args:
            aplicaciones (List[dict]): Lista de aplicaciones

        Returns:
            Lista filtrada: Lista de aplicaciones filtrada
        """
        filtro = []

        def filtrar_nombre_dosis(item: dict) -> dict:
            if "2da" in item["NOMBRE_DOSIS"]:
                return item

        filtro.extend(list(filter(filtrar_nombre_dosis, aplicaciones)))

        return filtro

    def filtrar_dosis_adicional(self, aplicaciones):
        """Devuelve una lista de aplicaciones

        Args:
            aplicaciones (List[dict]): Lista de aplicaciones

        Returns:
            Lista filtrada: Lista de aplicaciones filtrada
        """
        filtro = []

        def filtrar_nombre_dosis(item: dict) -> dict:
            if "Adicional" in item["NOMBRE_DOSIS"]:
                return item

        filtro.extend(list(filter(filtrar_nombre_dosis, aplicaciones)))

        return filtro

    def filtrar_dosis_unica(self, aplicaciones):
        """Devuelve una lista de aplicaciones

        Args:
            aplicaciones (List[dict]): Lista de aplicaciones

        Returns:
            Lista filtrada: Lista de aplicaciones filtrada
        """
        filtro = []

        def filtrar_nombre_dosis(item: dict) -> dict:
            if "Unica" in item["NOMBRE_DOSIS"]:
                return item

        filtro.extend(list(filter(filtrar_nombre_dosis, aplicaciones)))

        return filtro

    def filtrar_refuerzos(self, aplicaciones):
        """Devuelve una lista de aplicaciones

        Args:
            aplicaciones (List[dict]): Lista de aplicaciones

        Returns:
            Lista filtrada: Lista de aplicaciones filtrada
        """
        filtro = []

        def filtrar_nombre_dosis(item: dict) -> dict:
            if "Refuerzo" in item["NOMBRE_DOSIS"]:
                return item

        filtro.extend(list(filter(filtrar_nombre_dosis, aplicaciones)))

        return filtro

    def filtrar_por_fecha_de_aplicacion(self, aplicaciones, fecha_minima: str):
        """Devuelve una lista de aplicaciones

        Args:
            aplicaciones (List[dict]): Lista de aplicaciones
            fecha_minima (str): Fecha minima
            fecha_maxima (str): Fecha maxima


        Returns:
            Lista filtrada: Lista de aplicaciones filtrada
        """
        formato = "%d/%m/%Y"
        fecha_hoy = date.today().strftime(formato)

        fecha_minima = datetime.strptime(fecha_minima, formato)
        fecha_maxima = datetime.strptime(fecha_hoy, formato)

        return list(
            filter(
                lambda item: fecha_minima
                <= datetime.strptime(item["FECHA_APLICACION"], formato)
                <= fecha_maxima,
                aplicaciones,
            )
        )
