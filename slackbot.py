#!/usr/bin/env python

############################
#      Author: Brian Tilton
#        Date: 20151109
#       Title: slackbot.py
# Description: Script to send messages as Slack Bot
############################

import sys
import os
import urllib
import urllib2


##### Check Arg Count #####

if len(sys.argv) != 3:
    sys.exit('Usage: %s [channel] [message]' % sys.argv[0])


##### Token from file #####

tokenfile = open(os.path.dirname(os.path.realpath(__file__)) + "/slackbot-token.txt",'r')
tokenurl = tokenfile.read().split('\n')[0] + "&channel=%23"
print tokenurl

##### Arguments #####

channel = sys.argv[1]
message = sys.argv[2]


#####

url = tokenurl + channel
print url
req = urllib2.Request(url, message)
response = urllib2.urlopen(req)
print response.read()
