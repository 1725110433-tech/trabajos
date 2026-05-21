class coche:
    def __init__(self, marca, modelo, año, color, motor, potencia, consumo, velocidad_maxima, precio, puertas):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.motor = motor
        self.potencia = potencia
        self.consumo = consumo
        self.velocidad_maxima = velocidad_maxima
        self.precio = precio
        self.puertas = puertas
        print("f Marca {self.marca}")
        print("f Modelo {self.modelo}")
        print("f Año {self.año}")
        print("f Color {self.color}")
        print("f Motor {self.motor}")
        print("f Potencia {self.potencia}")
        print("f Consumo {self.consumo}")
        print("f Velocidad Maxima {self.velocidad_maxima}")
        print("f Precio {self.precio}")
        print("f Puertas {self.puertas}")

    def limpieza(self): 
        print(f"{self.modelo} se hizo limpieza ")

    def lubricacion(self): 
        print(f"{self.motor} se hizo lubricacion ")
    
    def alineacion(self): 
        print(f"{self.motor} se hizo alineacion ")

    def revicion(self): 
        print(f"{self.motor} se le hizo revicion al motor  ")

    def aire_acondicionado(self): 
        print(f"{self.potencia} se le ajusto la potencia al aire acondicionado")

tesla = coche("Tesla", "Model S", 2020, "Negro", "v8", "1020 hp", "20 kWh/100 km", "322 km/h", "$89,990", "2")
  
tesla.limpieza()
tesla.lubricacion()
tesla.alineacion()
tesla.revicion()
tesla.aire_acondicionado()


