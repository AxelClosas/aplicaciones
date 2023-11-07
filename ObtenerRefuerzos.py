import csv
import os

class ObtenerRefuerzos:

    def obtener_nombres(self):
        nombres = []
        # Obtengo la ruta absoluta del directorio actual
        directorio_actual = os.getcwd()
        carpeta_csv = f'{directorio_actual}\\CSV'

        # Con with podemos trabajar en el contexto actual del directorio y obtener los nombres de todos los ficheros
        with os.scandir(carpeta_csv) as ficheros:
            for fichero in ficheros:
                # Si el archivo es main.py simplemente lo pasa por alto continuando con el ciclo
                if fichero.name == 'main.py': continue
                nombres.append(fichero.name)
        return nombres
    
    def read_csv(self, path):
        with open(path, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            header = next(reader)
            data = []
            for row in reader:
                iterable = zip(header, row)
                vacuna_aplicada = {key:value for key, value in iterable}
                data.append(vacuna_aplicada)
        return data
    
    def generar_lista_con_listas_de_diccionarios(self) -> list:
        archivos = self.obtener_nombres()
        lista_con_listas_de_diccionarios = []

        for nombre_archivo in archivos:
            lista_de_diccionarios = self.read_csv(f'./CSV/{nombre_archivo}')
            lista_con_listas_de_diccionarios.append(lista_de_diccionarios)

        del archivos
        return lista_con_listas_de_diccionarios

    def filtrar_refuerzos(self):
        lista_de_vacunas = self.generar_lista_con_listas_de_diccionarios()
        filtrado = []

        for vacuna in lista_de_vacunas:
            print('Vacuna => ',len(vacuna))
            filtrado.append(list(filter(lambda item: 'Refuerzo' in item['NOMBRE_DOSIS'], vacuna)))
        
        del lista_de_vacunas
        return filtrado

    def calcular_frecuencia(self):
        f = {}
        vacunas_filtradas = self.filtrar_refuerzos()
        for vacuna in vacunas_filtradas:
            for item in vacuna:
                if item['NRO_DOC'] in f:
                    f[item['NRO_DOC']] += 1
                else:
                    f.update({item['NRO_DOC']: 1})
        print(len(f.keys()))
        print(len(f.values()))
        return f

# def cantidad_aplicaciones(frecuencias):
#     primer_refuerzo = 0
#     segundo_refuerzo = 0
#     tercer_refuerzo = 0
#     cuarto_refuerzo = 0
#     quinto_refuerzo = 0
#     sexto_refuerzo = 0
#     random = 0

#     for value in frecuencias.values():
#         match value:
#             case 1:
#                 primer_refuerzo += 1
#             case 2:
#                 primer_refuerzo += 1
#                 segundo_refuerzo += 1
#             case 3:
#                 primer_refuerzo += 1
#                 segundo_refuerzo += 1
#                 tercer_refuerzo += 1
#             case 4:
#                 primer_refuerzo += 1
#                 segundo_refuerzo += 1
#                 tercer_refuerzo += 1
#                 cuarto_refuerzo += 1
#             case 5:
#                 primer_refuerzo += 1
#                 segundo_refuerzo += 1
#                 tercer_refuerzo += 1
#                 cuarto_refuerzo += 1
#                 quinto_refuerzo += 1
#             case 6:
#                 primer_refuerzo += 1
#                 segundo_refuerzo += 1
#                 tercer_refuerzo += 1
#                 cuarto_refuerzo += 1
#                 quinto_refuerzo += 1
#                 sexto_refuerzo += 1
#             case _:
#                 random += 1

#     return primer_refuerzo, segundo_refuerzo, tercer_refuerzo, cuarto_refuerzo, quinto_refuerzo, sexto_refuerzo, random




