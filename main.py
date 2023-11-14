import app.ProcesosLogica as PL
from app.AnalisisRefuerzo import AnalisisRefuerzo
from app.AnalisisAplicaciones import AnalisisAplicaciones
from app.GenerarReporte import GenerarReporte

import time


def run():
    # Ejecuta la función que se encuentre en ProcesosLogica
    # PL.desempaquetadoDeComprimidoZIP()
    pass
    # aplicaciones = AnalisisAplicaciones(lista)
    # refuerzos = AnalisisRefuerzo(lista)
    # reporte = GenerarReporte(aplicaciones, refuerzos)
    # reporte.generar_reporte_de_dosis_aplicadas_y_refuerzos()


if __name__ == "__main__":
    inicio = time.time()
    run()
    final = time.time()
    print("Tiempo de ejecución => ", final - inicio)
