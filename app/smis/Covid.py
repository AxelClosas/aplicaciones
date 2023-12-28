from app.Configuraciones import diccionario_de_vacunas_covid, lista_de_vacunas_covid


class Covid:
    def __init__(self, movimientos: list):
        # Al instanciar la clase Covid, recibimos los movimientos para procesarlos luego
        self.movimientos = movimientos

    # Declaramos la función cambiar_nombre para recorrer item por item e ir estandarizando los nombres

    # Procesamos los datos para obtener los movimientos estandarizados y solamente de vacunas
    def procesar_datos(self) -> list:
        def cambiar_nombre(item) -> dict:
            nombres_con_variantes = diccionario_de_vacunas_covid.copy()

            for nombre, nombres_variables in nombres_con_variantes.items():
                for nombre_variable in nombres_variables:
                    if nombre_variable == item["Producto origen"]:
                        item["Producto origen"] = nombre
            return item

        # Declaramos la función obtener_vacunas para filtrar unicamente las vacunas
        def obtener_vacunas(item) -> dict:
            vacunas = lista_de_vacunas_covid.copy()
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
