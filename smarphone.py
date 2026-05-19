class smartphone:
    def __init__(self, marca, modelo, color, ram, memoria,
                 serie,pantalla,procesador,bateria,conectividad):
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
        print("f Marca {self.marca}")
        print("f Modelo {self.modelo}")
        print("f Color {self.color}")
        print("f Ram {self.ram}")
        print("f Memoria {self.memoria}")
        print("f Serie {self.serie}")
        print("f Pantalla {self.pantalla}")
        print("f Procesador {self.procesador}")
        print("f Bateria {self.bateria}")
        print("f Conectividad {self.conectividad}")
samsug=smartphone("Samsug,"fake S25","black","1GB","6GB","Serie a","1.8 pulgadas","Snapdragon 8 Elite","5000mAh","8g", Wi-Fi")