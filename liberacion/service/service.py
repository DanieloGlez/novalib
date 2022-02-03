from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import *
from util import config


# create engine and season
engine = create_engine(
    f'postgresql://{config["db.username"]}:{config["db.password"]}@{config["db.host"]}:{config["db.port"]}/{config["db"]}')
Session = sessionmaker(bind=engine)
session = Session()


class UsuarioService:
    @staticmethod
    def get_by_alias(alias):
        return session.query(Usuario).filter_by(alias=alias).first()

    @staticmethod
    def get_all():
        return session.query(Usuario).all()
