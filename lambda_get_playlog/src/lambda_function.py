import boto3
import requests
import json
import datetime
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY


def lambda_handler(event, context):
    playlog = get_playlog()
    upload_s3(playlog)


def upload_s3(playlog):

    playlog_string = json.dumps(playlog)

    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )

    s3.put_object(Body=playlog_string, Bucket='cbc-radio-2-spotify', Key='playlog.json')


def get_playlog():

    now = datetime.datetime.utcnow() - datetime.timedelta(hours=7, weeks=1)

    year = now.year
    month = now.month
    day = now.day

    url = "https://www.cbcmusic.ca/Component/Playlog/GetPlaylog?stationId=110&date={}-{}-{}"\
            .format(year, month, day)

    res = requests.get(url)
    playlog = res.json()

    playlog["timestamp"] = now.isoformat()

    return playlog


