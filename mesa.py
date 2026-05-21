class mesa:
    def __init__(self, material,ancho,disenio,tamanio,tipo,
                 altura,color,portabilidad,soporte,no_patas):
        self.material = material
        self.ancho = ancho
        self.disenio = disenio
        self.tamanio = tamanio
        self.tipo = tipo
        self.altura = altura
        self.color = color
        self.portabilidad = portabilidad
        self.soporte = soporte
        self.no_patas = no_patas
        print("f Material {self.material}")
        print("f Ancho {self.ancho}")
        print("f Diseño {self.disenio}")
        print("f Tamaño {self.tamanio}")
        print("f Tipo {self.tipo}")
        print("f Altura {self.altura}")
        print("f Color {self.color}")
        print("f Portabilidad {self.portabilidad}")
        print("f Soporte {self.soporte}")
        print("f No. Patas {self.no_patas}")

    def estabilidad(self): 
        print(f"{self.soporte} su estabilidad ")

    def forma (self): 
        print(f"{self.tipo} es su forma")

    def dimenciones (self): 
        print(f"{self.tamanio} son sus dimenciones")

    def funcionalidad(self): 
        print(f"{self.portabilidad} es su funcionalidad")

    def materiales(self): 
        print(f"su material es {self.material}")

mesa_vidrio = mesa("Fierro", "1.5m", "Moderno", "Pequeño", "Sala de estar", "0.75m", "Negro", "No portable", "Fuerte", "2")

mesa_vidrio.estabilidad()
mesa_vidrio.forma()
mesa_vidrio.dimenciones()
mesa_vidrio.funcionalidad()
mesa_vidrio.materiales()