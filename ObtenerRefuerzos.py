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

    def filtrar_refuerzos(self) -> list:
        lista_de_vacunas = self.generar_lista_con_listas_de_diccionarios()
        filtrado = []
        total = 0

        for vacuna in lista_de_vacunas:
            for item in vacuna:
                if 'Refuerzo' in item['NOMBRE_DOSIS']:
                    filtrado.append(item['NRO_DOC'].strip())
            # filtrado.append([item['NRO_DOC'].strip() for item in vacuna if 'Refuerzo' in item['NOMBRE_DOSIS']])
            
        total = len(filtrado)

        print('Total de Refuerzos => ', total)
        del lista_de_vacunas
        return filtrado

    def contar_total(self):
        lista_de_vacunas = self.generar_lista_con_listas_de_diccionarios()
        total = 0
        for vacuna in lista_de_vacunas:
            total += len(vacuna)
        print('Total de aplicaciones => ',total)

    def calcular_frecuencia(self) -> dict:
        f = {}
        dni_filtrados = self.filtrar_refuerzos()
        for dni in dni_filtrados:
            if dni in f.keys():
                f[dni] += 1
            else:
                f[dni] = 1
        # dni = [ dni for vacuna in vacunas_filtradas for dni in vacuna]
        return f

    def cantidad_aplicaciones(self):
        frecuencias = self.calcular_frecuencia()
        primer_refuerzo = 0
        segundo_refuerzo = 0
        tercer_refuerzo = 0
        cuarto_refuerzo = 0
        quinto_refuerzo = 0
        sexto_refuerzo = 0
        random = 0
        print('tamaño f => ', len(frecuencias))
        for value in frecuencias.values():
            if value == 1:
                primer_refuerzo += 1
            elif value == 2:
                primer_refuerzo += 1
                segundo_refuerzo += 1
            elif value == 3:
                primer_refuerzo += 1
                segundo_refuerzo += 1
                tercer_refuerzo += 1
            elif value == 4:
                primer_refuerzo += 1
                segundo_refuerzo += 1
                tercer_refuerzo += 1
                cuarto_refuerzo += 1
            elif value == 5:
                primer_refuerzo += 1
                segundo_refuerzo += 1
                tercer_refuerzo += 1
                cuarto_refuerzo += 1
                quinto_refuerzo += 1
            elif value == 6:
                primer_refuerzo += 1
                segundo_refuerzo += 1
                tercer_refuerzo += 1
                cuarto_refuerzo += 1
                quinto_refuerzo += 1
                sexto_refuerzo += 1
            else:
                random += 1
        print(primer_refuerzo)
        print(segundo_refuerzo)
        print(tercer_refuerzo)
        print(cuarto_refuerzo)
        print(quinto_refuerzo)
        print(sexto_refuerzo)
        print(random)
            




