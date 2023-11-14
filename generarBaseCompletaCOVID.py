import app.Aplicaciones as APL
import time


def run():
    vacunas = APL.Aplicaciones(carpeta_csv="CSV")
    vacunas.exportar_lista_vacunas()


if __name__ == "__main__":
    inicio = time.time()
    run()
    final = time.time()
    print("Tiempo de ejecución => ", final - inicio)
