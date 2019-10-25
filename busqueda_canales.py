import argparse
import youtube3
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import googleapiclient
import requests
import sys
import webbrowser
import json


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
# https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = 'AIzaSyC9m2HMj0d6a9tCORRBt0VRTu32GLQn8ew'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

with open('channel.txt') as json_file:
  channel = json.load(json_file)
titulo = channel

def youtube_search():
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q= titulo,
    part='id,snippet',
    maxResults=10
  ).execute()


  channels = []


  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#channel':
      channels.append('%s' % (search_result['id']['channelId']))

  

  return channels
  

channels = youtube_search()
i = 0
a = False
while i < len(channels) and a == False:
  if channels[i] is not None:
    channel = channels[i]
    a = True
  else:
    i+=1
url = 'youtube.com/channel/' + channel
webbrowser.open(url)