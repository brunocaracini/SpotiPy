from capa_negocio import NegocioUser
import os
import sys

accion = sys.argv[1]


if accion == 'login':
    usuario, password = NegocioUser().jsonDataOpen(accion)
    estado = NegocioUser().validarUsuarioLogin(usuario, password)
    NegocioUser().jsonDataReturn(usuario, password, estado, None, None, accion)

elif accion == 'signup':
    usuario, password, uri, nombre = NegocioUser().jsonDataOpen(accion)
    estado = NegocioUser().altaUsuario(usuario, nombre, password, uri)
    NegocioUser().jsonDataReturn(usuario, password, estado, uri, nombre, accion)

elif accion == 'geturi':
    usuario = NegocioUser().jsonDataOpen(accion)
    uri = NegocioUser().buscarURI(usuario)
    nombre = NegocioUser().buscarNombre(usuario)
    NegocioUser().jsonDataReturn(usuario, None, None, uri, nombre, accion)
