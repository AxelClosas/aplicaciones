from app.Aplicaciones import Aplicaciones
from app.AnalisisRefuerzo import AnalisisRefuerzo
from app.AnalisisAplicaciones import AnalisisAplicaciones
from app.GenerarReporte import GenerarReporte
from app.Descomprimir import Descomprimir


import time


def run():
    d = Descomprimir()
    d.descomprimir()
    d.mover_archivos_csv()
    d.limpieza_de_directorio()

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
