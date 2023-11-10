import Classes.AnalisisRefuerzo as AnalisisRefuerzo

def run():
    try:
        menu = '''
    ** MENÚ **

1. Obtener cantidad de refuerzos aplicados por vacuna
2. Obtener tipo y cantidad de refuerzos aplicados

    Opción: 
'''
        print('Hola!, se están leyendo los archivos .csv ubicados en la carpeta CSV. Ten paciencia, esto puede demorar unos segundos.')
        refuerzos = AnalisisRefuerzo.AnalisisRefuerzo()
        op = int(input(menu))
        match op:
            case 1:
                refuerzos.refuerzos_por_vacuna()
            case 2:
                refuerzos.obtener_refuerzos()
            case _:
                raise Exception('Opción no encontrada. Intenta nuevamente...')
        # refuerzo = refuerzos.filtrar_refuerzos()
        # print(refuerzo[0])
    except Exception as e:
        print(e.name)

if __name__ == '__main__':
    run()