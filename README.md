# cbc-radio-2-spotify

A project to get CBC Radio 2 (CBC Music) onto a dynamically generated Spotify
playlist done using a AWS Lambda scheduled task.

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
4. Go to your Spotify account, and create 10 empty playlists
5. For each of your playlists paste the playlist id into `config.py`
    - Navigate to each of your playlists in the Spotify web player, your playlist id will be in the url
    (i.e. https://open.spotify.com/user/[username]/playist/[playlist_id])
6. Run `python3 spotify_token_cli_tool.py` to generate a Spotify access token that will be used by the script

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
1. Create a Python 3.6 runtime AWS Lambda function.
2. Add an CloudWatch Events trigger with the following scheduled rule: `cron(0 7 * * ? *)`
    - Note this is assuming PDT timezone

# Deployment

Run `$ bash deploy.sh`
