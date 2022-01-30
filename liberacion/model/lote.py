from sqlalchemy import Column, String, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Lote(Base):
    __tablename__ = 'lote'

    id_lote = Column(Integer, primary_key=True)
    cod_lote = Column(String)
    id_numero_de_parte = Column(Integer, ForeignKey(
        'numero_de_parte.id_numero_de_parte'))
    fecha_produccion = Column(Date)
    rend_kg = Column(Float)
    rend_env_primario = Column(Float)
    rend_uf = Column(Float)
    ccc = Column(Float)
    id_decision = Column(Integer, ForeignKey('decision.id_decision'))
    fecha_decision = Column(Date)
    id_liberador = Column(Integer, ForeignKey('liberador.id_liberador'))
    id_aprobador = Column(Integer, ForeignKey('aprobador.id_aprobador'))
    observaciones = Column(String)

    # relationships
    numero_de_parte = relationship('NumeroDeParte', uselist=False)
    decision = relationship('Decision', uselist=False)
    liberador = relationship('Liberador', uselist=False)
    aprobador = relationship('Aprobador', uselist=False)

    def __init__(self, cod_lote, numero_de_parte, fecha_produccion, rend_kg, rend_env_primario, rend_uf, ccc, decision, fecha_decision, liberador, aprobador, observaciones):
        self.cod_lote = cod_lote
        self.numero_de_parte = numero_de_parte
        self.fecha_produccion = fecha_produccion
        self.rend_kg = rend_kg
        self.rend_env_primario = rend_env_primario
        self.rend_uf = rend_uf
        self.ccc = ccc
        self.decision = decision
        self.fecha_decision = fecha_decision
        self.liberador = liberador
        self.aprobador = aprobador
        self.observaciones = observaciones
