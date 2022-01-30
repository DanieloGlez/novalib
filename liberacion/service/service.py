from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import *


engine = create_engine('postgresql://postgres:postgres@localhost:5432/bd_liberacion')
Session = sessionmaker(bind=engine)
session = Session()


class UsuarioService:
    @staticmethod
    def get_by_alias(alias):
        return session.query(Usuario).filter_by(alias=alias).first()

    @staticmethod
    def get_all():
        return session.query(Usuario).all()