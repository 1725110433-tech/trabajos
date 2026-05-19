class transporte:
    def __init__(self,modo, operador, capacidad, origen, destino,
                 horario, duracion, precio, frecuencia,ruta):
        self. modo = modo
        self. operador = operador
        self. capacidad = capacidad
        self. origen = origen
        self. destino = destino
        self. horario = horario
        self. duracion = duracion
        self. precio = precio
        self. frecuencia = frecuencia
        self. ruta = ruta
        print("f Modo {self. modo}")
        print("f Operador {self. operador}")
        print("f Capacidad {self. capacidad}")
        print("f Origen {self. origen}")
        print("f Destino {self. destino}")
        print("f Horario {self. horario}")
        print("f Duracion {self. duracion}")
        print("f Precio {self. precio}")
        print("f Frecuencia {self. frecuencia}")
        print("f Ruta {self. ruta}")
didicard = transporte("didicard", "manual", "2 pasajeros", "tepito", "oaxaca","18:00-19:00","1 hoa", "35000 pesos", "30 min ", "Autopista")