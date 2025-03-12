
class Usuario:
    def __init__(self, id=None, nombre="", email="", edad=0):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.edad = edad
    
    def __str__(self):
        return f"Usuario(id={self.id}, nombre='{self.nombre}', email='{self.email}', edad={self.edad})"