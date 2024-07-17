import math
class Figura:

    def Calcular_AreaEsfera(radio):
        area_esfera = 4 *3.1416* (float(radio) ** 2)
        return area_esfera

    def Calcular_AreaCirculo(radio):
        area_circulo = 3.1416 * (float(radio) ** 2)
        return area_circulo

    def Calcular_Volumen(radio):
        volumen= (4/3) * 3.1416 * (float(radio) ** 3)
        return volumen




