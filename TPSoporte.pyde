import json
import os
import sys
import math
import re

refresh = False
config = False
salir = False
busca_recomend = False
artista_recomendaciones = ''
recomend = False
op = 0
scroll = 0
estado = 0
usuario = ''
password = ''
password2 = ''
uri = ''
nombre = ''
name = False
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
error_window_stroke = False
plsel = ''
ingresapl = False
ingresapl2 = False
len_data = 0
playlist = []
youtube = True
canciones = []



class Presentacion():
    
    def login(self):
        if usuario == '' and password == '':
            self.login_form()
        
    def login_form(self):
         
        image(back, 0, 0)
        
        #Cartel Iniciar Sesion o Registrese
        textSize(50)
        fill(250, 230)
        text('Inicie Sesion', 522 , 290)
        
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
        if usuario == '' and password == '' and password2 == '' and uri == '' and nombre == '':
            self.signup_form()
    
    def signup_form(self):
        image(back, 0, 0)
        
        #Cartel Registrese
        textSize(50)
        fill(250, 230)
        text('Registrese', 545 , 80)
        
        #Recuadro ingreso usuario
        noStroke()
        photo = loadImage("user_icon.png")
        image(photo, 460, 147)
        fill(240, 50)
        if name:
            stroke(117,231,193)
        rect(445, 130, 450, 70)
        
        #Recuadro ingreso mail
        noStroke()
        photo = loadImage("mail_icon.png")
        tint(230, 120)
        image(photo, 460, 244)
        noTint()
        fill(240, 50)
        if user:
            stroke(117,231,193)
        rect(445, 220, 450, 70)
       
        
        #Recuadro ingreso uri Spotify
        noStroke()
        fill(240, 50)
        photo = loadImage("spotify_icon.png")
        image(photo, 464, 329)
        if sp_user:
            stroke(117,231,193)
        rect(445, 310, 450, 70)
        
        #Recuadro ingreso contraseña
        noStroke()
        photo = loadImage("password_icon.png")
        image(photo, 460, 417)
        fill(240, 50)
        if passw:
           stroke(117,231,193)
        rect(445, 400, 450, 70)
        
        #Recuadro ingreso contraseña 2
        noStroke()
        photo = loadImage("password_icon.png")
        image(photo, 460, 507)
        fill(240, 50)
        if passw2:
           stroke(117,231,193)
        rect(445, 490, 450, 70)
        
        #boton Registrarse
        noStroke()
        if sign_up:
            fill (117,231,193, 250)
        else:
            fill (117,231,193, 150)
        rect(600,610,150,50,20)
        textSize(18)
        fill(255, 200)
        text('Sign up', 643,640)
        
        #Log In
        if log_in:
            fill(117,231,193)
        else: 
            fill(255,180)
        textSize(17)
        text('Ya posee una cuenta? Inicie sesion aqui',500,587)
        
        #Error window
        if error_window:
          self.error_window_form()  
    
        
    def menu_form(self):
        image(back, 0, 0)
        
        #Barra Lateral del menu
        fill(20)
        rect(0,0,350,height)
        
        #Texto menu lateral
        fill(240,210)
        textSize(20)
        
        #Icono usuario barra lateral
        textAlign(CENTER)
        text(nombre + " | " + uri, 175, 180)
        textAlign(LEFT)
        tint(255,240)
        photo = loadImage("usermenu_icon.png")
        image(photo, 105, 20)
        
        
        #Informacion usuario:
        textSize(40)
        fill(117,231,193, 220)
        if canciones <10:
            text(canciones, 55,420)
        elif canciones <100:
            text(canciones, 42,420)
        else:
            text(canciones, 30,420)
            
            
        if artistas <10:
            text(len(artistas), 161,420)
        elif len(artistas) <100:
            text(len(artistas), 149,420)
        else:
            text(len(artistas), 137,420)
        
        
        if cant_playlist <10:
            text(cant_playlist, 258,420)
        elif cant_playlist <100:
            text(cant_playlist, 247,420)
        else:
            text(cant_playlist, 236,420)
        
        fill(255,210)
        textSize(25)
        textSize(15)
        text("Canciones", 30,450)
        text("Artistas", 145,450)
        text("Playlist", 245,450)
        stroke(240,100)
        line(20,215,330,215)
        line(20,490,330,490)
        noStroke()
        
        #Imagen estadisticas
        photo = loadImage("stats_icon.png")
        image(photo, 105, 240)
        
        #Opcion de salir en barra lateral
        if salir:
            tint(117,231,193, 170)
            fill(117,231,193, 170)
        else:
            tint(240,210)
            fill(240,210)
        photo = loadImage("exit_icon.png")
        image(photo, 20, 630)
        textSize(20)
        text("Cerrar sesion", 85, 665)
        
        
        #Opcion de configuracion en barra lateral
        if config:
            tint(117,231,193, 170)
            fill(117,231,193, 170)
        else:
            tint(240,210)
            fill(240,210)
        photo = loadImage("settings_icon.png")
        image(photo, 25, 580)
        textSize(20)
        text("Modificar datos", 85, 605)
        
        #Opcion de actualizar en barra lateral
        if refresh:
            tint(117,231,193, 170)
            fill(117,231,193, 170)
        else:
            tint(240,210)
            fill(240,210)
        photo = loadImage("refresh_icon.png")
        image(photo, 25, 520)
        textSize(20)
        text("Actualizar", 85, 547)
        
        
        #Opcion 1: Mostrar tracks de una playlist en Spotify
        if op1:
            tint(117,231,193, 170)
            fill(117,231,193, 170)
        else:
            tint(250,210)
            fill(240,210)
        photo = loadImage("playlist_icon.png")
        image(photo, 602, 25)
        textSize(22)
        text("Spotify", 618, 150)
        text("Playlists", 611, 180)
        
        #Opcion 2: Buscar Videos de una PlayList
        if op2:
            tint(117,231,193, 170)
            fill(117,231,193, 170)
        else:
            tint(250,210)
            fill(255,210)
        photo = loadImage("videoSearch_icon.png")
        image(photo, 613, 263)
        textSize(22)
        text("Buscar videos", 587, 388)
        text("desde playlist", 585, 418)
        
        #Opcion 3: Buscar video Lyrics desde una Playlist
        if op3:
            tint(117,231,193, 170)
            fill(117,231,193, 170)
        else:
            tint(250,210)
            fill(255,210)
        photo = loadImage("videoSearch_icon.png")
        image(photo, 613, 490)
        textSize(22)
        text("Video lyric", 600, 615)
        text("desde playlist", 584, 645)
        
        #Opcion 4: Buscar Canales de Artistas de mis Playlist
        if op4:
            tint(117,231,193, 170)
            fill(117,231,193, 170)
        else:
            tint(250,210)
            fill(255,210)
        photo = loadImage("channel_icon.png")
        image(photo, 1011, 263)
        textSize(22)
        text("Buscar Canales", 976, 388)
        text("de artistas", 1001, 418)
        
        #Opcion 5: Buscar Canales de Artistas de mis Playlist
        if op5:
            tint(117,231,193, 170)
            fill(117,231,193, 170)
        else:
            tint(250,210)
            fill(255,210)
        photo = loadImage("favourite_icon.png")
        image(photo, 1011, 33)
        textSize(22)
        text("Artistas", 1011, 150)
        text("Favoritos", 1006, 180)
        
        #Opcion 6: Recomendar artistas
        photo = loadImage("music_icon.png")
        if op6:
            tint(117,231,193, 170)
            fill(117,231,193, 170)
        else:
            tint(250,210)
            fill(255,210)
        image(photo, 1013, 487)
        textSize(22)
        text("Artistas", 1013, 615)
        text("Recomendados", 980, 645)
    
        #Default Settings:
        tint(255,180)
        fill(255,180)
        
    
    def showPlaylist(self):
        
        image(back, 0, 0)
        with open('user_playlists.txt') as json_file:
            user_playlists = json.load(json_file)
        
        #Botón de atrás
        image(back_button, 75 , height/2)
        tint(255, 230)
        
        #Rectangulo negro de fondo
        noStroke()
        fill(40)
        rect(200,250 + scroll, width - 400, len(user_playlists)*50 + 75, 20)
        
        #Imprimir playlists
        vposition = 270
        hposition = 350
        len_playlists = len(user_playlists)
        for i in range(0, len_playlists):
            vposition +=50
            stroke(70, 240)
            line(220, vposition + 17 + scroll, width - 240, vposition + 15 + scroll)
            fill (220, 230)
            textSize(18)
            text(str(i + 1) + ".", hposition - 40, vposition + scroll)
            text(user_playlists[i][0:50], hposition, vposition + scroll)
        
        #Recuadro ingresa numero playlist
        noStroke()
        fill(40)
        if ingresapl:
           stroke(117,231,193)
        rect(200, 200 + scroll, 295, 40, 20)
        
        #Recuadro buscar
        if ingresapl2:
            fill(117,231,193,250)
        else:
            fill(117,231,193,150)
        noStroke()   
        rect(510, 200 + scroll, 80, 40, 20)

        
        fill(220, 230)
        text('Ingrese numero de Playlist:', 210, 227 + scroll)
        text('Buscar', 520, 227 + scroll)
        fill(117,231,193)
        text(plsel, 460, 227)
        
        #Error window
        if error_window:
          self.error_window_form()  

        
    
    def showTracks(self):
        image(back, 0, 0)
        with open('data.txt') as json_file:
            data = json.load(json_file)
        
        #Botón de atrás
        image(back_button, 75 , height/2)
        tint(255, 230)
        
        #Rectángulo Título de Playlist:
        noStroke()
        fill(40)
        rect(200,120 + scroll, width - 400, 100, 20)
        textSize(50)
        fill (220, 230)
        text("Playlist: " + playlist_name, 310, 185 + scroll)
        
        
        #Rectangulo negro de fondo
        noStroke()
        fill(40)
        rect(200,250 + scroll, width - 400, len(playlist)*50 + 75, 20)
        
        #Imprimir playlists
        vposition = 300
        hposition = 350
        i = 0
        fill(255)
        for track in playlist:
            vposition +=50
            stroke(70, 240)
            line(220, vposition + 17 + scroll, width - 240, vposition + 15 + scroll)
            fill (220, 230)                
            textSize(18)
            text(str(i + 1) + ".", hposition - 40, vposition + scroll)
            text(track['name'][0:40], hposition, vposition + scroll)
            text(track['artist'][0:50], hposition + 400, vposition + scroll)
            if op == 2 or op == 3:
                image(youtube_icon, hposition + 680, vposition - 21 + scroll)                
            i+=1
    
    
    def showArtists(self):
        image(back, 0, 0)
        with open('data.txt') as json_file:
            data = json.load(json_file)
        
        #Botón de atrás
        image(back_button, 75 , height/2)
        tint(255, 230)
        
        #Rectángulo Título de Playlist:
        noStroke()
        fill(40)
        rect(200,120 + scroll, width - 400, 100, 20)
        textSize(50)
        fill (220, 230)
        text("Artistas: " , 310, 185 + scroll)
        
        
        #Rectangulo negro de fondo
        noStroke()
        fill(40)
        rect(200,250 + scroll, width - 400, len(artistas)*50 + 75, 20)
        
        #Imprimir Artistas
        vposition = 300
        hposition = 350
        i = 0
        fill(255)
        for artist in artistas:
            vposition +=50
            stroke(70, 240)
            line(220, vposition + 17 + scroll, width - 240, vposition + 15 + scroll)
            fill (220, 230)                
            textSize(18)
            text(str(i + 1) + ".", hposition - 40, vposition + scroll)
            text(artist[0:40], hposition, vposition + scroll)
            if op == 2 or op == 3 or op == 4:
                image(youtube_icon, hposition + 680, vposition - 21 + scroll)                
            i+=1
        
        
    def showRecomendaciones(self):
        image(back, 0, 0)
        
        #Botón de atrás
        image(back_button, 75 , height/2)
        tint(255, 230)
        
        #Rectángulo Título de Playlist:
        noStroke()
        fill(40)
        rect(200,120 + scroll, width - 400, 100, 20)
        textSize(50)
        fill (220, 230)
        text("Artistas recomendados: " , 310, 185 + scroll)
        
        
        #Rectangulo negro de fondo
        noStroke()
        fill(40)
        rect(200,250 + scroll, width - 400, len(recomendaciones)*50 + 75, 20)
        
        #Imprimir playlists
        vposition = 300
        hposition = 350
        i = 0
        fill(255)
        for artist in recomendaciones:
            vposition +=50
            stroke(70, 240)
            line(220, vposition + 17 + scroll, width - 240, vposition + 15 + scroll)
            fill (220, 230)                
            textSize(18)
            text(str(i + 1) + ".", hposition - 40, vposition + scroll)
            text(artist[0:40], hposition, vposition + scroll)
            if op== 6:
                image(youtube_icon, hposition + 680, vposition - 21 + scroll)                
            i+=1
    
    def busqueda_artista_form(self):
        image(back, 0, 0)
        
        #cartel 
        textSize(50)
        fill(250, 230)
        text('Ingrese artista', 490 , 245)
        
        
        #Rectangulo ingreso artista
        textSize(18)
        noStroke()
        fill(40)
        if recomend:
            stroke(117,231,193)
        rect(445, 290, 450, 70)
        fill(245,230)
        text(artista_recomendaciones, 530 , 332)
        
        #Boton atras
        image(back_button, 75 , height/2)
        tint(255, 230)
        
        #Boton buscar
        noStroke()
        if len(artista_recomendaciones) == 0:
            fill(90)
        elif busca_recomend:
            fill (117,231,193, 250)
        else:
            fill (117,231,193, 150)
        rect(590,390,150,50,20)
        textSize(18)
        fill(255, 200)
        text('Buscar', 640,420)

    
    def error_window_form(self):
        global error
        
        #Fondo negro
        fill(10,230)
        rect(0,0,width,height)
        
        #Ventana de error
        fill(20,230)
        stroke(117,231,193)
        rect(400, 300, 535, 190)
        
        #Boton Aceptar
        fill(117,231,193,20)
        if error_window_stroke:
            fill(117,231,193)
        rect(570,447,200,30, 20)
        fill(255, 200)
        text('Aceptar', 640,468)
        
        #signo advertencia
        photo = loadImage("warning_icon.png")
        image(photo, 619, 317)
        tint(255,200)

        
        #Mensaje del error
        fill(240, 240)
        textAlign(CENTER)
        text("Error: "+ error, 670, 430)
        textAlign(LEFT)
        




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
    global nombre

    sign_up = False
    log_in = False
    user = False
    passw = False
    passw2 = False
    sp_user = False
    name = False
    usuario = ''
    password = ''
    password2 = ''
    uri = ''
    nombre = ''


def verifica_input(key_):
    verifica_input = False
    if estado == 3:
        if ((int(ord(key_))) >= 48 and (int(ord(key_))) <= 57):
            verifica_input = True
        else:
            verifica_input = False
    else:
        if key_ == 65535:
            str(key_)[:1]
        elif ((int(ord(key_)) >= 64 and int(ord(key_)) <= 90) or (int(ord(key_)) >= 97 and int(ord(key_)) <= 122) or int(ord(key_)) == 95 or int(ord(key_)) == 45 or int(ord(key_)) == 43 or int(ord(key_)) == 46):
            verifica_input = True
        elif (int(ord(key_)) >= 48 and int(ord(key_)) <= 57): 
            verifica_input = True
        elif estado == 8 and (int(ord(key_))) == 32:
            verifica_input = True
    return verifica_input
    

def printText():
    global usuario
    global password
    global uri
    global password2
    global error_window
    global error
    global ingresapl
    global ingresapl2
    global plsel
    global nombre
    
    if estado == 0:
        app.login_form()
        fill(240)
        if error_window == False:
            text(usuario, 530 , 422)
            text(password, 530 , 512)
    
    
    elif estado == 1:
        app.signup_form()
        fill(240)
        if error_window == False:
            text(nombre, 530, 172)
            text(usuario, 530 , 262)
            text(uri, 530 , 352)
            text(password, 530 , 442)
            text(password2, 530 , 532)
            
    elif estado == 3:
        app.showPlaylist()

    
    
    
def setup():
    global back
    global youtube_icon
    global back_button
    size (1365, 700)
    
    youtube_icon = loadImage("youtube_icon.png")
    back_button = loadImage("back_icon.png")
    back = loadImage("fondo2.jpg")
    image(back, 0, 0)

    strokeWeight(2)

    
def mouseWheel(event):
    global scroll
    if estado == 5 or estado == 4 or estado == 6 or estado == 7 or estado == 9:
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
    global ingresapl
    global plsel
    global recomend
    global artista_recomendaciones
    global nombre
    global name
    
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
        
        if name and verifica_input(key):
            nombre += str(key)
        elif name and (key == BACKSPACE) and len(nombre)>0:
            nombre = nombre[:-1]  
        
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
            
    if estado ==3:
        if ingresapl and verifica_input(key) and len(plsel) < 2:
            plsel += str(key)
        elif ingresapl and (key == BACKSPACE) and len(password)>0:
            plsel = plsel[:-1] 
    
    if estado == 8:
        if recomend and verifica_input(key) and len(plsel) < 2:
            artista_recomendaciones += str(key)
        elif recomend and (key == BACKSPACE) and len(artista_recomendaciones)>0:
            artista_recomendaciones = artista_recomendaciones[:-1] 
        
            
        
        
    printText()    
        

def mousePressed():
    global user
    global passw
    global passw2
    global estado
    global log_in
    global sign_up
    global sp_user
    global error_window
    global uri
    global ingresapl
    global op
    global scroll
    global youtube
    global recomend
    global name
    global error
    
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
            '''estado = 2
            obtener_artistas()
            obtener_playlist()
            obtener_canciones()
            '''
            printText()
            exporta_json()
            if importa_json():
                estado = 2
                exporta_json()
                importa_json()
                os.system("Python Obtener_canciones.py {0}".format(uri))
                obtener_artistas()
                obtener_playlist()
                obtener_canciones()
             
        
        #Cambia estado a Registrarse
        elif mouseX>= 470 and mouseX<= 835 and mouseY>= 545 and mouseY <= 579:
            estado = 1
            sign_up = False
            reset()
    
    elif estado == 1:
        
        #Resalta borde ingreso nombre de usuario
        if mouseX >= 445 and mouseX <=895 and mouseY >=130 and mouseY <= 240:
            passw = False
            passw2 = False
            sp_user = False
            user = False
            name = True
            printText()
        
        #Resalta borde ingreso usuario
        if mouseX >= 445 and mouseX <=895 and mouseY >=220 and mouseY <= 310:
            passw = False
            passw2 = False
            sp_user = False
            name = False
            user = True
            printText()

        #Resalta borde ingreso uri Spotify
        if mouseX >= 445 and mouseX <=895 and mouseY >=310 and mouseY <= 380:
            sp_user = True
            passw = False
            passw2 = False
            name = False
            user = False
            printText()
        
        #Resalta borde ingreso contraseña 1
        if mouseX >= 445 and mouseX <=895 and mouseY >=400 and mouseY <= 470:
            passw = True
            passw2 = False
            user = False
            sp_user = False
            name = False
            printText()
        
        #Resalta borde ingreso Contraseña 2
        elif mouseX >= 445 and mouseX <=895 and mouseY >=490 and mouseY <= 560:
            user = False
            passw = False
            nombre = False
            sp_user = False
            nombre = False
            passw2 = True
            printText()
            
        #Ejecuta Registro y cambia estado a Log In (estado = 0)
        elif mouseX >= 600 and mouseX <=750 and mouseY >=610 and mouseY <= 660:
            exporta_json()
            if importa_json():
                estado = 0

        
        #Cambia estado a Registrarse
        elif mouseX>= 470 and mouseX<= 835 and mouseY>= 565 and mouseY <= 599:
            estado = 0
            reset()
        
    elif estado == 2:
        #Seleccion de opcion 1 (Buscar Playlists en Spotify)
        if (mouseX>= 600.5 and mouseX<= 700.5 and mouseY>= 25 and mouseY <= 125) or (mouseX>= 607 and mouseX<= 700 and mouseY>= 130 and mouseY <= 200):
            #os.system("Python Obtener_canciones.py {0}".format(uri))
            op = 1
            estado = 3
        
        #Seleccion de opcion 2 (Buscar videos para una Playlist)
        if (mouseX>= 600.5 and mouseX<= 700.5 and mouseY>= 263 and mouseY <= 348) or (mouseX>= 590 and mouseX<= 740 and mouseY>= 368 and mouseY <= 438):
            #os.system("Python Obtener_canciones.py {0}".format(uri))
            op = 2
            estado = 3
        
        #Seleccion opcion opcion 3 (Buscar video Lyrics para una Playlist)
        if (mouseX>= 600.5 and mouseX<= 700.5 and mouseY>= 470 and mouseY <= 563) or (mouseX>= 590 and mouseX<= 740 and mouseY>= 572 and mouseY <= 655):
           #os.system("Python Obtener_canciones.py {0}".format(uri))
           op = 3
           estado = 3
    
        #Selección opción 4 (Buscar canales para los artistas de mis playlist)
        if (mouseX>= 1000 and mouseX<= 1103 and mouseY>= 263 and mouseY <= 348) or (mouseX>= 970 and mouseX<= 1140 and mouseY>= 368 and mouseY <= 438):
            obtener_artistas()
            op = 4
            estado = 7
        
        #Recomendación de artistas
        if (mouseX>= 1000 and mouseX<= 1103 and mouseY>= 470 and mouseY <= 563) or (mouseX>= 993 and mouseX<= 1120 and mouseY>= 572 and mouseY <= 620):
            op = 6
            cursor(ARROW)
            estado = 8
        
        #Cerrar sesion
        if (mouseX>= 20 and mouseX<= 220 and mouseY>= 640 and mouseY <= 685):
            salir = False
            cursor(ARROW)
            reset()
            estado = 0
        
        #Actualizar
        if (mouseX>= 20 and mouseX<= 200 and mouseY>= 520 and mouseY <= 565):
            os.system("Python Obtener_canciones.py {0}".format(uri))
            obtener_canciones()
            obtener_artistas()
            obtener_playlist()
            
             
            
    
    elif estado == 3:
        
        #Selección botón atrás
        if mouseX>= 75 and mouseX<= 145 and mouseY>= 372.5 and mouseY <= 452.5:
            estado = 2

        #seleccion ingreso numero playlist
        if (mouseX>= 200 and mouseX<= 550 and mouseY>= 200 and mouseY <= 250):
            ingresapl = True
        
        #Seleccion busqueda (cambia estado en base a estado anterior)
        if (mouseX>= 510 and mouseX<= 600 and mouseY>= 200 and mouseY <= 250):    
            if busca_index():
                obtener_playlist()
                if op == 1:
                    estado = 6
                elif op == 2:
                    estado = 4
                elif op == 3:
                    estado = 5

    
    
    elif estado == 4:
        
        #Ejecuta busqueda video
        if mouseX>=1025 and mouseX<=1075:
            with open('data.txt') as json_file:
                data = json.load(json_file)   
            numero = math.ceil((mouseY - scroll + 340)/50) - 13        
            arg = playlist[int(numero)]['name'] + " " +  playlist[int(numero)]['artist']
            arg = re.sub('[^a-zA-Z.\d\s]', '', arg)  
            with open('song.txt', 'w') as outfile:
                json.dump(arg, outfile)
            os.system("Python busqueda_videos.py")
        
        #Cambia estado a 3 (vuelve hacia atrás)
        if mouseX>= 75 and mouseX<= 145 and mouseY>= height/2 and mouseY <= height/2 + 70:
            estado = 3
            scroll = 0
        

    elif estado == 5:
        
        #Ejecuta busqueda video
        if mouseX>=1025 and mouseX<=1075:
            with open('data.txt') as json_file:
                data = json.load(json_file)  
            numero = math.ceil((mouseY - scroll + 340)/50) - 13        
            arg = "Lyrics video " + playlist[int(numero)]['name'] + " " + playlist[int(numero)]['artist']
            arg = re.sub('[^a-zA-Z.\d\s]', '', arg)
            arg = re.sub('Remastered', '', arg)  
            with open('song.txt', 'w') as outfile:
                json.dump(arg, outfile)
            os.system("Python busqueda_videos.py")
        
        #Cambia estado a 3 (vuelve hacia atrás)
        if mouseX>= 75 and mouseX<= 145 and mouseY>= height/2 and mouseY <= height/2 + 70:
            estado = 3
            scroll = 0
            
    elif estado == 6:
        
        #Cambia estado a 3 (vuelve hacia atrás)
        if mouseX>= 75 and mouseX<= 145 and mouseY>= height/2 and mouseY <= height/2 + 70:
            estado = 3
            scroll = 0
    
    elif estado == 7:
        if mouseX>=1025 and mouseX<=1075:
            with open('data.txt') as json_file:
                data = json.load(json_file)  
            numero = math.ceil((mouseY - scroll + 340)/50) - 13        
            arg = artistas[int(numero)]
            arg = re.sub('[^a-zA-Z.\d\s]', '', arg)
            with open('channel.txt', 'w') as outfile:
                json.dump(arg, outfile)
            os.system("Python busqueda_canales.py")
        
        #Cambia estado a 2 (vuelve hacia atrás)
        if mouseX>= 75 and mouseX<= 145 and mouseY>= height/2 and mouseY <= height/2 + 70:
            estado = 2
            scroll = 0
    
    elif estado == 8:
        
        #Resalta borde ingreso artista para recomendaciones
        if mouseX >= 445 and mouseX <=895 and mouseY >=290 and mouseY <= 360:
            recomend = True
        
        #Cambia estado a 2 (vuelve hacia atrás)
        if mouseX>= 75 and mouseX<= 145 and mouseY>= height/2 and mouseY <= height/2 + 70:
            estado = 2
            scroll = 0
        
        if mouseX>= 580 and mouseX<= 750 and mouseY>= 380 and mouseY <= 450 and len(artista_recomendaciones) >0:
            obtener_recomendaciones1()
            estado = 9
            
    elif estado == 9:

        if mouseX>=1025 and mouseX<=1075:
            with open('data.txt') as json_file:
                data = json.load(json_file)  
            numero = math.ceil((mouseY - scroll + 340)/50) - 13        
            arg = recomendaciones[int(numero)]
            arg = re.sub('[^a-zA-Z.\d\s]', '', arg)
            with open('channel.txt', 'w') as outfile:
                json.dump(arg, outfile)
            os.system("Python busqueda_canales.py")
        
        #Cambia estado a 8 (vuelve hacia atrás)
        if mouseX>= 75 and mouseX<= 145 and mouseY>= height/2 and mouseY <= height/2 + 70:
            estado = 8
            scroll = 0
    
    if error_window:
        if (mouseX>= 570 and mouseX<= 770 and  mouseY>= 447 and mouseY<= 467):
            error_window = False
            error = ''
    
        
def importa_json():
    global estado
    global error
    global error_window
    global uri
    global nombre
    global cant_playlist

    if estado == 0:
        with open('user_login_result.txt') as json_file:
            user_data = json.load(json_file)
        error = user_data
        os.system("DEL user_login_result.txt")
            
    elif estado == 1:
        with open('user_signup_result.txt') as json_file:
            user_data_signup = json.load(json_file)
        error = user_data_signup
        os.system("DEL user_signup_result.txt")
    
    elif estado == 2:
        with open('user_uri.txt') as json_file:
            user_uri = json.load(json_file)
        uri = user_uri['uri']
        nombre = user_uri['nombre']
        os.system("DEL user_uri.txt")
        

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
    global nombre
    
    if estado == 0:
        user_data = [usuario, password]
        with open('user_data.txt', 'w') as outfile:
            json.dump(user_data, outfile)
        os.system("Python capa_interfaz.py login") 
   
    elif estado == 1:
        user_data_signup = {  
                'usuario': usuario,
                'password': password,
                'uri' : uri,
                'estado': '',
                'nombre': nombre
                }     
        with open('user_data_signup.txt', 'w') as outfile:
            json.dump(user_data_signup, outfile)
        os.system("Python capa_interfaz.py signup")
    
    elif estado == 2:
        user_uri = {
            'usuario': usuario,
            'uri': '',
            'nombre':''
            }
        with open('user_uri.txt', 'w') as outfile:
            json.dump(user_uri, outfile)
        os.system("Python capa_interfaz.py geturi")
                
            
def checkMousePosition():
    global estado
    global sign_up
    global log_in
    global ingresapl2
    global op1
    global op2
    global op3
    global op4
    global op5
    global op6
    global salir
    global error_window_stroke
    global busca_recomend
    global config
    global refresh
    global error_window
    
    
    if estado == 0:
        #Cambia color del cartel de cambio de estado
        if mouseX>= 470 and mouseX<= 835 and mouseY>= 545 and mouseY <= 579:
            sign_up = True
            printText()
        elif estado == 0:
            sign_up = False
            printText()
            
        #Cambia color boton log_in o registrarse
        if mouseX >= 600 and mouseX <=750 and mouseY >=600 and mouseY <= 640 and len(password)>=1 and len(usuario)>=1:
            log_in = True
            printText()
        elif estado == 0:
            log_in = False
            printText()
        
        if (sign_up or log_in) and error_window == False:
            cursor(HAND)
        elif error_window == False:
            cursor(ARROW)
        
            
            
    if estado == 1:
        #Cambia color del cartel de cambio de estado
        if mouseX>= 470 and mouseX<= 835 and mouseY>= 565 and mouseY <= 599:
            log_in = True
            printText()
        elif estado == 1:
            log_in = False
            printText()
            
        #Cambia color boton Registrame
        if mouseX >= 600 and mouseX <=750 and mouseY >=620 and mouseY <= 660:
            sign_up = True
            printText()
        elif estado == 1:
            sign_up = False
            printText()
            
        if (sign_up or log_in) and error_window == False:
            cursor(HAND)
        elif error_window == False:
            cursor(ARROW)
        
    if estado == 2:
        
        #Cambia color opcion 1 (Buscar Playlists en Spotify)
        if (mouseX>= 600.5 and mouseX<= 700.5 and mouseY>= 25 and mouseY <= 125) or (mouseX>= 607 and mouseX<= 700 and mouseY>= 130 and mouseY <= 200):
            op1 = True
        elif estado == 2:
            op1 = False
        
        #Cambia color opcion 2 (Buscar Videos para una Playlist)
        if (mouseX>= 600.5 and mouseX<= 700.5 and mouseY>= 263 and mouseY <= 348) or (mouseX>= 590 and mouseX<= 740 and mouseY>= 368 and mouseY <= 438):
            op2 = True
        elif estado == 2:
            op2 = False

        
        #Cambia color opcion 3 (Buscar video Lyrics para una Playlist)
        if (mouseX>= 600.5 and mouseX<= 700.5 and mouseY>= 470 and mouseY <= 577) or (mouseX>= 590 and mouseX<= 740 and mouseY>= 600 and mouseY <= 655):
            op3 = True
        elif estado == 2:
            op3 = False
        
        #Cambia color opción 4 (Buscar canales de los artistas de una playlist)
        if (mouseX>= 1000 and mouseX<= 1103 and mouseY>= 263 and mouseY <= 348) or (mouseX>= 970 and mouseX<= 1140 and mouseY>= 368 and mouseY <= 438):
            op4 = True
        elif estado == 2:
            op4 = False
        
        #Cambia color opcion 6 (Configuración)
        if (mouseX>= 1000 and mouseX<= 1103 and mouseY>= 470 and mouseY <= 577) or (mouseX>= 977 and mouseX<= 1160 and mouseY>= 600 and mouseY <= 660):
            op6 = True
        elif estado == 2:
            op6 = False
            
        #Cambia color opcion cerrar sesion
        if (mouseX>= 20 and mouseX<= 220 and mouseY>= 640 and mouseY <= 685):
            salir = True
        elif estado == 2:
            salir = False
        
        #Cambia color opcion modficar datos
        if (mouseX>= 20 and mouseX<= 235 and mouseY>= 580 and mouseY <= 625):
            config = True
        elif estado == 2:
            config = False
            
        #Cambia color opcion actualizar
        if (mouseX>= 20 and mouseX<= 200 and mouseY>= 520 and mouseY <= 565):
            refresh = True
        elif estado == 2:
            refresh = False
            
        #Cambia cursor de una flecha a una mano
        if op1 or op2 or op3 or op4 or op5 or op6 or salir or config or refresh:
            cursor(HAND)
        else:
            cursor(ARROW)
            

    if estado == 3:
        
        #Cambia color boton de busqueda  y cursor sobre ese botón
        if mouseX>= 510 and mouseX<= 600 and mouseY>= 200 and mouseY <= 245:
            ingresapl2 = True
            cursor(HAND)
        #Cambia cursor sobre el botón de atrás
        elif mouseX>= 75 and mouseX<= 145 and mouseY>= 372.5 and mouseY <= 452.5:
            cursor(HAND)
        #Cambia cursor sobre el recuadro de ingreso de playlist
        elif (mouseX>= 200 and mouseX<= 550 and mouseY>= 200 and mouseY <= 250):
            cursor(HAND)
        #Devuelve el cursor a una flecha
        elif estado == 3:
            ingresapl2 = False
            cursor(ARROW)
        
            
    if estado == 4 or estado == 5 or estado == 7 or estado == 9:
        
        #Cambia cursor en icono youtube y botón de atrás
        if mouseX>=1025 and mouseX<=1075:
            cursor(HAND)
        elif mouseX>= 75 and mouseX<= 145 and mouseY>= 372.5 and mouseY <= 452.5:
            cursor(HAND)
        else:
            cursor(ARROW)
            
    if estado == 6:
        if mouseX>= 75 and mouseX<= 145 and mouseY>= 372.5 and mouseY <= 452.5:
            cursor(HAND)
        else:
            cursor(ARROW)
    
    if estado == 8:
        
        #Cambia color boton buscar artistas recomendados
        if mouseX>= 580 and mouseX<= 750 and mouseY>= 380 and mouseY <= 450:
            busca_recomend = True
        elif estado == 8:
            busca_recomend = False
        
        #Cambia Mouse en boton atras y boton buscar
        if mouseX>= 75 and mouseX<= 145 and mouseY>= 372.5 and mouseY <= 452.5 or recomend:
            cursor(HAND)
        else:
            cursor(ARROW)
            
    if error_window:
        
        #Cambia color boton aceptar de la ventana de error
        if (mouseX>= 560 and mouseX<= 780 and  mouseY>= 437 and mouseY<= 487):
            error_window_stroke = True
            cursor(HAND)
        else:
            error_window_stroke = False
            cursor(ARROW)
        

def obtener_playlist():
    global playlist
    global playlist_name
    global cant_playlist
    playlist = []
    with open('user_playlists.txt') as json_file:
        user_playlists = json.load(json_file)
    with open('data.txt') as json_file:
        data = json.load(json_file)
    if estado == 2:
        cant_playlist = len(user_playlists)
    elif estado == 3:
        playlist_name = user_playlists[int(plsel) - 1]
        for track in data['tracks']:
            if track['playlist'] == playlist_name:
                playlist.append(track)

def obtener_artistas():
    global artistas
    artistas = []
    with open('data.txt') as json_file:
        data = json.load(json_file)
    for track in data['tracks']:
        if track['artist'] not in artistas:
            artistas.append(track['artist'])
    
def obtener_canciones():
    global canciones
    with open('data.txt') as json_file:
        data = json.load(json_file)
    canciones = len(data['tracks'])

def obtener_recomendaciones1():
    global recomendaciones
    global artista_recomendaciones
    with open('artista_recomendaciones.txt', 'w') as outfile:        
        json.dump(artista_recomendaciones, outfile)
    os.system("Python buscar_reco.py")
    with open('reco.txt') as json_file:
        reco = json.load(json_file)
    recomendaciones = reco
    
    

def busca_index():
    global error_window
    global error
    with open('user_playlists.txt') as json_file:
        user_playlists = json.load(json_file)
    index = len(user_playlists)
    if int(plsel) >= 1 and int(plsel) <= index:
        error_window = False
        return True
    else:
        error = 'Playlist inexistente'
        error_window = True
        return False                


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
        checkMousePosition()
        app.showPlaylist()
    if estado == 4 or estado == 5 or estado == 6:
        checkMousePosition()
        app.showTracks()
    if estado == 7:
        checkMousePosition()
        app.showArtists()
    if estado == 8:
        checkMousePosition()
        app.busqueda_artista_form()
    if estado == 9:
        checkMousePosition()
        app.showRecomendaciones()
        
    
