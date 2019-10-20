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

    def agregarUsuario(self, usuario, nombre, psw, uri):

        us = User()
        us.usuario = usuario
        us.nombreUsuario = nombre
        us.passwordUsuario = psw
        us.uriUsuario = uri
        self.session.add(us)
        self.session.commit()
        return True
    '''En el return de arriba, no sabiamos que datos querías devolver, 
        te puse que retorne la primary key de la tabla pero podes devolver us (que es la instancia us)'''

    def validarUsuario(self, usuario, psw):

        user = self.session.query(User).filter_by(usuario=usuario).first()

        if user is None:
            return 'Usuario inexistente'

        if user.passwordUsuario == psw:
            return 'ok'
        else:
            return 'Contraseña incorrecta'


    def buscarUsuario(self, id):
        user = self.session.query(User).filter_by(idUsuario=id).first()
        if user is None:
            return False
        else:
            return user


    def actualizarUsuario(self, id, usuario, nombre, psw, uri):
        self.session.query(User).filter_by(idUsuario=id).update({User.usuario:usuario, User.nombreUsuario:nombre, User.passwordUsuario:psw, User.uriUsuario:uri})
        self.session.commit()
        return True


   


