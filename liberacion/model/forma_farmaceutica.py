from sqlalchemy import Column, String, Integer
from .base import Base


class FormaFarmaceutica(Base):
    __tablename__ = 'forma_farmaceutica'

    id_forma_farmaceutica = Column(Integer, primary_key=True)
    nom_forma_farmaceutica = Column(String)

    def __init__(self, nom_forma_farmaceutica):
        self.nom_forma_farmaceutica = nom_forma_farmaceutica
