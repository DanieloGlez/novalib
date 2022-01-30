from sqlalchemy import Column, String, Integer
from .base import Base


class Producto(Base):
    __tablename__ = 'producto'

    id_producto = Column(Integer, primary_key=True)
    nom_producto = Column(String)

    def __init__(self, nom_producto):
        self.nom_producto = nom_producto
