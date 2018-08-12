import spotipy.util as util
from config import USERNAME, SCOPE, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

def get_token():

    token = util.prompt_for_user_token(USERNAME,SCOPE,
        client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI)

    if token:
        print("Successfully obtained Spotify access token")
    else:
        print("Error getting Spotify access token")


get_token()
