import requests
import json
import pprint
from collections import Counter
import re

API = 'http://api.420chan.org'

# def get_common_terms(comments):
#     comments = ' '.join(com for com in comments)
#     comments = comments.replace(',', ' ').replace('.', ' ').replace('?', ' ').replace('"', '')
#     c = Counter(comments.split()).most_common()
#     output = open('output.txt', 'w')
#     for i in c:
#         if i[1] > 5:
#             if isinstance(i[0], unicode):
#                 term = i[0].encode('ascii', 'ignore')
#             else:
#                 term = i[0]
#             if isinstance(i[1], unicode):
#                 n = i[1].encode('ascii', 'ignore')
#             else:
#                 n = i[1]
#             s = "{0} ({1})\n".format(term, n)
#             output.write(s)
#     output.close()

class Board(object):
    """
    Return an instance containing thread information for a particular board.
    """
    def __init__(self, board, pages=1, catalog=False):
        self.board = board
        self.pages = pages
        self.base_url = "{0}/{1}/{2}.json".format(API, self.board, 
                                        'catalog' if catalog else 'threads')
        self.json = requests.get(self.base_url).json()
        self.threads = self.get_threads()

    def __str__(self):
        return "/{0}/ ({1})".format(self.board, len(self.threads))

    def get_threads(self):
        _threads = []
        x = 0
        for pg in self.json:
            for t in pg['threads']:
                _threads.append(Thread(self.board, t['no']))
                x+=1
            if x == self.pages:
                return _threads


class Thread(object):

    def __init__(self, board, _id):
        self.base_url = "{0}/{1}/res/{2}.json".format(API, board, _id)
        self._id = _id
        self.json = requests.get(self.base_url).json()['posts']
        self.posts, self.subject = self.get_posts(self.json)

    def __str__(self):
        return ">>{0} {1}".format(self.thread_id, self.subject)

    def get_posts(self, posts):
        _posts = []
        _subject = ''
        for pst in self.json:
            p = Post(pst)
            try:
                _subject = p.sub
            except:
                pass
            _posts.append(p)
        return _posts, _subject


class Post(object):
    """
    Return an instance containing individual post information.
    """
    def __init__(self, post):
        self.sub = None
        self.tn_h = None
        self.tn_w = None
        self.h = None
        self.w = None
        self.fsize = None
        self.filename = None
        self.ext = None
        self.resto = None
        self.trip = None
        for opt, val in post.iteritems():
            setattr(self, opt, val)  

    def __str__(self):
       return ">>{0}".format(self.no)


def main():
    woo = Board('wooo')
    print woo.threads


if __name__ == '__main__':
    main()