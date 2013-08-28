import requests
import json
import pprint


API = 'http://api.420chan.org'


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
        self.posts, self.original_post = self.get_posts(requests.get(self.base_url).json()['posts'])

    def __str__(self):
        return "[{0}]:{1}".format(self.thread_id, self.original_post)

    def get_posts(self, posts):
        _posts = []
        _op = ''
        for pst in posts:
            p = Post(pst)
            if not p.original_post:
                _posts.append(p)
            else:
                _op = p
        return _posts, _op


class Post(object):
    """
    Return an instance containing individual post information.
    """
    def __init__(self, post_info):
        self.original_post = False
        for opt, val in post_info.iteritems():
            setattr(self, opt, val)   
            if opt == 'sub':
                self.original_post = True


#Board('wooo')
thread = Thread('wooo', '3159492')
print(thread)
