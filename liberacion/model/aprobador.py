from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Aprobador(Base):
    __tablename__ = 'aprobador'

    id_aprobador = Column(Integer, primary_key=True)
    nom_aprobador = Column(String)
    id_cargo = Column(Integer, ForeignKey('cargo.id_cargo'))

    # relationships
    cargo = relationship('Cargo', uselist=False)

    def __init__(self, nom_aprobador, cargo):
        self.nom_aprobador = nom_aprobador
        self.cargo = cargo
