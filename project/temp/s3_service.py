import boto3
import json
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

def upload_s3(playlog):

#    playlog_string = str(playlog)
    playlog_string = json.dumps(playlog)



    s3 = boto3.resource('s3')
    s3.Object('cbc-radio-2-spotify', 'playlog.json') \
            .put(Body=playlog_string)
