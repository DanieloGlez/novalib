from sqlalchemy import Column, String, Integer
from .base import Base


class Decision(Base):
    __tablename__ = 'decision'

    id_decision = Column(Integer, primary_key=True)
    nom_decision = Column(String)

    def __init__(self, nom_decision):
        self.nom_decision = nom_decision
