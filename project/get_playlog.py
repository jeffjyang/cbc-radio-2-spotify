import requests
import json
import datetime

def get_playlog():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day

    url = "https://www.cbcmusic.ca/Component/Playlog/GetPlaylog?stationId=110&date={}-{}-{}"\
            .format(year, month, day)

    print(url)

    res = requests.get(url)
    playlog = res.json()

    return playlog
