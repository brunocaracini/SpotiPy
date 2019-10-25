from sqlalchemy import Column, INTEGER, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):

    __tablename__ = 'user'
    idUsuario = Column(INTEGER, primary_key=True, autoincrement=True)
    emailUsuario = Column(VARCHAR(30), unique=True, nullable=False)
    nombreUsuario = Column(VARCHAR(50))
    passwordUsuario = Column(VARCHAR(10), nullable=False)
    uriUsuario = Column(VARCHAR(30), unique=True, nullable=False)


engine = create_engine('sqlite:///soporte-practico-08.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


def crearTabla():
    Base.metadata.create_all(engine)


def borrarTabla():
    User.__table__.drop()
    
crearTabla()

