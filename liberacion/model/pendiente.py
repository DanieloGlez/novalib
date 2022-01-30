from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Pendiente(Base):
    __tablename__ = 'pendiente'

    id_lote = Column(Integer, ForeignKey('lote.id_lote'), primary_key=True)
    rmf_cp = Column(Date)
    rme = Column(Date)
    ri = Column(Date)
    me = Column(Date)
    rta = Column(Date)
    observaciones = Column(String)

    # relationships
    lote = relationship('Lote', uselist=False)

    def __init__(self, lote, rmf_cp, rme, ri, me, rta, observaciones):
        self.lote = lote
        self.rmf_cp = rmf_cp
        self.rme = rme
        self.ri = ri
        self.me = me
        self.rta = rta
        self.observaciones = observaciones