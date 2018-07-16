import boto3
import requests
import json
import datetime



def lambda_handler(event, context):
    playlog = get_playlog()
    print(playlog)
    upload_s3(playlog)



def upload_s3(playlog):

#    playlog_string = str(playlog)
    playlog_string = json.dumps(playlog)

    s3 = boto3.resource('s3')
    s3.Object('cbc-radio-2-spotify', 'playlog.json') \
            .put(Body=playlog_string)



def get_playlog():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day

    url = "https://www.cbcmusic.ca/Component/Playlog/GetPlaylog?stationId=110&date={}-{}-{}"\
            .format(year, month, day)

#    print(url)
    res = requests.get(url)
    playlog = res.json()

    return playlog








#lambda_handler(None, None)
