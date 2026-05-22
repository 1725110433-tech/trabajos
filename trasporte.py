class transporte:
    def __init__(self, modo, operador, capacidad, origen, destino,
                 horario, duracion, precio, frecuencia, ruta):
        self.modo = modo
        self.operador = operador
        self.capacidad = capacidad
        self.origen = origen
        self.destino = destino
        self.horario = horario
        self.duracion = duracion
        self.precio = precio
        self.frecuencia = frecuencia
        self.ruta = ruta
        
        print(f"Modo: {self.modo}")
        print(f"Operador: {self.operador}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Origen: {self.origen}")
        print(f"Destino: {self.destino}")
        print(f"Horario: {self.horario}")
        print(f"Duracion: {self.duracion}")
        print(f"Precio: {self.precio}")
        print(f"Frecuencia: {self.frecuencia}")
        print(f"Ruta: {self.ruta}")

    def velocidad(self): 
        print(f"El viaje tiene una duración estimada de {self.duracion}")

    def combustible(self): 
        print(f"El tipo de transporte utilizado es: {self.modo}")

    def cupo(self): 
        print(f"Este transporte tiene capacidad para {self.capacidad}")

    def control(self): 
        print(f"El tipo de control del vehículo es {self.operador}")

    def viaje(self): 
        print(f"El viaje va desde {self.origen}")

didicard = transporte("didicard", "manual", "2 pasajeros", "tepito", "oaxaca", "18:00-19:00", "1 hoa", "35000 pesos", "30 min ", "Autopista")

didicard.velocidad()
didicard.combustible()
didicard.cupo()
didicard.control()
didicard.viaje()