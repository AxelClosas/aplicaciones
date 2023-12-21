import app.sistema.Descomprimir as Des
import app.sistema.MoverArchivos as MA
import app.sistema.Limpieza as LIMP


# Proceso para descomprimir el archivo CATAMARCA.zip
def desempaquetadoDeComprimidoZIP():
    # Instanciamos las clases necesarias para ejecutar la lógica
    descompresor = Des.Descomprimir()
    mover_archivos = MA.MoverArchivos()
    limpieza = LIMP.Limpieza()
    # Ejecutamos el metodo descomprimir el objeto descompresor
    descompresor.descomprimir()

    # Ejecutamos el metodo mover_archivos_csv del objeto mover_archivos
    print("Moviendo archivos...")
    mover_archivos.mover_archivos_csv()

    # Ejecutamos el metodo limpieza_de_directorio del objeto limpieza
    print("Limpiando directorio...")
    limpieza.limpieza_de_directorio()

    # Eliminamos las instancias para liberar memoria
    del descompresor, mover_archivos, limpieza
