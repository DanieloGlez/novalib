from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Float, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship


BaseORM = declarative_base()


class Aprobador(BaseORM):
    __tablename__ = 'aprobador'

    id_aprobador = Column(Integer, primary_key=True)
    nom_aprobador = Column(String)
    id_cargo = Column(Integer, ForeignKey('cargo.id_cargo'))

    # relationships
    cargo = relationship('Cargo', uselist=False)

    def __init__(self, nom_aprobador, cargo):
        self.nom_aprobador = nom_aprobador
        self.cargo = cargo


class Cargo(BaseORM):
    __tablename__ = 'cargo'

    id_cargo = Column(Integer, primary_key=True)
    nom_cargo = Column(String)

    def __init__(self, nom_cargo):
        self.nom_cargo = nom_cargo


class ClaveDeProducto(BaseORM):
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


class CondicionDeAlmacenamiento(BaseORM):
    __tablename__ = 'condicion_de_almacenamiento'

    id_condicion_de_almacenamiento = Column(Integer, primary_key=True)
    info_condicion_de_almacenamiento = Column(String)

    def __init__(self, info_condicion_de_almacenamiento):
        self.info_condicion_de_almacenamiento = info_condicion_de_almacenamiento


class Decision(BaseORM):
    __tablename__ = 'decision'

    id_decision = Column(Integer, primary_key=True)
    nom_decision = Column(String)

    def __init__(self, nom_decision):
        self.nom_decision = nom_decision


class Destino(BaseORM):
    __tablename__ = 'destino'

    id_destino = Column(Integer, primary_key=True)
    nom_destino = Column(String)

    def __init__(self, nom_destino):
        self.nom_destino = nom_destino


class FormaFarmaceutica(BaseORM):
    __tablename__ = 'forma_farmaceutica'

    id_forma_farmaceutica = Column(Integer, primary_key=True)
    nom_forma_farmaceutica = Column(String)

    def __init__(self, nom_forma_farmaceutica):
        self.nom_forma_farmaceutica = nom_forma_farmaceutica


class Liberador(BaseORM):
    __tablename__ = 'liberador'

    id_liberador = Column(Integer, primary_key=True)
    nom_liberador = Column(String)
    id_cargo = Column(Integer, ForeignKey('cargo.id_cargo'))

    # relationships
    cargo = relationship('Cargo', uselist=False)

    def __init__(self, nom_liberador, cargo):
        self.nom_liberador = nom_liberador
        self.cargo = cargo


class Lote(BaseORM):
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


class NumeroDeParte(BaseORM):
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


class Pendiente(BaseORM):
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


class Presentacion(BaseORM):
    __tablename__ = 'presentacion'

    id_presentacion = Column(Integer, primary_key=True)
    info_presentacion = Column(String)

    def __init__(self, info_presentacion):
        self.info_presentacion = info_presentacion


class Producto(BaseORM):
    __tablename__ = 'producto'

    id_producto = Column(Integer, primary_key=True)
    nom_producto = Column(String)

    def __init__(self, nom_producto):
        self.nom_producto = nom_producto


class RegistroSanitario(BaseORM):
    __tablename__ = 'registro_sanitario'

    id_registro_sanitario = Column(Integer, primary_key=True)
    cod_registro_sanitario = Column(String)

    def __init__(self, cod_registro_sanitario):
        self.cod_registro_sanitario = cod_registro_sanitario


class Usuario(BaseORM):
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


class Rol(BaseORM):
    __tablename__ = 'f_rol'

    id_rol = Column(Integer, primary_key=True)
    nom_rol = Column(String)
