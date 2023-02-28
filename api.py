import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

client_id= '539ea02afb9a4c21bc490dfba95bf88b'

client_secret = '5315462e90d748c195f94da09424f876'

redirect_uri="http://localhost:8888/callback"

audio_features = [
  'danceability',
  'energy',
  'loudness',
  'speechiness',
  'acousticness',
  'instrumentalness',
  'liveness',
  'valence',
  'tempo',
  'duration_ms',
  'explicit'
  ]

feature = ['artist']

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_audio_features(query):
    results = sp.search(q = query, type = 'track')
    track_uri = results['tracks']['items'][0]['uri']
   
    #track_artist = results['tracks']['items'][0]['artists'][0]['name']
    track_features = sp.audio_features(track_uri)
    #track_popularity = results['tracks']['items'][0]['popularity']
    df = pd.DataFrame(track_features, columns = audio_features)
    track_explicit = results['tracks']['items'][0]['explicit']
    #df['artist'] = track_artist
    #df['popularity'] = track_popularity
    df['explicit'] = track_explicit
    return df

def get_audio_artist(query):
    results = sp.search(q = query, type = 'track')
    track_uri = results['tracks']['items'][0]['uri']
    track_features = sp.audio_features(track_uri)
    df_artist = pd.DataFrame(track_features,columns=feature)
    results = sp.search(q = query, type = 'track')
    track_artist = results['tracks']['items'][0]['artists'][0]['name']
    df_artist['artist'] = track_artist
    return df_artist