#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tweepy


# In[ ]:


import tweepy
import time
twitter_auth_key = {
        "oauth_consumer_key" : "ChGgg0SyY2utG7LMh9JOye932",
        "oauth_consumer_secret" : "yRj7uTBieALMataSClF0zShCq8hqBZvxVuWYx61pAbV8Olpags",
        "oauth_access_token" : "1278713407277944833-rt35awdTwbLz5frzeaFzNcx8t5V93F",
        "oauth_access_token_secret" : "NObugQoVo1wb8vyyAvN7iKy78TxnV9Oo1mvSWwLqLZRhB"
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
        
            break
while True:
    main()
    time.sleep(20)


# In[ ]:




