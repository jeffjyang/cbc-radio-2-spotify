import sys
import spotipy
import spotipy.util as util
import spotipy.oauth2 as oauth
from config import USERNAME, CLIENT_ID, CLIENT_SECRET, SCOPE, REDIRECT_URI


token = util.prompt_for_user_token(USERNAME,SCOPE,
    client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI)

spotify = spotipy.Spotify(auth=token)


def search_spotify(track, album):

    query = "track:{} album:{}".format(track, album)

    results = spotify.search(q=query, type='track', limit=10)

    items = results.get("tracks").get("items")

    if not items:
        print("No results for query: " + query)
        return ""

    track_id = items[0].get("id")

    return track_id


def update_name(playlist_id, playlist_name):

    spotify.user_playlist_change_details(USERNAME, playlist_id, name=playlist_name)


def add_tracks_to_playlist(playlist_id, tracks):

    spotify.user_playlist_replace_tracks(USERNAME, playlist_id, tracks)


def remove_all_tracks(playlist_id):

    tracks = []
    spotify.user_playlist_replace_tracks(USERNAME, playlist_id, tracks)
