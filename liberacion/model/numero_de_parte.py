from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class NumeroDeParte(Base):
    __tablename__ = 'numero_de_parte'

    id_numero_de_parte = Column(Integer, primary_key=True)
    cod_numero_de_parte = Column(Integer)
    id_clave_de_producto = Column(Integer, ForeignKey(
        'clave_de_producto.id_clave_de_producto'))
    id_presentacion = Column(Integer, ForeignKey(
        'presentacion.id_presentacion'))
    id_destino = Column(Integer, ForeignKey('destino.id_destino'))
    id_registro_sanitario = Column(Integer, ForeignKey(
        'registro_sanitario.id_registro_sanitario'))
    id_condicion_de_almacenamiento = Column(Integer, ForeignKey(
        'condicion_de_almacenamiento.id_condicion_de_almacenamiento'))
    tiempo_de_validez = Column(Integer)

    # relationships
    clave_de_producto = relationship('ClaveDeProducto', uselist=False)
    presentacion = relationship('Presentacion', uselist=False)
    destino = relationship('Destino', uselist=False)
    registro_sanitario = relationship('RegistroSanitario', uselist=False)
    condicion_de_almacenamiento = relationship(
        'CondicionDeAlmacenamiento', uselist=False)

    def __init__(self, cod_numero_de_parte, clave_de_producto, presentacion, destino, registro_sanitario, condicion_de_almacenamiento):
        self.cod_numero_de_parte = cod_numero_de_parte
        self.clave_de_producto = clave_de_producto
        self.presentacion = presentacion
        self.destino = destino
        self.registro_sanitario = registro_sanitario
        self.condicion_de_almacenamiento = condicion_de_almacenamiento
