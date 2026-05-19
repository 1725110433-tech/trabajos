class Alumno:
    def __init__(self, matricula, materias, nombre, carrera, altura, edad, promedio, sexo, nivel_estudio, uniforme):
        self.matricula = matricula
        self.materias = materias
        self.nombre = nombre 
        self.carrra = carrera
        self.altura = altura 
        self.edad = edad
        self.promedio = promedio
        self.sexo = sexo
        self.nivel_estudio = nivel_estudio 
        self.uniforme = uniforme
        print(f" su matricula es {self.matricula}")
        print(f" las materias son{self.materias}")  
        print(f" su nombre es  {self.nombre}") 
        print(f"su carrera es  {self.carrera}")
        print(f"su altura es {self.altura}")  
        print(f"su edad es {self.edad}")
        print(f"su promedio es  {self.promedio}")
        print(f"su sexo es {self.sexo}")
        print(f"su nivel de estudio es  {self.nivel_estudio}")    
        print(f"lleva uniforme  {self.unifrome }") 
mencho = Alumno("1725110433","matematicas","mencho","tics","19","8.0","Masculino","Universiodad","no")