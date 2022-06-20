

from dao.personaDao import PersonaDAO as pd

class Persona:
    
    def __init__(self, name, email) -> None:
        self.__id = 0
        self.__name = name
        self.__email = email
    
    @property
    def name(self):
        return self.__name
    
    @property
    def email(self):
        return self.__email
    
    @property
    def id(self):
        return self.__id
    
    @name.setter
    def name(self, n):
        assert isinstance(n, str), "El nombre debe ser un texto"
        self.__name = n
        return self.__name
    
    @email.setter
    def email(self, e:int):
        assert isinstance(e, str), "El email tiene que ser un texto"
        self.__email = e
        return self.__email
    
    @id.setter
    def id(self, id:int):
        self.__id = id
        return self.__id
    
    @classmethod
    def createTable(self, sentencia):
        pd.createTable(sentencia)
    
    def insert(self):
        datos = (self.__name, self.__email)
        id = pd.insertPersona(datos)
        self.__id = id
        return id
    
    def update(self, datos):
        return pd.update(datos, self.__id)
    
    def delete(self):
        return pd.delete(self.__id)
    
    @classmethod
    def drop(self):
        return pd.drop()
    
    @classmethod
    def truncate(self):
        return pd.truncate()
    
    @classmethod
    def select(self):
        pd.select()