# cbc-radio-2-spotify

A project to get CBC Music (CBC Radio 2) onto a dynamically generated Spotify playlist using an AWS
Lambda scheduled task. A separate playlist for each of CBC Music's programs of the day will be created
in Spotify everyday.


# Setup

## Environment setup

```
# Clone and navigate to the repo
$ git clone https://github.com/jeffjyang/cbc-radio-2-spotify.git
$ cd cbc-radio-2-spotify

# Create your Python virtual environment
$ python3 -m venv env

# Start the virtual environment
$ source env/bin/activate

# Install dependencies  
$ pip install -r requirements.txt

```
To shutdown the virtual environment, run
```
$ deactivate
```

## Spotify setup
1. Create a Spotify developer account https://developer.spotify.com/dashboard/
2. On the dashboard click "CREATE A CLIENT ID", and follow the prompts
3. Into `config.py`, paste your `Client ID` and `Client Secret`, and your Spotify username.
4. Go to your Spotify account and create 10 empty playlists
5. For each of your playlists paste the playlist id into `config.py`
    - Navigate to each of your playlists in the Spotify web player, your playlist id will be in the url
    (i.e. https://open.spotify.com/user/[username]/playist/[playlist_id])
    - See [Discussion](#discussion) for the reasoning behind this
6. Run `$ python3 spotify_token_cli_tool.py` to generate a Spotify access token that will be used by the script

## AWS setup

### IAM user
1. Login to your AWS Management Console as root
2. Create an IAM user with `AWSLambdaExecute` permissions
3. Create an access key for the IAM user and paste the credentials into `config.py`

### S3
1. Create an S3 bucket and give read and write permissions to your IAM user.
Follow the guide in https://docs.aws.amazon.com/general/latest/gr/acct-identifiers.html to get
the canonical user ID for your IAM user
2. Paste the name of your bucket into `config.py`

### Lambda
1. Create a Python 3.6 runtime AWS Lambda function
2. Set the timeout of the Lambda function to a few minutes
    - This script tends to take roughly 1 to 2 minutes to execute
2. Add an CloudWatch Events trigger with the following scheduled rule: `cron(0 7 * * ? *)`
    - Note this is assuming PDT timezone

# Deployment

To run the script on your local machine, run `$ python3 lambda_cli_tool.py`

To deploy to Lambda, run `$ bash deploy.sh`


# Discussion

## The need to create 10 Spotify playlists

Spotipy, the Python client library for Spotify's API, does not support getting the playlist_id of a
Spotify playlist. This is an issue since Spotipy requires a playlist's playlist_id in order to
populate it with tracks.

As well, Spotify's API does not support the deletion of playlists. Since the number of programs on
CBC Music may differ each day, it is inevitable that we will end up with unused playlists on days
where CBC Music has fewer programs.

By creating a list of Spotify playlists, we can provide Spotipy a number of playlist_id's to use
when we want to add tracks to a playlist. Now, instead of requiring Spotipy to create playlists itself,
it can simply rename a playlist from "Inactive" to the title of one of CBC Music's programs when
it wants to add tracks to it. Likewise, if Spotipy wants to "delete" a playlist, it can simply
remove all tracks from the playlist and rename it to "Inactive".

The choice of creating 10 playlists is to ensure that we will not run out of playlists to use on
days where CBC Music has a relatively large number of programs. This tends to be about 8 programs
per day.
