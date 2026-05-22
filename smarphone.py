class smartphone:
    def __init__(self, marca, modelo, color, ram, memoria,
                 serie, pantalla, procesador, bateria, conectividad):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.ram = ram
        self.memoria = memoria
        self.serie = serie
        self.pantalla = pantalla
        self.procesador = procesador
        self.bateria = bateria
        self.conectividad = conectividad
        
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Ram: {self.ram}")
        print(f"Memoria: {self.memoria}")
        print(f"Serie: {self.serie}")
        print(f"Pantalla: {self.pantalla}")
        print(f"Procesador: {self.procesador}")
        print(f"Bateria: {self.bateria}")
        print(f"Conectividad: {self.conectividad}")
        
    def energia(self): 
        print(f"La capacidad de la batería es de {self.bateria}")

    def mostrar_pantalla(self): 
        print(f"Su tamaño de pantalla es de {self.pantalla}")

    def espacio(self): 
        print(f"Tiene una memoria de {self.memoria}")

    def foto(self): 
        print(f"La cámara pertenece al modelo {self.modelo}")

    def cerebro(self): 
        print(f"El procesador que utiliza es {self.procesador}")

samsug = smartphone("Samsung", "fake S25", "black", "1GB", "6GB", "Serie a", "1.8 pulgadas", "Snapdragon 8 Elite", "5000mAh", "8g, Wi-Fi")

samsug.energia()
samsug.mostrar_pantalla()       
samsug.espacio()
samsug.foto()
samsug.cerebro()