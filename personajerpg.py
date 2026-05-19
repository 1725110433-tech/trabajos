class personaje_rpg:
    def __init__(self, fuerza,agilidad,punteria,resistencia,salud,
                 intuicion,percepcion,altura,peso):
        self. fuerza = fuerza
        self. agilidad = agilidad
        self. punteria = punteria
        self. resistencia = resistencia 
        self. salud = salud
        self. intuicion = intuicion
        self. percepcion = percepcion
        self. altura = altura
        self. peso = peso
        print("f Fuerza {self. fuerza}")
        print("f Agilidad {self. agilidad}")
        print("f Punteria {self. punteria}")
        print("f Resistencia {self. resistencia}")
        print("f Salud {self. salud}")
        print("f Intuicion {self. intuicion}")
        print("f Percepcion {self. percepcion}")
        print("f Altura {self. altura}")
        print("f Peso {self. peso}")
ghost=personaje_rpg("poca", "mala", "novato", "nada", "Robusto", "mala", "Excepcional", "1.12cm", "9-1kg")