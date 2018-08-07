import spotify_utils
import playlog_utils
import playlist_utils
import s3_utils

def lambda_handler(event, context):
    playlog = playlog_utils.get_playlog()

    s3_utils.upload_s3(playlog)

    playlist_utils.reset_playlists()
    playlist_utils.create_playlists(playlog)
