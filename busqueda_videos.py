import argparse
import youtube3
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import googleapiclient
import requests
import sys
import os
import webbrowser



# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
# https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = 'AIzaSyC9m2HMj0d6a9tCORRBt0VRTu32GLQn8ew'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search():
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=sys.argv[1],
    part='id,snippet',
    maxResults=1
  ).execute()

  videos = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
      videos.append('%s (%s)' % (search_result['snippet']['title'],
                                 search_result['id']['videoId']))

  return (search_result['id']['videoId'])



video = youtube_search()
url = 'youtube.com/watch?v=' + video
webbrowser.open_new(url)