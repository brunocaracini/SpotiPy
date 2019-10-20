import os
import oauth2
import spotipy
from spotipy import oauth2
import webbrowser
from tkinter import *
import tkinter as tk


url = ''

def obtain_response():
    url_form = tk.Tk()
    url_form.geometry("300x100") #Configurar tamaño
    url_form.title ("URL Verification")


    def realiza():
        global url
        url = url_e.get()
        str(url)
        url_form.destroy()

    #Labels y Botones
    lblurl = tk.Label(url_form, text="Ingrese el URL al que fue dirigido")
    lblurl.place(x=50, y=10)
    url_e = tk.Entry(url_form)
    url_e.place(x=80, y=40)

    btnGuarda = tk.Button(url_form, text="Guardar", command = realiza)
    btnGuarda.place(x=117, y=70)

    url_form.mainloop()
    return url

def prompt_for_user_token(username, scope=None, client_id = None,
        client_secret = None, redirect_uri = None):
    ''' prompts the user to login if necessary and returns       
        the user token suitable for use with the spotipy.Spotify
        constructor

        Parameters:

         - username - the Spotify username
         - scope - the desired scope of the request
         - client_id - the client id of your app
         - client_secret - the client secret of your app
         - redirect_uri - the redirect URI of your app

    '''

    if not client_id:
        client_id = os.getenv('SPOTIPY_CLIENT_ID')

    if not client_secret:
        client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

    if not redirect_uri:
        redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')

    if not client_id:
        print('''
            You need to set your Spotify API credentials. You can do this by
            setting environment variables like so:

            export SPOTIPY_CLIENT_ID='your-spotify-client-id'
            export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
            export SPOTIPY_REDIRECT_URI='your-app-redirect-url'

            Get your credentials at
                https://developer.spotify.com/my-applications
        ''')
        raise spotipy.SpotifyException(550, -1, 'no credentials set')

    sp_oauth = oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri,
        scope=scope, cache_path=".cache-" + username )

    # try to get a valid token for this user, from the cache,
    # if not in the cache, the create a new (this will send
    # the user to a web page where they can authorize this app)

    token_info = sp_oauth.get_cached_token()

    if not token_info:
        print('''

            User authentication requires interaction with your
            web browser. Once you enter your credentials and
            give authorization, you will be redirected to
            a url.  Paste that url you were directed to to
            complete the authorization.

        ''')
        auth_url = sp_oauth.get_authorize_url()
        try:
            webbrowser.open(auth_url)
            print("Opened %s in your browser" % auth_url)
        except:
            print("Please navigate here: %s" % auth_url)

        print()
        print()
        try:
            obtain_response()
            response = url
        except NameError:
            obtain_response()
            response = url

        print()
        print()

        code = sp_oauth.parse_response_code(response)
        token_info = sp_oauth.get_access_token(code)
    # Auth'ed API request
    if token_info:
        return token_info['access_token']
    else:
        try:
            webbrowser.open(auth_url)
            print("Opened %s in your browser" % auth_url)
        except:
            print("Please navigate here: %s" % auth_url)

        print()
        print()
        try:
            obtain_response()
            response = url
        except NameError:
            obtain_response()
            response = url

        print()
        print()

        code = sp_oauth.parse_response_code(response)
        token_info = sp_oauth.get_access_token(code)
    # Auth'ed API request
    if token_info:
        return token_info['access_token']
    else:
        return None