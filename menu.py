def menu():
    menu = """
 _____                                                                           _____ 
( ___ )-------------------------------------------------------------------------( ___ )
 |   |                                                                           |   | 
 |   |  ___                             _               _   __                   |   | 
 |   | |_ _|_ __  _ __ ___  _   _ _ __ (_)______ _  ___(_) /_/  _ __   ___  ___  |   | 
 |   |  | || '_ \\| '_ ` _ \\| | | | '_ \\| |_  / _` |/ __| |/ _ \\| '_ \\ / _ \\/ __| |   | 
 |   |  | || | | | | | | | | |_| | | | | |/ / (_| | (__| | (_) | | | |  __/\\__ \\ |   | 
 |   | |___|_| |_|_| |_| |_|\\__,_|_| |_|_/___\\__,_|\\___|_|\\___/|_| |_|\\___||___/ |   | 
 |___|                                                                           |___| 
(_____)-------------------------------------------------------------------------(_____)

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

    4. Cuarto reporte - Cantidad de dosis distribuidas por vacuna a cada Institución - DiCEI

    5. Quinto reporte - Reporte de Ultimas Aplicaciones y Pendientes

    6. Sexto reporte - Descartes de Vacunas según Programa Sanitario (COVID o DiCEI)
    """
    return menu
