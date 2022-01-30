from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class ClaveDeProducto(Base):
    __tablename__ = 'clave_de_producto'

    id_clave_de_producto = Column(Integer, primary_key=True)
    cod_clave_de_producto = Column(Integer)
    id_producto = Column(Integer, ForeignKey('producto.id_producto'))
    id_forma_farmaceutica = Column(Integer, ForeignKey(
        'forma_farmaceutica.id_forma_farmaceutica'))

    # relationships
    producto = relationship('Producto', uselist=False)
    forma_farmaceutica = relationship('FormaFarmaceutica', uselist=False)

    def __init__(self, cod_clave_de_producto, producto, forma_farmaceutica):
        self.cod_clave_de_producto = cod_clave_de_producto
        self.producto = producto
        self.forma_farmaceutica = form
