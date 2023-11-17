def menu():
    menu = """
oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
o                                                                o
o        ooooooo    ooooooo    ooo  ooo    ooo    oooooo         o
o        ooooooo    ooooooo    ooo  ooo    ooo    ooooooo        o
o        ooo        oo   oo    ooo  ooo    ooo    oo    oo       o
o        ooo        oo   oo    ooo  ooo    ooo    oo    oo       o
o        ooo        oo   oo    ooo  ooo    ooo    oo    oo       o
o        ooooooo    ooooooo     oo  oo     ooo    ooooooo        o
o        ooooooo    ooooooo      oooo      ooo    oooooo         o
o                                                                o
oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

Hola!, este programa permite automatizar la extracción de datos en archivos CSV, por lo tanto, solo podrías ejecutar 1 tarea
por cada ejecución del Script. A continuación tienes un menú de opciones con el número asociado a la tarea para realizar, por favor escribe
la opción que desees y a continuación presiona Enter para iniciar la ejecución. Para conocer a fondo como trabaja el Script, por favor
consulta el material "Explicacion_programa.docx".

    1. Primer reporte
        -> Total de vacunas aplicadas en general
        -> Total de vacunas aplicadas a la población de Catamarca (Provincia de domicilio = Catamarca)
        -> Total de vacunas aplicadas por Departamento (Provincia de domicilio = Catamarca)
    
    2. Segundo reporte - Vacunas
        -> Total de vacunas aplicadas discriminadas por Vacuna en general
        -> Total de vacunas aplicadas discriminadas por Vacuna a la población de Catamarca (Provincia de domicilio = Catamarca)
    
    3. Tercer reporte - Tipo y cantidad de Aplicaciones (1ra dosis, 2da dosis, etc, incluidos los refuerzos)
        -> Dosis aplicadas en general
        -> Dosis aplicadas a la población de Catamarca (Provincia de domicilio = Catamarca)
    """
    return menu
