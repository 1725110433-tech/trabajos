class banco:
    def __init__(self, no_clientes, no_guardias, no_edificios, sistema_informatico,
                nombre_banco, no_cajeros, fiable, capital, horario_atencion, color_banco):
        self. no_clientes = no_clientes
        self. no_guardias = no_guardias
        self. no_edificios = no_edificios
        self. sistema_informatico = sistema_informatico
        self. nombre_banco = nombre_banco
        self. no_cajeros = no_cajeros
        self. fiable = fiable
        self. capital = capital
        self. horario_atencion = horario_atencion
        self. color_banco = color_banco
        print("f No. Clientes {self.no_clientes}")
        print("f No. Guardias {self.no_guardias}")  
        print("f No. Edificios {self.no_edificios}")
        print("f Sistema Informatico {self.sistema_informatico}")
        print("f Nombre Banco {self.nombre_banco}") 
        print("f No. Cajeros {self.no_cajeros}")
        print("f Fiable {self.fiable}")
        print("f Capital {self.capital}")
        print("f Horario Atencion {self.horario_atencion}")
        print("f Color Banco {self.color_banco}")
acme=banco("1000 clientes", "none", "none", "ACME Banking System", "Banco Acme", "1000", "True", "$1,000,000,000", "9am-19pm", "Verde Fosforecente")