class libro_biblioteca:
    def __init__(self, titulo, autor, isbn, editorial, anio_publicacion, 
                 genero, num_paginas, idioma, estante, estado_disponible):

        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.editorial = editorial
        self.anio_publicacion = anio_publicacion
        self.genero = genero
        self.num_paginas = num_paginas
        self.idioma = idioma
        self.estante = estante
        self.estado_disponible = estado_disponible
        
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")
        print(f"Editorial: {self.editorial}")
        print(f"Año de Publicación: {self.anio_publicacion}")
        print(f"Género: {self.genero}")
        print(f"Número de Páginas: {self.num_paginas}")
        print(f"Idioma: {self.idioma}")
        print(f"Estante asignado: {self.estante}")
        print(f"Disponibilidad inicial: {self.estado_disponible}")

    def mostrar_disponibilidad(self): 
        print(f"El libro actualmente se encuentra: {self.estado_disponible}")

    def ubicacion(self): 
        print(f"Para buscar este libro, debes ir al estante {self.estante}")

    def origen(self): 
        print(f"Este texto fue escrito por {self.autor} ")

    def clasificacion(self): 
        print(f"La obra pertenece al género literario de {self.genero}")

    def ficha_tecnica(self): 
        print(f"El libro '{self.titulo}")


mi_libro = libro_biblioteca("Cien años de soledad", "Gabriel García Márquez", "978-0307474728", "Editorial Sudamericana", "1967", "Realismo Mágico", "496", "Español", "Pasillo B - Ficción", "Disponible para préstamo")

mi_libro.mostrar_disponibilidad()
mi_libro.ubicacion()
mi_libro.origen()
mi_libro.clasificacion()
mi_libro.ficha_tecnica()