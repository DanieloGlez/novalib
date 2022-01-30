from sqlalchemy import Column, String, Integer
from .base import Base


class Cargo(Base):
    __tablename__ = 'cargo'

    id_cargo = Column(Integer, primary_key=True)
    nom_cargo = Column(String)

    def __init__(self, nom_cargo):
        self.nom_cargo = nom_cargo
