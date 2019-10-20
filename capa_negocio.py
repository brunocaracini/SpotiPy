from capa_datos import DatosUser
import json


class NegocioUser(object):

    MIN_CAR_PSW = 5
    MAX_CAR_PSW = 10

    def __init__(self):
        self.datos = DatosUser()

    def jsonDataOpen(self, accion):
        if accion == 'login':
            with open('user_data.txt') as json_file:
                user_data = json.load(json_file)
            usuario = user_data['usuario']
            password = user_data['password']
            return usuario, password
        
        elif accion == 'signup':
            with open('user_data_signup.txt') as json_file:
                user_data_signup = json.load(json_file)
            usuario = user_data_signup['usuario']
            password = user_data_signup['password']
            uri = user_data_signup['uri']
            nombre = user_data_signup['nombre']
            return usuario, password, uri, nombre


    def jsonDataReturn(self, usuario, password, estado, uri, nombre, accion):
        if accion == 'login':
            user_data={
                'usuario': usuario,
                'password': password,
                'estado': estado
            }
            with open('user_data.txt', 'w') as outfile:
                json.dump(user_data, outfile)

        if accion == 'signup':
            user_data_signup={
            'usuario': usuario,
            'password': password,
            'estado': estado,
            'uri': uri,
            'nombre': nombre
            }

        with open('user_data_signup.txt', 'w') as outfile:
                json.dump(user_data_signup, outfile)

    def buscarUsuario(self, id):
        return self.datos.buscarUsuario(id)


    def validarUsuario(self, email, psw):
        '''Devuelve la instancia del usuario, dado su email y contraseña.
        Retorna None si no lo encuentra, True si pasa el login y False si la contraseña es incorrecta'''

        return self.datos.validarUsuario(email, psw)


    def altaUsuario(self, email, nombre, psw, uri):
        '''Da de alta un usuario, se debe validar que el usuario no exista (reglaValidacionUsuario),
        que la contraseña pase el min y max de caracteres (reglaLongitudContrasenia) y
        además que el email sea una dirección valida (reglaValidacionEmail).
        Retorna True si el alta fue exitoso, y se deben levantar excepciones por validaciones no pasadas'''


        if (self.reglaValidacionUsuario(email, psw) == True):
            return 'Este usuario ya existe' 
        elif (self.reglaLongitudContrasenia(psw) == False):
            return 'Longitud de contraseña incorrecta'
        elif (self.reglaValidacionEmail(email) == False):
            return 'Error - Solo se aceptan Gmail o Hotmail'
        else:
            self.datos.agregarUsuario(email, nombre, psw, uri)
            return 'ok'

    def modificacion(self, id, email, nombre, psw, uri):
        '''Modifica un usuario. Se debe validar que el usuario exista primero.
        Retorna True si la modificación fue exitosa y se debe levantar excepción si no pasa la validación.'''
        us  = self.buscarUsuario(id)
        if  us == False:
            return False
        else:
            return self.datos.actualizarUsuario(id, email, nombre, psw, uri)


    def reglaValidacionUsuario(self, email, psw):
        '''Validar que el usuario exista para el login mediante email y contraseña.
        Retorna un boolean según la condición correspondiente.
        OJO AGREGAR RAISE EXCEPTION CORRESPONDIENTE'''

        us = self.validarUsuario(email, psw)

        if us is None:
            return False #Este falso es porque usuario no existe hay que registrarse (usar Raise UsuarioInexistente)

        if us == True:
            return True #Este retorna que existe, pasa el login
        else:
            return False #Este falso es porque la contraseña es incorrecta (usar Raise ContraseniaInvalida)


    def reglaLongitudContrasenia(self, psw):
        '''Validar que la contraseña tenga una longitud entre los valores MIN_CAR_PSW y MAX_CAR_PSW.
        Retorna un boolean según la condición correspondiente.
        OJO AGREGAR RAISE EXCEPTION CORRESPONDIENTE'''

        if (len(psw) >= self.MIN_CAR_PSW) and (len(psw) <= self.MAX_CAR_PSW):
            return True
        else:
            return False #(usar Raise LongContraseñaInvalida)


    def reglaValidacionEmail(self, email):
        '''Validar que el mail sea una dirección válida, es decir, que posea el dominio @gmail.com o @hotmail.com.
        Retorna un boolean según la condición correspondiente.
        OJO AGREGAR RAISE EXCEPTION CORRESPONDIENTE'''

        if (email.find('@gmail.com') != -1) or (email.find('@hotmail.com') != -1):
            return True
        else:
            return False #Este es falso porque el email no tiene dominio valido (usar Raise EmailInvalido)

