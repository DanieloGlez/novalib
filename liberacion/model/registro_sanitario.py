from sqlalchemy import Column, String, Integer
from .base import Base


class RegistroSanitario(Base):
    __tablename__ = 'registro_sanitario'

    id_registro_sanitario = Column(Integer, primary_key=True)
    cod_registro_sanitario = Column(String)

    def __init__(self, cod_registro_sanitario):
        self.cod_registro_sanitario = cod_registro_sanitario
