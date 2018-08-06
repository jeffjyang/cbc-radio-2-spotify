import sys
import spotipy
import spotipy.util as util
import spotipy.oauth2 as oauth
import json
from config import USERNAME, CLIENT_ID, CLIENT_SECRET, SCOPE, REDIRECT_URI


token = util.prompt_for_user_token(USERNAME,SCOPE,
    client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI)


spotify = spotipy.Spotify(auth=token)

def search_spotify(track, album):

    query = "track:{} album:{}".format(track, album)

    print(query)

    results = spotify.search(q=query, type='track', limit=10)

    return results



def get_track_id(results):
    items = results.get("tracks").get("items")
    
    if not items:
        print("empty list")
        return ""
    
    track_id = items[0].get("id")
    return track_id




def create_playlist(name):

    spotify.user_playlist_create(USERNAME, name)


def add_tracks_to_playlist(playlist, tracks):

    playlist_id = "7a6OIkGpNhOUx4HHMmsBFH"  


    spotify.user_playlist_replace_tracks(USERNAME, playlist_id, tracks)



#create_playlist("test_playlist")



