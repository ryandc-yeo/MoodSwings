###
# TEST: fetch artist albums
###

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import config

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id=config.SPOTIFY_CLIENT_ID, 
    client_secret=config.SPOTIFY_CLIENT_SECRET
    ))

am_uri = 'spotify:artist:7Ln80lUS6He07XvHI8qqHH'

results = spotify.artist_albums(am_uri, album_type='album')
albums = results['items']

while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])