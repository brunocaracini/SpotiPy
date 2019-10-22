from capa_datos import DatosUser
import json


class NegocioUser(object):

    MIN_CAR_PSW = 8
    MAX_CAR_PSW = 20

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


    def buscarUsuario(self, email, uri):
        return self.datos.buscarUsuario(email, uri)


    def validarUsuarioLogin(self, email, psw):
        '''Devuelve la instancia del usuario, dado su email y contraseña.
        Retorna None si no lo encuentra, True si pasa el login y False si la contraseña es incorrecta'''

        return self.datos.validarUsuario(email, psw)


    def altaUsuario(self, email, nombre, psw, uri):
        '''Da de alta un usuario, se debe validar que el usuario no exista (reglaValidacionLogin),
        que la contraseña pase el min y max de caracteres (reglaLongitudContrasenia) y
        además que el email sea una dirección valida (reglaValidacionEmail).
        Retorna True si el alta fue exitoso, y se deben levantar excepciones por validaciones no pasadas'''

        if self.buscarUsuario(email, uri) == 'ok':
            if self.reglaLongitudContrasenia(psw) == False:
                return 'Longitud de contraseña invalida'
            elif self.reglaValidacionEmail(email) == False:
                    return 'Solo se aceptan Gmail o Hotmail'
            else:
                return self.datos.agregarUsuario(email, nombre, psw, uri)
        else:
            return self.buscarUsuario(email, uri)



    def modificacion(self, id, email, nombre, psw, uri):
        '''Modifica un usuario. Se debe validar que el usuario exista primero.
        Retorna True si la modificación fue exitosa y se debe levantar excepción si no pasa la validación.'''
        us  = self.buscarUsuario(id)
        if  us == False:
            return False
        else:
            return self.datos.actualizarUsuario(id, email, nombre, psw, uri)


    def reglaValidacionSignUp(self, email, uri):
        '''Validar que el usuario no existe previamente antes del registro y que la URI no sea duplicada'''
        return self.buscarUsuario(email, uri)




    def reglaValidacionLogin(self, email, psw):
        '''Validar que el usuario exista para el login mediante email y contraseña.
        Retorna un error en caso de no pasar la validación.'''

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
            return False


    def reglaValidacionEmail(self, email):
        '''Validar que el mail sea una dirección válida, es decir, que posea el dominio @gmail.com o @hotmail.com.
        Retorna un boolean según la condición correspondiente.
        OJO AGREGAR RAISE EXCEPTION CORRESPONDIENTE'''

        if (email.find('@gmail.com') != -1) or (email.find('@hotmail.com') != -1):
            return True
        else:
            return False

