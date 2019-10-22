from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from connection_DB import Base, User, crearTabla
import json


class DatosUser(object):

    def __init__(self):

        engine = create_engine('sqlite:///soporte-practico-08.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker()
        DBSession.bind = engine
        self.session = DBSession()

    def agregarUsuario(self, email, nombre, psw, uri):

        us = User()
        us.emailUsuario = email
        us.nombreUsuario = nombre
        us.passwordUsuario = psw
        us.uriUsuario = uri
        self.session.add(us)
        self.session.commit()
        return 'ok'


    def validarUsuario(self, email, psw):

        user = self.session.query(User).filter_by(emailUsuario=email).first()

        if user is None:
            return 'Usuario inexistente'

        if user.passwordUsuario == psw:
            return 'ok'
        else:
            return 'Contraseña incorrecta'


    def buscarUsuario(self, email, uri):
        us_email = self.session.query(User).filter_by(emailUsuario=email).first()
        us_uri = self.session.query(User).filter_by(uriUsuario=uri).first()
        if us_email is not None:
            return 'Existe un usuario registrado con ese email'
        elif us_uri is not None:
            return 'Existe un usuario registrado con esa uri'
        elif us_email is None and us_uri is None:
            return 'ok'


    def actualizarUsuario(self, id, email, nombre, psw, uri):
        self.session.query(User).filter_by(idUsuario=id).update({User.emailUsuario:email, User.nombreUsuario:nombre, User.passwordUsuario:psw, User.uriUsuario:uri})
        self.session.commit()
        return True


   


