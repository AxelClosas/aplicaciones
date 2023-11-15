class ProcesarDatosDeCatamarca:
    def __init__(self, lista_de_vacunas):
        self.lista_de_vacunas = lista_de_vacunas

    def proceso_obtener_registros_catamarca_ceros_vacios(self) -> list:
        filtro_registros_catamarca = []

        def retornar_id_3(item):
            if (
                item["ID_PROVINCIA_DOMICILIO"].isnumeric()
                and int(item["ID_PROVINCIA_DOMICILIO"]) == 3
            ):
                return item

        def retornar_id_0(item):
            if (
                item["ID_PROVINCIA_DOMICILIO"].isnumeric()
                and int(item["ID_PROVINCIA_DOMICILIO"]) == 0
            ):
                return item

        def retornar_id_vacio(item):
            if item["ID_PROVINCIA_DOMICILIO"] == "":
                return item

        filtrar_id_prov_3 = list(filter(retornar_id_3, self.lista_de_vacunas))
        filtrar_id_prov_0 = list(filter(retornar_id_0, self.lista_de_vacunas))
        filtrar_id_prov_vacio = list(filter(retornar_id_vacio, self.lista_de_vacunas))

        # print("Total dosis id_prov = 3", len(filtrar_id_prov_3))
        # print("Total dosis id_prov = 0", len(filtrar_id_prov_0))
        # print("Total dosis id_prov = vacio", len(filtrar_id_prov_vacio))

        filtro_registros_catamarca.extend(filtrar_id_prov_3)
        filtro_registros_catamarca.extend(filtrar_id_prov_0)
        filtro_registros_catamarca.extend(filtrar_id_prov_vacio)

        return filtro_registros_catamarca

    def proceso_arreglar_id_prov_domicilio(self) -> list:
        catamarca_ceros_vacios = self.proceso_obtener_registros_catamarca_ceros_vacios()

        def cambiar_id_nombre(item):
            copia_item = item.copy()
            if (
                copia_item["ID_PROVINCIA_DOMICILIO"].isnumeric()
                and int(copia_item["ID_PROVINCIA_DOMICILIO"]) == 0
            ):
                copia_item["ID_PROVINCIA_DOMICILIO"] = 3
                copia_item["PROVINCIA_DOMICILIO"] = "Catamarca"
            elif copia_item["ID_PROVINCIA_DOMICILIO"] == "":
                copia_item["ID_PROVINCIA_DOMICILIO"] = 3
                copia_item["PROVINCIA_DOMICILIO"] = "Catamarca"

            return copia_item

        resultado = list(map(cambiar_id_nombre, catamarca_ceros_vacios))

        return resultado

    def proceso_arreglar_id_depto_domicilio_post_arreglar_id_prov(self):
        catamarca = self.proceso_arreglar_id_prov_domicilio()

        def cambiar_id_nombre(item):
            copia_item = item.copy()

            def reemplazar():
                copia_item["ID_DEPTO_DOMICILIO"] = copia_item[
                    "ID_DEPTO_ESTABLECIMIENTO"
                ]
                copia_item["DEPTO_DOMICILIO"] = copia_item["DEPTO_ESTABLECIMIENTO"]

            if (
                copia_item["ID_DEPTO_DOMICILIO"].isnumeric()
                and int(copia_item["ID_DEPTO_DOMICILIO"]) == 0
            ):
                reemplazar()
            elif (
                copia_item["ID_DEPTO_DOMICILIO"].isnumeric()
                and int(copia_item["ID_DEPTO_DOMICILIO"]) == 473
            ):
                reemplazar()
            elif copia_item["ID_DEPTO_DOMICILIO"] == "":
                reemplazar()

            return copia_item

        resultado = list(map(cambiar_id_nombre, catamarca))

        return resultado

    def obtener_base_arreglada_catamarca(self) -> list:
        resultado = self.proceso_arreglar_id_depto_domicilio_post_arreglar_id_prov()
        return resultado
