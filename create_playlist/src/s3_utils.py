import boto3
import json
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY


def get_playlog():

    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )

    content = s3.get_object(Bucket='cbc-radio-2-spotify', Key='playlog.json')

    playlog = json.loads(content.get('Body').read().decode('utf-8'))

    return playlog

