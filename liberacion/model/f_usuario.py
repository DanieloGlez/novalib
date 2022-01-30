from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Usuario(Base):
    __tablename__ = 'f_usuario'

    id_usuario = Column(Integer, primary_key=True)
    nom_usuario = Column(String)
    alias = Column(String)
    contrasena = Column(String)
    id_rol = Column(Integer, ForeignKey('f_rol.id_rol'))
    activo = Column(Boolean)

    # relationships
    rol = relationship('Rol', uselist=False)

    def __init__(self, nom_usuario, alias, contrasena, rol, activo):
        self.nom_usuario = nom_usuario
        self.alias = alias
        self.contrasena = contrasena
        self.rol = rol
        self.activo = activo