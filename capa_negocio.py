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

        elif accion == 'geturi':
            with open('user_uri.txt') as json_file:
                user_uri = json.load(json_file)
            usuario = user_uri['usuario']
            return usuario

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
        
        if accion == 'geturi':
            user_uri = {
                'usuario': usuario,
                'uri':uri
            }
        with open('user_uri.txt', 'w') as outfile:
                json.dump(user_uri, outfile)

    def buscarURI(self, email):
        return self.datos.buscarURI(email)


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
            elif self.reglaValidacionEmail(email) != True:
                    return self.reglaValidacionEmail(email)
            else:
                return self.datos.agregarUsuario(email, nombre, psw, uri)
        else:
            return self.buscarUsuario(email, uri)



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
            if ((email.find('@') < 3) or (len(email) > 30)):
                return 'Longitud invalida o faltan caracteres delante del dominio'
            else:
                return True
        else:
            return 'Solo se aceptan dominios Gmail o Hotmail'



