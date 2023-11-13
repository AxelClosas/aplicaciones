class AnalisisRefuerzo:
    def __init__(self, lista_de_vacunas: list):
        self.lista_de_vacunas = lista_de_vacunas

    def filtrar_refuerzos(self) -> list:
        filtro_ref = []
        filtro_ref.extend(
            list(
                filter(lambda item: "Refuerzo" in item["DOSIS"], self.lista_de_vacunas)
            )
        )
        return filtro_ref

    def frecuencia(self) -> dict:
        refuerzos = self.filtrar_refuerzos()
        f = {}
        for item in refuerzos:
            if item["DNI"].isnumeric():
                if int(item["DNI"]) in f.keys():
                    f[int(item["DNI"])] += 1
                else:
                    f[int(item["DNI"])] = 1
            else:
                if item["DNI"] in f.keys():
                    f[item["DNI"]] += 1
                else:
                    f[item["DNI"]] = 1
        return f

    def refuerzos_por_vacuna(self, nombre="refuerzos_por_vacuna"):
        ref_vacuna = {}
        vacunas = self.filtrar_refuerzos()
        for item in vacunas:
            if item["VACUNA"] in ref_vacuna:
                ref_vacuna[item["VACUNA"]] += 1
            else:
                ref_vacuna[item["VACUNA"]] = 1
        return ref_vacuna

    def total_refuerzos(self) -> int:
        refuerzos = self.filtrar_refuerzos()
        return len(refuerzos)

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

    # def obtener_refuerzos(self, nombre_archivo="ref_aplicados"):
    #     primer, segundo, tercer, cuarto, quinto, sexto, extra = self.calcular()
    #     total_refuerzos = self.total_refuerzos()

    #     print(f"Exportando archivo: {nombre_archivo}")
    #     with open(f"{nombre_archivo}.txt", "w", encoding="utf-8") as file:
    #         file.write(
    #             f"Actualización: {str(input('Ingresa la fecha de corte de las bases: '))}\n\nPrimer refuerzo: {primer}\nSegundo refuerzo: {segundo}\nTercer refuerzo: {tercer}\nCuarto refuerzo: {cuarto}\nQuinto refuerzo: {quinto}\nSexto refuerzo: {sexto}\nValores extras: {extra}\n\nTotal Refuerzos: {total_refuerzos}"
    #     )
