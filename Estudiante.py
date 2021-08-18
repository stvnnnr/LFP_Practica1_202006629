class Estudiante():
    nombre = ""
    calificacion = ""

    def __init__(self , nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion

    def get_name(self):
        return self.nombre
    
    def get_nota(self):
        return self.calificacion