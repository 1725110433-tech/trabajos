class personaje_rpg:
    def __init__(self, fuerza, agilidad, punteria, resistencia, salud, intuicion, percepcion, altura, peso):
    
        self.fuerza = fuerza
        self.agilidad = agilidad
        self.punteria = punteria
        self.resistencia = resistencia 
        self.salud = salud
        self.intuicion = intuicion
        self.percepcion = percepcion
        self.altura = altura
        self.peso = peso
        
        print(f"Fuerza: {self.fuerza}")
        print(f"Agilidad: {self.agilidad}")
        print(f"Punteria: {self.punteria}")
        print(f"Resistencia: {self.resistencia}")
        print(f"Salud: {self.salud}")
        print(f"Intuicion: {self.intuicion}")
        print(f"Percepcion: {self.percepcion}")
        print(f"Altura: {self.altura}")
        print(f"Peso: {self.peso}")

    def vida(self): 
        print(f"Al personaje le quedan {self.salud} puntos de vida")

    def clase(self): 
        print(f"La profesión del personaje es {self.punteria}") 
        
    def poder(self): 
        print(f"Su fuerza mágica es de {self.intuicion}") 

    def mochila(self): 
        print(f"En su inventario lleva {self.resistencia}") 

    def nivel(self): 
        print(f"Su nivel actual es {self.agilidad}")
        
ghost = personaje_rpg("poca", "mala", "novato", "nada", "Robusto", "mala", "Excepcional", "1.12cm", "9-1kg")


ghost.clase()
ghost.vida()
ghost.poder()
ghost.mochila()
ghost.nivel()