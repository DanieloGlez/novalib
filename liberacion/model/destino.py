from sqlalchemy import Column, String, Integer
from .base import Base


class Destino(Base):
    __tablename__ = 'destino'

    id_destino = Column(Integer, primary_key=True)
    nom_destino = Column(String)

    def __init__(self, nom_destino):
        self.nom_destino = nom_destino
