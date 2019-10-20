from __future__ import print_function    # (at top of module)
import os
import sys
import json
import time
import spotipy
import webbrowser
import URL_Auth as util
from json.decoder import JSONDecodeError
from spotipy.oauth2 import SpotifyClientCredentials
import tkinter as tk


#Get the username from terminal
username = 'nazarenaa.a'
scope = 'user-read-private user-read-playback-state user-modify-playback-state'

# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username) # add scope
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username) # add scope'''


# Create our spotify object with permissions
sp= spotipy.Spotify(auth=token)
tracks_name = []
tracks_artist = []

# Main Program
def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        tracks_name.append(track['name'])
        tracks_artist.append(track['artists'][0]['name'])
        print("   %d %32.32s %s" % (i, track['artists'][0]['name'],track['name']))


playlists = sp.user_playlists(username)
for playlist in playlists['items']:
        if playlist['owner']['id'] == username:
            print()
            print(playlist['name'])
            print('  total tracks', playlist['tracks']['total'])
            results = sp.user_playlist(username, playlist['id'],
            fields="tracks,next")
            tracks = results['tracks']
            show_tracks(tracks)
            while tracks['next']:
                tracks = sp.next(tracks)
                show_tracks(tracks)


data = {}
data['tracks'] = []
for i in range(0,len(tracks_name)):
    data['tracks'].append({
        'name': tracks_name[i],
        'artist': tracks_artist[i],
        'index': i + 1
    })

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
