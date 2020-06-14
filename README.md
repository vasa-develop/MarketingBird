# MarketingBird, An open-source marketing tool to port/enagage your twitter follower base

## Setup

You need to prepare API keys at first.
Go to [the front page](https://apps.twitter.com/), create a new app, and generate a new access token.

Then put them as a key file at `~/.tweet.client.key`, with the format:

```
MY_SCREEN_NAME=xxxxxxxxxxxxxxxxxxx
MY_LANGUAGE=xx
CONSUMER_KEY=xxxxxxxxxxxxxxxxxxx
CONSUMER_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
ACCESS_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
ACCESS_TOKEN_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

If there is a key file named `tweet.client.key` in the current directory, `tweet.sh` will load it.
Otherwise, the file `~/.tweet.client.key` will be used as the default key file.

Moreover, you can give those information via environment variables without a key file.

```
$ export MY_SCREEN_NAME=xxxxxxxxxxxxxxxxxxx
$ export MY_LANGUAGE=xx
$ export CONSUMER_KEY=xxxxxxxxxxxxxxxxxxx
$ export CONSUMER_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
$ export ACCESS_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
$ export ACCESS_TOKEN_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
$ ./tweet.sh post "Hello!"
```

This form will be useful to implement a bot program.

And, this script uses some external commands.
You need to install them via package system on your environment: `apt`, `yum` or something.
Required commands are:

- `curl`
- `jq`
- `nkf`
- `openssl`

## Usage

```
python followers.py -a <twitter_handle> <cvs_file_name_to_store_follower_details>

// For eg

python followers.py -a simpleaswater_ followers.csv
```
