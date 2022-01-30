from sqlalchemy import Column, String, Integer
from .base import Base


class Presentacion(Base):
    __tablename__ = 'presentacion'

    id_presentacion = Column(Integer, primary_key=True)
    info_presentacion = Column(String)

    def __init__(self, info_presentacion):
        self.info_presentacion = info_presentacion
