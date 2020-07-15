#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tweepy


# In[ ]:
# I cannot disclose by oauth_consumer_key ,oauth_consumer_secret ,oauth_access_token and oauth_access_token_secret as it is intended for Specific user Only.
# You can get these keys By creating your  twitter Developer account which is free of cost. Just visit https://developer.twitter.com/.

import tweepy
import time
twitter_auth_key = {
        "oauth_consumer_key" : "*****************",
        "oauth_consumer_secret" : "************************",
        "oauth_access_token" : "****************************************",
        "oauth_access_token_secret" : "**************************"
        
    }
auth = tweepy. OAuthHandler (twitter_auth_key['oauth_consumer_key'], twitter_auth_key['oauth_consumer_secret'])
auth.set_access_token(twitter_auth_key['oauth_access_token'], twitter_auth_key['oauth_access_token_secret'])
api = tweepy.API(auth)
def main():
    tweets = api.user_timeline(screen_name='@ANI')
    for i in range(len(tweets)):
        try:
            api.retweet(tweets[0].id)
        except:
            time.sleep(20)
            break
        
Print("Retweeting")          
while True:
    main()
    time.sleep(20)


# In[ ]:




