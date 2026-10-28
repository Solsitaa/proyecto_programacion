import MySQLdb
from MySQLdb.connections import Connection
from abc import ABC, abstractmethod

DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = ""
DB_NAME = "echotech_db"

class Conexion:
    __instancia = None
    __conexion = None

    def __new__(cls):
        if cls.__instancia is None:
            cls.__instancia = super(Conexion, cls).__new__(cls)
        return cls.__instancia

    def __init__(self):
        if self.__conexion is None:
            self.__conexion = MySQLdb.connect(
                host=DB_HOST, user=DB_USER, passwd=DB_PASS, db=DB_NAME
            )

    def obtener_conexion(self) -> Connection:
        return self.__conexion

# from abc import ABC, abstractmethod
class ActiveRecord(ABC):

    @abstractmethod
    def guardar(self) -> None:
        pass

    @abstractmethod
    def actualizar(self) -> None:
        pass

    @abstractmethod
    def eliminar(self) -> None:
        pass

    @classmethod    
    @abstractmethod
    def buscar_por_id(cls, id: int):
        pass

    @classmethod
    @abstractmethod
    def buscar_todos(cls):
        pass
