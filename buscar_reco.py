import sys
import spotipy
import json
import os

''' shows recommendations for the given artist
'''

from spotipy.oauth2 import SpotifyClientCredentials
client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False

def get_artist(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None

def show_recommendations_for_artist(artist):
    artists = []
    results = sp.recommendations(seed_artists = [artist['id']])
    for track in results['tracks']:
        if track['artists'][0]['name'] not in artists and track['artists'][0]['name'] is not artist:
            artists.append(track['artists'][0]['name'])
    return artists

with open('artista_recomendaciones.txt') as json_file:
    artista_recomendaciones = json.load(json_file)
artista = artista_recomendaciones
name = artista
artist = get_artist(name)
artistas = show_recommendations_for_artist(artist)
with open('reco.txt', 'w') as outfile:
    json.dump(artistas, outfile)
