# MarketingBird, An open-source marketing tool to port/enagage your twitter follower base

## Ongoing Work

The plan here is to build something like Zapier so that the users can create multiple flows and join them to get desired results.
This model can be scaled over other social media platforms too.

Here is the list of work we/I are/am doing, so that you can checkup our status:  

- Working CLI tool (Works with a single command) **[DONE]**: [DEMO](https://github.com/balajis/twitter-export/issues/1#issuecomment-643811801)
- Mockup for Zapier like interface for Dasboard UI **[DONE]**: [Youtube Video](https://youtu.be/16cJlX578gs)
- Creating a easy-to-use flow, so that anybody can start getting more info about their userbase. **[PENDING]**
  - A MarketingBird flow to scrape all the public data about an accounts followers and exporting it in user-firendly formats (spreadsheets, etc.)**[PENDING]**
  - A Dashbaord to analyse your scapred data (charts, comparisons, all analytics stuff)**[PENDING]**
  - A MarketingBird flow to use a spreadsheet (or a stream of data from another MarketingBird flow) to send DMs. We should be able to filter out the accounts with specific conditions (followers > 1000, or interested in #Bitcoin)**[PENDING]**
  - More stuff to be planned...


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
