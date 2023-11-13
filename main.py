from Aplicaciones import Aplicaciones
from AnalisisRefuerzo import AnalisisRefuerzo
from AnalisisAplicaciones import AnalisisAplicaciones
from GenerarReporte import GenerarReporte
import time


def run():
    vacunas = Aplicaciones()
    lista = vacunas.exportar_lista_vacunas()
    aplicaciones = AnalisisAplicaciones(lista)
    refuerzos = AnalisisRefuerzo(lista)
    reporte = GenerarReporte(aplicaciones, refuerzos)
    reporte.generar_reporte_de_dosis_aplicadas_y_refuerzos()


if __name__ == "__main__":
    inicio = time.time()
    run()
    final = time.time()
    print("Tiempo de ejecución => ", final - inicio)
