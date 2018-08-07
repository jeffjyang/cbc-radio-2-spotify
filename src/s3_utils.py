import boto3
import datetime
import json
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, UTC_OFFSET

def upload_s3(playlog):

    playlog_string = json.dumps(playlog)

    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )

    now = datetime.datetime.utcnow() + datetime.timedelta(hours=UTC_OFFSET, weeks=-1)

    key = "playlog-" + now.strftime("%Y-%m-%d")

    s3.put_object(Body=playlog_string, Bucket='cbc-radio-2-spotify', Key=key)
