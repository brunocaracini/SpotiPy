import json
import os

scroll = 0
estado = 0
usuario = ''
password = ''
password2 = ''
uri = ''
sp_user = False
user = False
passw = False
passw2 = False
log_in = False
sign_up = False
op1 =  False
op2 = False
op3 = False
op4 = False
op5 = False
op6 = False
error_window = False
error = ''

class Presentacion():
    
    def login(self):
        if usuario == '' and password == '':
            self.login_form()
        
    def login_form(self):
         
        image(back, 0, 0)
        
        #Cartel Iniciar Sesion o Registrese
        textSize(40)
        fill(90)
        text('Inicie Sesion', 550 , 200)
        
        #Recuadro ingreso usuario
        noStroke()
        photo = loadImage("user_icon.png")
        image(photo, 460, 397)
        fill(240, 50)
        if user:
            stroke(117,231,193)
        rect(445, 380, 450, 70)
        
        #Recuadro ingreso contraseña
        noStroke()
        photo = loadImage("password_icon.png")
        image(photo, 460, 487)
        fill(240, 50)
        if passw:
            stroke(117,231,193)
        rect(445, 470, 450, 70)
        
        #boton Log in
        noStroke()
        if len(usuario) == 0 or len(password) == 0:
            fill(90)
        elif log_in:
            fill (117,231,193, 250)
        else:
            fill (117,231,193, 150)
        rect(600,590,150,50,20)
        textSize(18)
        fill(255, 200)
        text('Log in', 650,620)
        
        #sign Up
        if sign_up:
            fill(117,231,193)
        else: 
            fill(255, 180)
        textSize(17)
        text('No estas registrado aun? Resgistrate aqui',490,567)

        #Error window
        if error_window:
            self.error_window_form()    
    
    
     
    def signup(self):
        if usuario == '' and password == '' and password2 == '' and uri == '':
            self.signup_form()
    
    def signup_form(self):
        image(back, 0, 0)
        
        #Cartel Registrese
        textSize(40)
        fill(90)
        text('Registrese', 550 , 100)
        
        #Recuadro ingreso usuario
        noStroke()
        photo = loadImage("user_icon.png")
        image(photo, 460, 217)
        fill(240, 50)
        if user:
            stroke(117,231,193)
        rect(445, 200, 450, 70)
       
        
        #Recuadro ingreso uri Spotify
        noStroke()
        fill(240, 50)
        photo = loadImage("spotify_icon.png")
        image(photo, 464, 309)
        if sp_user:
            stroke(117,231,193)
        rect(445, 290, 450, 70)
        
        #Recuadro ingreso contraseña
        noStroke()
        photo = loadImage("password_icon.png")
        image(photo, 460, 397)
        fill(240, 50)
        if passw:
           stroke(117,231,193)
        rect(445, 380, 450, 70)
        
        #Recuadro ingreso contraseña 2
        noStroke()
        photo = loadImage("password_icon.png")
        image(photo, 460, 487)
        fill(240, 50)
        if passw2:
           stroke(117,231,193)
        rect(445, 470, 450, 70)
        
        #boton Registrarse
        noStroke()
        if sign_up:
            fill (117,231,193, 250)
        else:
            fill (117,231,193, 150)
        rect(600,590,150,50,20)
        textSize(18)
        fill(255, 200)
        text('Sign up', 643,620)
        
        #Log In
        if log_in:
            fill(117,231,193)
        else: 
            fill(255,180)
        textSize(17)
        text('Ya posee una cuenta? Inicie sesion aqui',500,567)
        
        #Error window
        if error_window:
          self.error_window_form()  
    
        
    def menu_form(self):
        
        image(back, 0, 0)
        
        #Barra Lateral del menu
        fill(50, 200)
        rect(0,0,350,height)
        
        #Opcion 1: Mostrar tracks de una playlist en Spotify
        if op1:
            tint(117,231,193, 170)
            fill(117,231,193, 170)
        else:
            tint(255,180)
            fill(255,180)
        photo = loadImage("playlist_icon.png")
        image(photo, 602, 25)
        textSize(23)
        text("Spotify", 614, 150)
        text("Playlists", 607, 180)
        
        #Opcion 2: Buscar Videos de una PlayList
        if op2:
            tint(117,231,193, 170)
            fill(117,231,193, 170)
        else:
            tint(255,180)
            fill(255,180)
        photo = loadImage("videoSearch_icon.png")
        image(photo, 613, 263)
        textSize(23)
        text("Match videos", 587, 388)
        text("with playlists", 588, 418)
        
        #Opcion 3: Buscar video Lyrics desde una Playlist
        tint(255,180)
        photo = loadImage("videoSearch_icon.png")
        image(photo, 613, 490)
        textSize(23)
        fill(255,180)
        text("Lyrics videos", 587, 615)
        text("from playlists", 582, 645)
    
    
    def showTracks(self):
        image(back, 0, 0)
        with open('data.txt') as json_file:
            data = json.load(json_file)
        self.show_scroll_bar(data)
        self.header()
        fill (240)
        textSize(25)
        vposition = 270
        hposition_cancion = width/10
        hposition_artista = width-800
        text('Cancion', width/10, vposition - 20 + scroll)
        text('Artista', width-800, vposition - 20 + scroll)
        textSize(14)
        for track in data['tracks']:
                vposition +=50
                text(track['name'][0:50], hposition_cancion, vposition + scroll)                    
                text(track['artist'], hposition_artista, vposition + scroll)
    
    
    def error_window_form(self):
        global error
        fill(10,230)
        rect(0,0,width,height)
        fill(20,230)
        stroke(117,231,193)
        rect(405, 300, 520, 170)           
    
    
    def show_scroll_bar(self, data):
        fill (190)
        stroke (190)
        len_data = self.calcula_largo(data)
        rect (width - 20, 0 - scroll*len_data/(height), 10, (height + 5000)/len_data)


    def calcula_largo(self, data):
        len_data = 0
        for track in data['tracks']:
            len_data +=1
        print(len_data)
        return len_data
        
    
    def header(self):
        fill (45)
        stroke (45)
        rect(0,0+ scroll,width - 20,170)




app = Presentacion()


def reset():
    global usuario
    global password
    global password2
    global uri 
    global user
    global passw2
    global sp_user
    global passw
    global log_in
    global sign_up

    sign_up = False
    log_in = False
    user = False
    passw = False
    passw2 = False
    sp_user = False
    usuario = ''
    password = ''
    password2 = ''
    uri = ''


def verifica_input(key_):
    verifica_input = False
    if key_ == 65535:
        str(key_)[:1]
    elif ((int(ord(key_)) >= 64 and int(ord(key_)) <= 90) or (int(ord(key_)) >= 97 and int(ord(key_)) <= 122) or int(ord(key_)) == 95 or int(ord(key_)) == 45 or int(ord(key_)) == 43 or int(ord(key_)) == 46):
        verifica_input = True
    elif (int(ord(key_)) >= 48 and int(ord(key_)) <= 57): 
        verifica_input = True
    return verifica_input
    


def printText():
    global usuario
    global password
    global uri
    global password2
    global error_window
    global error
    
    if estado == 0:
        app.login_form()
        fill(240)
        if error_window == False:
            text(usuario, 530 , 422)
            text(password, 530 , 512)
        else:
            fill(240, 240)
            text("Error: " + error, 565, 450)
    
    elif estado == 1:
        app.signup_form()
        fill(240)
        text(usuario, 530 , 242)
        text(uri, 530 , 332)
        text(password, 530 , 422)
        text(password2, 530 , 512)
    
    elif estado == 2:
        app.menu_form()

    
def setup():
    global back
    size (1365, 700)
    back = loadImage("fondo2.jpg")
    image(back, 0, 0)
    strokeWeight(2)

    
def mouseWheel(event):
    global scroll
    e = event.getCount()
    if scroll == 0:
        if event.getCount() >=0:
            scroll -= event.getCount() * 50
    else:
        scroll -= event.getCount() * 50


def keyPressed():
    global estado
    global usuario
    global password
    global password2
    global uri
    global user
    global passw
    global passw2
    global sp_user
    
    
    if estado == 0:
        textSize(18)
        if user and verifica_input(key):
            usuario += str(key)
        elif user and (key == BACKSPACE) and len(usuario)>0:
            usuario = usuario[:-1]  
        if passw and verifica_input(key):
            password += str(key)
        elif passw and (key == BACKSPACE) and len(password)>0:
            password = password[:-1]  
    
    
    if estado == 1:
        textSize(18)
        
        if user and verifica_input(key):
            usuario += str(key)
        elif user and (key == BACKSPACE) and len(usuario)>0:
            usuario = usuario[:-1]  
        
        if passw and verifica_input(key):
            password += str(key)
        elif passw and (key == BACKSPACE) and len(password)>0:
            password = password[:-1] 
        
        if passw2 and verifica_input(key):
            password2 += str(key)
        elif passw2 and (key == BACKSPACE) and len(password2)>0:
            password2 = password2[:-1]  
        
        if sp_user and verifica_input(key):
            uri += str(key)
        elif sp_user and (key == BACKSPACE) and len(uri)>0:
            uri = uri[:-1]  
            
        
        
    printText()    
        

def mouseClicked():
    global user
    global passw
    global passw2
    global estado
    global log_in
    global sign_up
    global sp_user
    
    if estado == 0:
        #Resalta borde ingreso usuario
        if mouseX >= 445 and mouseX <=895 and mouseY >=380 and mouseY <= 450:
            passw = False
            log_in = False
            user = True
            printText()
        
        #Resalta borde ingreso Contraseña
        elif mouseX >= 445 and mouseX <=895 and mouseY >=470 and mouseY <= 540:
            user = False
            log_in = False
            passw = True
            printText()
            
        #Ejecuta .py de validacion del login y cambia estado a 2 (Menu de opciones)
        elif mouseX >= 600 and mouseX <=750 and mouseY >=590 and mouseY <= 640 and len(usuario) > 0 and len(password) > 0:
            printText()
            exporta_json()
            if importa_json():
                estado = 2
        
        #Cambia estado a Registrarse
        elif mouseX>= 470 and mouseX<= 835 and mouseY>= 545 and mouseY <= 579:
            estado = 1
            sign_up = False
            reset()
    
    elif estado == 1:
        
        #Resalta borde ingreso usuario
        if mouseX >= 445 and mouseX <=895 and mouseY >=200 and mouseY <= 290:
            passw = False
            passw2 = False
            sp_user = False
            user = True
            printText()

        #Resalta borde ingreso uri Spotify
        if mouseX >= 445 and mouseX <=895 and mouseY >=290 and mouseY <= 360:
            sp_user = True
            passw = False
            passw2 = False
            user = False
            printText()
        
        #Resalta borde ingreso contraseña 1
        if mouseX >= 445 and mouseX <=895 and mouseY >=380 and mouseY <= 450:
            passw = True
            passw2 = False
            user = False
            sp_user = False
            printText()
        
        #Resalta borde ingreso Contraseña 2
        elif mouseX >= 445 and mouseX <=895 and mouseY >=470 and mouseY <= 540:
            user = False
            passw = False
            sp_user = False
            passw2 = True
            printText()
            
        #Ejecuta Registro y cambia estado a Log In (estado = 0)
        elif mouseX >= 600 and mouseX <=750 and mouseY >=590 and mouseY <= 640:
            exporta_json()
            estado = 0
        
        #Cambia estado a Registrarse
        elif mouseX>= 470 and mouseX<= 835 and mouseY>= 545 and mouseY <= 579:
            estado = 0
            reset()
        
    elif estado == 2:
        #Seleccion de opcion 1 (Buscar Playlists en Spotify)
        if (mouseX>= 600.5 and mouseX<= 700.5 and mouseY>= 25 and mouseY <= 125) or (mouseX>= 607 and mouseX<= 700 and mouseY>= 130 and mouseY <= 200):
            os.system("Python Obtener_canciones.py")
            estado = 3
    
    
def importa_json():
    global estado
    global error
    global error_window

    if estado == 0:
        with open('user_data.txt') as json_file:
            user_data = json.load(json_file)
        error = user_data['estado']
            
    elif estado == 1:
        with open('user_data_signup.txt') as json_file:
            user_data_signup = json.load(json_file)
        error = user_data_signup['estado']

    if error == 'ok':
        error_window = False
        return True
    else:
        error_window = True
        return False
                          
def exporta_json():
    global usuario
    global password
    global password2
    global uri
    global estado
    
    if estado == 0:
        user_data = {  
            'usuario': usuario,
            'password': password,
            'estado': ''
            }     
        with open('user_data.txt', 'w') as outfile:
            json.dump(user_data, outfile)
        os.system("Python capa_interfaz.py login") 
   
    elif estado == 1:
        user_data_signup = {  
                'usuario': usuario,
                'password': password,
                'uri': uri,
                'estado': '',
                'nombre': "Mario Ernesto"
                }     
        with open('user_data_signup.txt', 'w') as outfile:
            json.dump(user_data_signup, outfile)
        os.system("Python capa_interfaz.py signup")
                
            
def checkMousePosition():
    global estado
    global sign_up
    global log_in
    global op1
    global op2
    global op3
    global op4
    global op5
    global op6
    
    if estado == 0:
        #Cambia color del cartel de cambio de estado
        if mouseX>= 470 and mouseX<= 835 and mouseY>= 545 and mouseY <= 579:
            sign_up = True
            printText()
        elif estado == 0:
            sign_up = False
            printText()
            
        #Cambia color boton log_in o registrarse
        if mouseX >= 600 and mouseX <=750 and mouseY >=600 and mouseY <= 640:
            log_in = True
            printText()
        elif estado == 0:
            log_in = False
            printText()
            
    if estado == 1:
        #Cambia color del cartel de cambio de estado
        if mouseX>= 470 and mouseX<= 835 and mouseY>= 545 and mouseY <= 579:
            log_in = True
            printText()
        elif estado == 1:
            log_in = False
            printText()
            
        #Cambia color boton Registrame
        if mouseX >= 600 and mouseX <=750 and mouseY >=600 and mouseY <= 640:
            sign_up = True
            printText()
        elif estado == 1:
            sign_up = False
            printText()
        
    if estado == 2:
        
        #Cambia color opcion 1 (Buscar Playlists en Spotify)
        if (mouseX>= 600.5 and mouseX<= 700.5 and mouseY>= 25 and mouseY <= 125) or (mouseX>= 607 and mouseX<= 700 and mouseY>= 130 and mouseY <= 200):
            op1 = True
            printText()
        elif estado == 2:
            op1 = False
            printText()
        
        #Cambia color opcion 2 (Buscar Videos para una Playlist)
        if (mouseX>= 600.5 and mouseX<= 700.5 and mouseY>= 263 and mouseY <= 348) or (mouseX>= 590 and mouseX<= 740 and mouseY>= 368 and mouseY <= 438):
            op2 = True
            printText()
        elif estado == 2:
            op2 = False
            printText()
        

        
def draw():
    if estado == 0:
        checkMousePosition()
        app.login()
    elif estado == 1:
        checkMousePosition()
        app.signup()
    if estado == 2:
        checkMousePosition()
        app.menu_form()
    if estado == 3:
        app.showTracks()
