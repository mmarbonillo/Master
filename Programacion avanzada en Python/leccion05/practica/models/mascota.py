
from dao.mascotaDao import MascotaDAO as md

class Mascota:
    
    def __init__(self, name, fechaNacimiento, tipo, personaId) -> None:
        self.__id = 0
        self.__name = name
        self.__fechaNacimiento = fechaNacimiento
        self.__tipo = tipo
        self.__personaId = personaId
    
    @property
    def name(self):
        return self.__name
    
    @property
    def fechaNacimiento(self):
        return self.__fechaNacimiento
    
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def personaId(self):
        return self.__personaId
    
    @property
    def id(self):
        return self.__id
    
    @name.setter
    def name(self, n):
        assert isinstance(n, str), "El nombre debe ser un texto"
        self.__name = n
        return self.__name
    
    @fechaNacimiento.setter
    def fechaNacimiento(self, fechaNacimiento:int):
        assert isinstance(fechaNacimiento, str), "La fecha de nacimiento debe ser un texto"
        self.__fechaNacimiento = fechaNacimiento
        return self.__fechaNacimiento
    
    @tipo.setter
    def tipo(self, tipo:int):
        assert isinstance(tipo, str), "La fecha de nacimiento debe ser un texto"
        self.__tipo = tipo
        return self.__tipo
    
    @personaId.setter
    def personaId(self, personaId:int):
        self.__personaId = personaId
        return self.__personaId
    
    @id.setter
    def id(self, id:int):
        self.__id = id
        return self.__id
    
    @classmethod
    def createTable(self, sentencia):
        md.createTable(sentencia)
    
    def insert(self):
        datos = (self.__name, self.__fechaNacimiento, self.__tipo, self.__personaId)
        id = md.insertMascotas(datos)
        self.__id = id
        return id
    
    def update(self, datos):
        return md.update(datos, self.__id)
    
    def delete(id):
        return md.delete(id)
    
    @classmethod
    def drop(self):
        return md.drop()
    
    @classmethod
    def truncate(self):
        return md.truncate()
    
    @classmethod
    def select(self):
        md.select()