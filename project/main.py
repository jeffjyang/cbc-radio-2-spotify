# shows a user's playlists (need to be authenticated via oauth)
import sys
import spotipy
import spotipy.util as util
import spotipy.oauth2 as oauth
from config import USERNAME, CLIENT_ID, CLIENT_SECRET, SCOPE, REDIRECT_URI
#TODO setup config


token = util.prompt_for_user_token(USERNAME,SCOPE,
        client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI)

print("token " + token)

#if token:
if token:
    print("have token")
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print (track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print ("Can't get token for", USERNAME)

def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print ("   %d %32.32s %s" % (i, track['artists'][0]['name'],
            track['name']))
