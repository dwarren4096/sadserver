#!/usr/bin/python3

# https://api.twitter.com/1.1/statuses/user_timeline.json?count=5&exclude_replies=true&include_rts=false&user_id=116568685&screen_name=sadserver

#import tweepy

keyfile = open('api.key', 'r')
apikey = keyfile.read()
print("API Key:", apikey)

secretfile = open('api.secret', 'r')
apisecret = secretfile.read()
print("API Secret:", apisecret)

URL = "https://api.twitter.com/1.1/statuses/user_timeline.json"
PARAMS = ["user_id=116568685", "screen_name=sadserver", "count=5", "exclude_replies=true", "include_rts=false"]
#PARAMS.append("")

QUERY = '?'+PARAMS[0] #PARAMS concatenated, separated by & and prepended with a ?
for i in range(1, len(PARAMS)):
  QUERY += '&'+PARAMS[i]

print(URL+QUERY)