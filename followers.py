from bluebird import BlueBird
import os

for username in BlueBird().get_followers('simpleaswater_'):

    # Print out all the follower handles
    print(username)

    # Send DMs to every handle
    os.system('./tweet.sh direct-message @' +
              username + ' hey there! we will be sharing new Web 3.0 articles every week. Feel free to subscribe to our posts here: https://simpleaswater.com/signup/')
