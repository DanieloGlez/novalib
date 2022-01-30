from sqlalchemy import Column, String, Integer
from .base import Base


class Rol(Base):
    __tablename__ = 'f_rol'

    id_rol = Column(Integer, primary_key=True)
    nom_rol = Column(String)