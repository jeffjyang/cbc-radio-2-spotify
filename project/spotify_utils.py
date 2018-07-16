# shows a user's playlists (need to be authenticated via oauth)
import sys
import spotipy
import spotipy.util as util
import spotipy.oauth2 as oauth
import json
from config import USERNAME, CLIENT_ID, CLIENT_SECRET, SCOPE, REDIRECT_URI



def search_spotify(track, album):

    query = "track:{} album:{}".format(track, album)

    print(query)

    token = util.prompt_for_user_token(USERNAME,SCOPE,
            client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI)

    spotify = spotipy.Spotify(auth=token)
    results = spotify.search(q=query, type='track', limit=10)

    print(type(results))

    return results



#track="dear life"
#album="colors"
#search_spotify(track, album)

def get_track_id(results):
