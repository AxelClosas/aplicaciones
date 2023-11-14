import app.ProcesosLogica as PL
import app.AnalisisRefuerzo as AR
import app.AnalisisAplicaciones as AP
import app.GenerarReporte as GR
import app.Sanitizar as SA
import time
import os


def run():
    ruta_carpeta_csv = PL.generar_ruta_carpeta_csv(carpeta_csv="CSV")
    nombre_archivo_base_completa = "BaseCompletaCOVID.csv"
    es_windows = PL.sistema_actual()
    if es_windows:
        ruta_completa_base_covid = f"{ruta_carpeta_csv}\\{nombre_archivo_base_completa}"
    else:
        ruta_completa_base_covid = f"{ruta_carpeta_csv}/{nombre_archivo_base_completa}"
    base_existe = False

    with os.scandir(ruta_carpeta_csv) as ficheros:
        for fichero in ficheros:
            if nombre_archivo_base_completa == fichero.name:
                base_existe = True
                break
    # Si la base ya existe, aquí armamos el menú
    if base_existe:
        lista_de_vacunas = PL.read_csv(ruta_completa_base_covid)
        sanitizador = SA.Sanitizar(lista_de_vacunas)
        print(sanitizador.sanitizar())

    else:
        print(
            "\nHola!, en unos segundos iniciará el proceso de descompresión del archivo principal que contiene las bases de datos..."
        )
        time.sleep(2)
        PL.desempaquetadoDeComprimidoZIP()
        print("Uniendo archivos para generar base de datos completa")
        PL.creacionDeBaseDeDatosCompletaCOVID()
        print(
            "Parece que todo salió bien!, ejecuta nuevamente el script para obtener los datos que precises. Hasta pronto!"
        )
        time.sleep(2)
        exit()


if __name__ == "__main__":
    inicio = time.time()
    run()
    final = time.time()
    print("Tiempo de ejecución => ", final - inicio)
