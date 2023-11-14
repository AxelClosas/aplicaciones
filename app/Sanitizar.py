class Sanitizar:
    def __init__(self, lista_de_vacunas):
        self.lista_de_vacunas = lista_de_vacunas

    def sanitizar(self) -> list:
        def reemplazar(item) -> dict:
            item["DEPTO_DOMICILIO"].replace("á", "a")
            item["DEPTO_DOMICILIO"].replace("é", "e")
            item["DEPTO_DOMICILIO"].replace("í", "i")
            item["DEPTO_DOMICILIO"].replace("ó", "o")
            item["DEPTO_DOMICILIO"].replace("ú", "u")
            return item

        lista_sana = []
        lista_sana.append(list(map(reemplazar, self.lista_de_vacunas)))
        if len(lista_sana) > 0:
            return lista_sana
        else:
            return "Error."

    def obtener_lista_sana(self) -> list:
        return self.sanitizar()
