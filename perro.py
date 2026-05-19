class perro: 
    def __init__(self, altura, color, raza, peso, no_patas,
                 no_ojos, color_de_ojos, temperamento, fuerza_de_mordedura, apariencia):
        self.altura = altura
        self.color = color
        self.raza = raza
        self.peso = peso
        self.no_patas = no_patas
        self.no_ojos = no_ojos
        self.color_de_ojos = color_de_ojos
        self.temperamento = temperamento
        self.fuerza_de_mordedura = fuerza_de_mordedura
        self.apariencia = apariencia
        print("f Altura {self. altura}")
        print("f Color {self. color}")
        print("f Raza {self. raza}")
        print("f Peso {self. peso}")
        print("f No. Patas {self. no_patas}")
        print("f No. Ojos {self. no_ojos}")
        print("f Color de Ojos {self. color_de_ojos}")
        print("f Temperamento {self. temperamento}")
        print("f Fuerza de Mordedura {self. fuerza_de_mordedura}")
        print("f Apariencia {self. apariencia}")
perro_beto= perro("80m", "gris", "Pug", "1000kg", "1", "7", "Negro", "malo", "100PSI", "Liso")