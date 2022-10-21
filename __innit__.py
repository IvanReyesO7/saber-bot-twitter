from time import gmtime, strftime
from lib.twitter_bot import TwitterBot
import yaml


def parsePeopleIWantToAnnoy():
    with open('./lib/people_i_want_to_annoy.yml', 'r') as f:
        return yaml.full_load(f)['people_i_want_to_annoy']

def timestampedMessage():
    return f', I am sending this message from a GitHub repo with GitHub actions at {strftime("%Y-%m-%d %H:%M:%S", gmtime())} (even though you didn\'t ask)'

users = parsePeopleIWantToAnnoy()
message = timestampedMessage()

twiiterBot = TwitterBot(users, message)
twiiterBot.send_message()
