import s3_utils
import spotify_utils
from config import PLAYLISTS

def lambda_handler(event, context):

    reset_playlists()

    playlog = s3_utils.get_playlog()

    playlist_num = 0

    for program in playlog.get("programs"):

        if playlist_num >= len(PLAYLISTS):
            # We're out of playlists to use
            # TODO log this
            return

        playlist_id = PLAYLISTS[playlist_num]

        all_tracks = []

        title = "CBC Music: " + program.get("Title")

        for track in program.get("Tracks"):

            results = spotify_utils.search_spotify(track.get("Title"), track.get("Album"))
            track_id = spotify_utils.get_track_id(results)

            if track_id:
                all_tracks.append(track_id)


        spotify_utils.add_tracks_to_playlist(playlist_id, all_tracks)
        spotify_utils.update_name(playlist_id, title)

        playlist_num += 1


def reset_playlists():
    for playlist in PLAYLISTS:
        spotify_utils.remove_all_tracks(playlist)
        spotify_utils.update_name(playlist, "Inactive")
