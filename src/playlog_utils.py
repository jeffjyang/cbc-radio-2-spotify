import requests
import datetime
import json
from config import UTC_OFFSET

def get_playlog():

    now = datetime.datetime.utcnow() + datetime.timedelta(hours=UTC_OFFSET, weeks=-1)

    year = now.year
    month = now.month
    day = now.day

    url = "https://www.cbcmusic.ca/Component/Playlog/GetPlaylog?stationId=110&date={}-{}-{}"\
            .format(year, month, day)

    res = requests.get(url)
    playlog = res.json()

    playlog["timestamp"] = now.isoformat()

    return playlog
