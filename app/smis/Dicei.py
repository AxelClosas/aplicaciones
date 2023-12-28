class Dicei:
    def __init__(self, movimientos: list):
        self.movimientos = movimientos

    def procesar_datos(self) -> list:
        def cambiar_nombre(item) -> dict:
            cambiar_nombre = {
                # Diccionario de vacunas con sus diferentes nombres según laboratorio para ser reemplazados
            }

            for nombre, nombres_variables in cambiar_nombre.items():
                for nombre_variable in nombres_variables:
                    if nombre_variable in item["Producto origen"]:
                        item["Producto origen"] = nombre
            return item

        # Declaramos la función obtener_vacunas para filtrar unicamente las vacunas
        def obtener_vacunas(item) -> dict:
            vacunas = [
                # Lista de vacunas, nombres estandarizados
            ]
            for vacuna in vacunas:
                if vacuna in item["Producto origen"]:
                    return item

        # Mapeamos la lista de movimientos inicializada para dar origen a una nueva lista estandarizada
        nueva_lista_vacunas = list(map(cambiar_nombre, self.movimientos))

        # Filtramos la nueva lista para extraer unicamente las vacunas
        movimientos_vacunas = list(filter(obtener_vacunas, nueva_lista_vacunas))

        # Retornamos los movimientos de vacunas unicamente
        return movimientos_vacunas

    # Declaramos la función retornar_movimientos_regulares
    def retornar_movimientos_regulares(self) -> list:
        # Obtenemos los movimientos de vacunas
        movimientos = self.procesar_datos()
        # Retornamos una lista de movimientos regulares
        return list(
            filter(lambda item: item["Tipo movimiento"] == "Regular", movimientos)
        )

    # Declaramos la función retornar_movimientos_internos
    def retornar_movimientos_internos(self):
        # Obtenemos los movimientos de vacunas
        movimientos = self.procesar_datos()
        # Retornamos una lista de movimientos regulares
        return list(
            filter(lambda item: item["Tipo movimiento"] == "Interno", movimientos)
        )