from twython import Twython, TwythonError

#load the config file
config = {}
execfile("Cam2Twit_conf.py", config)

#create Twitter API object
twitter = Twython(config["app_key"],config["app_secret"],config["oauth_token"],config["oauth_token_secret"])

try:
    search_results = twitter.search(q='WebsDotCom', count=50)
except TwythonError as e:
    print e

for tweet in search_results['statuses']:
    print 'Tweet from @%s Date: %s' % (tweet['user']['screen_nam\
                                       e'].encode('utf-8'),
                                       tweet['created_at'])
    print tweet['text'].encode('utf-8'), '\n'
