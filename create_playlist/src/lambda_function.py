import s3_utils 

from spotify_utils import search_spotify, get_track_id, add_tracks_to_playlist


def lambda_handler(event, context):

    playlog = s3_utils.get_playlog()
    
    programs = playlog.get("programs")
    program = programs[0] 

    all_tracks = []


    tracks = program.get("Tracks")

    for track in tracks:

        
        results = search_spotify(track.get("Title"), track.get("Album")) 
        track_id = get_track_id(results)

        if track_id:

            all_tracks.append(track_id)


    print(all_tracks)

    add_tracks_to_playlist(None, all_tracks) 
    
    print("done adding tracks")

 
#    track = program.get("Tracks")[0]
#    print(track)
#    print("searching for track")
#    results = search_spotify(track.get("Title"), track.get("Album")) 
#    track_id = get_track_id(results)


 
#    for program in programs:
#        print(program)
        
        
    


lambda_handler(None, None)


