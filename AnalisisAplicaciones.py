from AnalisisRefuerzo import AnalisisRefuerzo

class AnalisisAplicaciones():
    def __init__(self, lista_de_vacunas):
        self.lista_de_vacunas = lista_de_vacunas
        self.primera_dosis = self.filtrar_primera_dosis()
        self.primera_dosis = self.filtrar_primera_dosis()
        self.primera_dosis = self.filtrar_primera_dosis()

    def filtrar_primera_dosis(self) -> list:
        filtro_primera = []
        filtro_primera.extend(list(filter(lambda item: '1ra' in item['DOSIS'], self.lista_de_vacunas)))
        return filtro_primera
    
    def filtrar_segunda_dosis(self) -> list:
        filtro_segunda = []
        filtro_segunda.extend(list(filter(lambda item: '2da' in item['DOSIS'], self.lista_de_vacunas)))
        return filtro_segunda
    
    def filtrar_dosis_unica(self) -> list:
        filtro_unica = []
        filtro_unica.extend(list(filter(lambda item: 'Unica' in item['DOSIS'], self.lista_de_vacunas)))
        return filtro_unica

    def filtrar_dosis_adicional(self) -> list:
        filtro_adicional = []
        filtro_adicional.extend(list(filter(lambda item: 'Adicional' in item['DOSIS'], self.lista_de_vacunas)))
        return filtro_adicional
        
    def obtener_aplicaciones(self, nombre='aplicaciones_totales'):
        primera_dosis = len(self.filtrar_primera_dosis())
        segunda_dosis = len(self.filtrar_segunda_dosis())
        unica_dosis = len(self.filtrar_dosis_unica())
        dosis_adicional = len(self.filtrar_dosis_adicional())
        
        print(f'Exportando archivo: {nombre}')
        with open(f'{nombre}.txt', 'w') as file:
            file.write(f'Primera dosis: {primera_dosis}\nSegunda dosis: {segunda_dosis}\nUnica dosis: {unica_dosis}\nDosis Adicional: {dosis_adicional}')
        refuerzos = AnalisisRefuerzo(self.lista_de_vacunas)
        refuerzos.obtener_refuerzos()
        
