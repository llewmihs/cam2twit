from twython import TwythonStreamer, Twython

#load the config file
config = {}
execfile("Cam2Twit_conf.py", config)

class MyStreamer(TwythonStreamer):
  def on_success(self, data):
    if 'text' in data:
      print data['text'].encode('utf-8')
        
  def on_error(self, status_code, data):
    print status_code, data

#create Twitter API object
stream = MyStreamer(config["app_key"],config["app_secret"],config["oauth_token"],config["oauth_token_secret"])

#stream.user()

list = stream.statuses.filter(track='*******')
