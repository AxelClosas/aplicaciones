import csv
import os

class Refuerzos:
    def __init__(self):
        self.lista_de_vacunas = self.transformar_datos()
    
    def obtener_nombres(self) -> list:
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
    
    def read_csv(self, path) -> list:
        with open(path, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            header = next(reader)
            data = []
            for row in reader:
                iterable = zip(header, row)
                vacuna_aplicada = {key:value for key, value in iterable}
                data.append(vacuna_aplicada)
            
        return data
    
    def generar_lista(self) -> list:
        archivos = self.obtener_nombres()
        data = []
        for archivo in archivos:
            lista = self.read_csv(f'./CSV/{archivo}')
            data.append(lista)
        
        return data
    
    def transformar_datos(self) -> list:
        def obtener(item) -> dict:
            n_dict = {
                'ID': item['ID_CMDB_PERSONA'],
                'DNI': item['NRO_DOC'],
                'VACUNA': item['VACUNA'],
                'FECHA_APLICACION': item['FECHA_APLICACION'],
                'DOSIS': item['NOMBRE_DOSIS'],
                'PROVINCIA': item['PROVINCIA_DOMICILIO']
                }
            return n_dict
        
        data = self.generar_lista()
        nuevo = []
        for vacuna in data:
            nuevo.extend(list(map(obtener, vacuna)))
        return nuevo
    
    def filtrar_catamarca(self) -> list:
        filtro_catamarca = []
        filtro_catamarca.extend(list(filter(lambda item: 'Catamarca' in item['PROVINCIA'], self.lista_de_vacunas)))
        return filtro_catamarca
    
    def filtrar_refuerzos(self) -> list:
        filtro_ref = []
        filtro_ref.extend(list(filter(lambda item: 'Refuerzo' in item['DOSIS'], self.lista_de_vacunas)))
        return filtro_ref

    def frecuencia(self) -> dict:
        refuerzos = self.filtrar_refuerzos()
        f = {}
        for item in refuerzos:
            if item['DNI'].isnumeric():
                if int(item['DNI']) in f.keys():
                    f[int(item['DNI'])] += 1
                else:
                    f[int(item['DNI'])] = 1
            else:
                if item['DNI'] in f.keys():
                    f[item['DNI']] += 1
                else:
                    f[item['DNI']] = 1
        return f
    
    def refuerzos_por_vacuna(self):
        ref_vacuna = {}
        vacunas = self.filtrar_refuerzos()
        for item in vacunas:
            if item['VACUNA'] in ref_vacuna:
                ref_vacuna[item['VACUNA']] += 1
            else:
                ref_vacuna[item['VACUNA']] = 1
        print(ref_vacuna)

    def calcular(self):
        f = self.frecuencia()
        primer = 0
        segundo = 0
        tercer = 0
        cuarto = 0
        quinto = 0
        sexto = 0
        extra = 0

        for cantidad in f.values():
            match cantidad:
                case 1:
                    primer += 1
                case 2:
                    primer += 1
                    segundo += 1
                case 3:
                    primer += 1
                    segundo += 1
                    tercer += 1
                case 4:
                    primer += 1
                    segundo += 1
                    tercer += 1
                    cuarto += 1
                case 5:
                    primer += 1
                    segundo += 1
                    tercer += 1
                    cuarto += 1
                    quinto += 1
                case 6:
                    primer += 1
                    segundo += 1
                    tercer += 1
                    cuarto += 1
                    quinto += 1
                    sexto += 1
                case _:
                    extra += 1
        return primer, segundo, tercer, cuarto, quinto, sexto, extra
    
    def obtener_refuerzos(self, nombre_archivo='ref_aplicados'):
        primer, segundo, tercer, cuarto, quinto, sexto, extra = self.calcular()
        with open(f'{nombre_archivo}.txt', 'w') as file:
            file.write(f'Primer refuerzo: {primer}\nSegundo refuerzo: {segundo}\nTercer refuerzo: {tercer}\nCuarto refuerzo: {cuarto}\nQuinto refuerzo: {quinto}\nSexto refuerzo: {sexto}\nValores extras: {extra}')