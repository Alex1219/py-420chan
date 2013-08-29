import requests
import json
import pprint
from collections import Counter

API = 'http://api.420chan.org'

def get_common_terms(posts):
    posts = ' '.join(posts)
    print Counter(test.split()).most_common()

class Board(object):
    """
    Return an instance containing thread information for a particular board.
    """
    def __init__(self, board, detailed=False):
        self.base_url = "{0}/{1}/{2}.json".format(API, board, 
                                        'catalog' if detailed else 'threads')
        self.threads = requests.get(self.base_url).json()


class Thread(object):
    """
    Return an instance containing post information for a particular thread.
    """
    def __init__(self, board, thread_id):
        self.base_url = "{0}/{1}/res/{2}.json".format(API, board, thread_id)
        self.thread_id = thread_id
        self.posts, self.subject = self.get_posts(requests.get(self.base_url).json()['posts'])

    def __str__(self):
        return "[{0}]: {1}".format(self.thread_id, self.subject)

    def get_posts(self, posts):
        _posts = []
        _subject = ''
        for pst in posts:
            p = Post(pst)
            try:
                _subject = p.sub
            except:
                pass
        return _posts, _subject

class Post(object):
    """
    Return an instance containing individual post information.
    """
    def __init__(self, post_info):
        self.original_post = False
        for opt, val in post_info.iteritems():
            setattr(self, opt, val)   


#lol = Board('wooo')
#print lol.threads
thread = Thread('wooo', '3159492')
print(thread)
