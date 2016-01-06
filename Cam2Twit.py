import time
#import the twitter module
from twython import Twython

#import PiCam
import picamera

#load the config file
config = {}
execfile("Cam2Twit_conf.py", config)

#create Twitter API object
twitter = Twython(config["app_key"],config["app_secret"],config["oauth_token"],config["oauth_token_secret"])

tweeter = raw_input("Who would you like to tweet?",)
print tweeter

message = raw_input("What is your message?",)
print message

twit_message = tweeter + ' ' + message

print twit_message
camera = picamera.PiCamera()

camera.capture('image.jpg')

time.sleep(4)

photo = open('image.jpg', 'rb')
response = twitter.upload_media(media = photo)

twitter.update_status(status = twit_message, media_ids=[response['media_id']])
