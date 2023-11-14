from app.Descomprimir import Descomprimir
from platform import system


def desempaquetadoDeComprimidoZIP():
    try:
        d = Descomprimir()
        d.descomprimir()
        d.mover_archivos_csv()
        d.limpieza_de_directorio()
    except:
        pass


def sistema_actual():
    # Retorna True si es Windows o False si no lo es
    sistema = system()
    return True if sistema == "Windows" else False
