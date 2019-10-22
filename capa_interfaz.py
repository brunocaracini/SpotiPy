from capa_negocio import NegocioUser
import os
import sys

#accion = sys.argv[1]
accion = 'signup'




if accion == 'login':
    usuario, password = NegocioUser().jsonDataOpen(accion)
    estado = NegocioUser().validarUsuario(usuario, password)
    NegocioUser().jsonDataReturn(usuario, password, estado, None, None, accion)

elif accion == 'signup':
    usuario, password, uri, nombre = NegocioUser().jsonDataOpen(accion)
    estado = NegocioUser().altaUsuario(usuario, nombre, password, uri)
    NegocioUser().jsonDataReturn(usuario, password, estado, uri, nombre, accion)


