import app.FuncionesLogicaCSV as FL
from datetime import datetime


class Distribucion:
    # Inicializamos la instancia con los nombres clave de la carpeta y el archivo para posteriormente usarlos
    def __init__(self, nombre_carpeta_csv_smis: str, nombre_archivo_csv_smis: str):
        self.nombre_carpeta_csv_smis = nombre_carpeta_csv_smis
        self.nombre_archivo_csv_smis = nombre_archivo_csv_smis

    # Se obtienen los datos crudos de la Base SMIS en función de los parametros recibidos en el constructor
    def obtener_datos(self):
        carpeta_csv_smis = FL.generar_ruta_carpeta_csv(self.nombre_carpeta_csv_smis)
        data = FL.read_csv(f"{carpeta_csv_smis}/{self.nombre_archivo_csv_smis}")
        return data

    def retornar_movimientos_de_programa_sanitario(self, programa: str) -> list:
        # Funciones para transformar los datos
        def campos_relevantes(item):
            item_copy = item.copy()
            n_dict = {
                "Tipo movimiento": item_copy["Tipo movimiento"],
                "Motivo movimiento interno": item_copy["Motivo movimiento interno"],
                "Fecha entrega": item_copy["Fecha entrega"],
                "Nro. remito": item_copy["Nro. remito"],
                "Código institución origen": int(
                    item_copy["Código institución origen "]
                ),
                "Institución origen": item_copy["Institución origen"],
                "Depósito origen": item_copy["Depósito origen"],
                "Código institución destino": int(
                    item_copy["Código institución destino"]
                ),
                "Código depósito destino": int(item_copy["Código depósito destino"]),
                "Institución destino": item_copy["Institución destino"],
                "Depósito destino": item_copy["Depósito destino"],
                "Programa sanitario": item_copy["Programa sanitario"],
                "Producto origen": item_copy["Producto origen"],
                "Lote origen": item_copy["Lote origen"],
                "Fecha vto. origen": item_copy["Fecha vto. origen"],
                "Cantidad origen": int(item_copy["Cantidad origen"]),
            }
            return n_dict

        def transformar_fecha_entrega(item):
            formato = "%d/%m/%Y"
            item_copia = item.copy()
            item_copia["Fecha entrega"] = datetime.strptime(
                item_copia["Fecha entrega"], formato
            )
            return item_copia

        # Obtenemos los datos crudos para aplicar las transformaciones
        data = self.obtener_datos()
        # Primero nos quedamos con los campos relevantes
        campos_importantes = list(map(campos_relevantes, data))

        # Luego transformamos la fecha de entrega
        resultado_transformacion_fecha_entrega = list(
            map(transformar_fecha_entrega, campos_importantes)
        )

        movimientos_segun_programa = list(
            filter(
                lambda item: item["Programa sanitario"] == programa,
                resultado_transformacion_fecha_entrega,
            )
        )

        return movimientos_segun_programa
