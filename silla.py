class silla:
    def __init__(self, material, ergonomia, portabilidad, no_patas, color,
                 altura, reclinable, tamanio, peso, disenio):
        self.material = material
        self.ergonomia = ergonomia
        self.portabilidad = portabilidad
        self.no_patas = no_patas
        self.color = color
        self.altura = altura
        self.reclinable = reclinable
        self.tamanio = tamanio
        self.peso = peso
        self.disenio = disenio
        print("f Material {self. material}")
        print("f Ergonomia {self. ergonomia}")
        print("f Portabilidad {self. portabilidad}")
        print("f No. Patas {self. no_patas}")
        print("f Color {self. color}")
        print("f Altura {self. altura}")
        print("f Reclinable {self. reclinable}")
        print("f Tamaño {self. tamanio}")
        print("f Peso {self. peso}")
        print("f Diseño {self. disenio}")
silla_cocina = silla("Madera", "Alta", "No portable", "4", "Marron", "0.9m", "No reclinable", "Grande", "5kg", "Clasico")