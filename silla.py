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
        
        print(f"Material: {self.material}")
        print(f"Ergonomia: {self.ergonomia}")
        print(f"Portabilidad: {self.portabilidad}")
        print(f"No. Patas: {self.no_patas}")
        print(f"Color: {self.color}")
        print(f"Altura: {self.altura}")
        print(f"Reclinable: {self.reclinable}")
        print(f"Tamaño: {self.tamanio}")
        print(f"Peso: {self.peso}")
        print(f"Diseño: {self.disenio}")

    def soporte(self): 
        print(f"El peso propio de la silla es {self.peso}")

    def confort(self): 
        print(f"El material de la silla es {self.material}")

    def postura(self): 
        print(f"Su tipo de respaldo es {self.ergonomia}")

    def base(self): 
        print(f"La base de la silla tiene {self.no_patas} patas")

    def lugar(self): 
        print(f"Esta silla está diseñada con un estilo {self.disenio}")

silla_cocina = silla("Madera", "Alta", "No portable", "4", "Marron", "0.9m", "No reclinable", "Grande", "5kg", "Clasico")

silla_cocina.soporte()
silla_cocina.confort()
silla_cocina.postura()
silla_cocina.base()
silla_cocina.lugar()
