from Refuerzos import Refuerzos

def run():
    print('Hola!, se están leyendo los archivos .csv ubicados en la carpeta CSV. Ten paciencia, esto puede demorar unos segundos.')
    refuerzos = Refuerzos()
    refuerzos.obtener_refuerzos()
    print('Terminado.')
    # refuerzo = refuerzos.filtrar_refuerzos()
    # print(refuerzo[0])

if __name__ == '__main__':
    run()