from Aplicaciones import Aplicaciones
from AnalisisRefuerzo import AnalisisRefuerzo
from AnalisisAplicaciones import AnalisisAplicaciones


def run():
    try:
        vacunas = Aplicaciones()
        lista = vacunas.exportar_lista_vacunas()
        menu = '''
    ** MENÚ **

1. Obtener cantidad de refuerzos aplicados por vacuna
2. Obtener tipo y cantidad de refuerzos aplicados
3. Obtener total de aplicaciones. (1ra dosis, 2da dosis)
    Opción: '''
        op = int(input(menu))
        match op:
            case 1:
                refuerzos = AnalisisRefuerzo(lista)
                refuerzos.refuerzos_por_vacuna()
            case 2:
                refuerzos = AnalisisRefuerzo(lista)
                refuerzos.obtener_refuerzos()
            case 3:
                aplicaciones = AnalisisAplicaciones(lista)
                aplicaciones.obtener_aplicaciones()
            case _:
                raise Exception('Opción no encontrada. Intenta nuevamente...')
        # refuerzo = refuerzos.filtrar_refuerzos()
        # print(refuerzo[0])
    except Exception as e:
        print(e)

if __name__ == '__main__':
    run()