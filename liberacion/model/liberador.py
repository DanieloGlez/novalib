from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Liberador(Base):
    __tablename__ = 'liberador'

    id_liberador = Column(Integer, primary_key=True)
    nom_liberador = Column(String)
    id_cargo = Column(Integer, ForeignKey('cargo.id_cargo'))

    # relationships
    cargo = relationship('Cargo', uselist=False)

    def __init__(self, nom_liberador, cargo):
        self.nom_liberador = nom_liberador
        self.cargo = cargo
