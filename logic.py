import random
from starlette.applications import Starlette
from starlette.responses import UJSONResponse
import uvicorn
import os
from random import uniform
import tweepy
import yaml

def main():
    COUNTRIES = "countries.txt"
    VERBS = "verbs.txt"
    GAMES = "games.txt"
    CONFLICTS = "conflicts.txt"

    with open(COUNTRIES) as f:
        countries_list = f.readlines()
    with open(VERBS) as f:
        verbs_list = f.readlines()
    with open(GAMES) as f:
        games_list = f.readlines()
    with open(CONFLICTS) as f:
        conflicts_list = f.readlines()

    countries_list = [x.strip() for x in countries_list]
    verbs_list = [x.strip() for x in verbs_list]
    games_list = [x.strip() for x in games_list]
    conflicts_list = [x.strip() for x in conflicts_list]

    c1 = random.choice(countries_list)
    countries_list.remove(c1)
    c2 = random.choice(countries_list)
    v = random.choice(verbs_list)
    g = random.choice(games_list)

    the_tweet = ""
    if random.random() > 0.5:
        cl = random.choice(conflicts_list)
        the_tweet = "What if %s %s %s during the %s? %s" % (c1, v, c2, cl, g)
    else:
        the_tweet = ("What if %s %s %s? %s" % (c1, v, c2, g))

    print(the_tweet)
    tweet(the_tweet)


def tweet(the_tweet):
    TWITTER_KEYS = "twitter_keys.yaml"
    # Twitter app configuration information: required
    with open (TWITTER_KEYS) as f:
        keys = yaml.load(f, Loader=yaml.FullLoader)

    CONSUMER_KEY = keys["consumer_key"]
    CONSUMER_SECRET = keys["consumer_secret"]
    ACCESS_KEY = keys["token"]
    ACCESS_SECRET = keys["secret"]

    assert all([CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET]
               ), "Not all Twitter app config tokens have been specified."

    # Request token: optional
    #REQUEST_TOKEN = os.environ.get('REQUEST_TOKEN', None)

    app = Starlette(debug=False)

    # Needed to avoid cross-domain issues
    response_header = {
        'Access-Control-Allow-Origin': '*'
    }

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth)
    api.update_status(the_tweet)


if __name__ == "__main__":
    main()


