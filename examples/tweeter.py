import tweepy
import random
import re
import time
from py420chan import py420chan as wooo

consumer_key=''
consumer_secret=''
access_token='' 
access_token_secret=''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def get_posts():
    woo = wooo.Board('wooo', pages=5)
    posts = []
    for thread in woo.threads:
        for p in thread.posts:
            posts.append(p.com)
    return posts

def clean_posts():
    posts = get_posts()
    _posts = []
    for p in posts:
        if p == 'ARMBARS EVERYWHERE':
            pass
        elif len(p) > 140:
            pass
        else:
            p = re.sub("\d{7}", "", p).replace('>>', '')
            _posts.append(p)
    return _posts


if __name__ == "__main__":
    
    posts = clean_posts()
    api = tweepy.API(auth)
    while True:
        time.sleep(1200)
        if posts:
            index = random.randrange(len(posts))
            tweet = posts.pop(index)
            if tweet == None or len(tweet) < 5:
                pass
            else:
                try:
                    api.update_status(tweet)
                except:
                    pass
