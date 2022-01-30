from sqlalchemy import Column, String, Integer
from .base import Base


class CondicionDeAlmacenamiento(Base):
    __tablename__ = 'condicion_de_almacenamiento'

    id_condicion_de_almacenamiento = Column(Integer, primary_key=True)
    info_condicion_de_almacenamiento = Column(String)

    def __init__(self, info_condicion_de_almacenamiento):
        self.info_condicion_de_almacenamiento = info_condicion_de_almacenamiento
