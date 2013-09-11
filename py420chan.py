import requests
import json


API = 'http://api.420chan.org'


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
        print("Gathering threads from {0} page(s) on {1}".format(self.pages, self.board))
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
                print("{0} threads acquired".format(len(_threads)))
                return _threads


class Thread(object):
    """
    Return an instance containing post information for a particular thread.
    """
    def __init__(self, board, no):
        self.base_url = "{0}/{1}/res/{2}.json".format(API, board, no)
        self.no = no
        self.json = requests.get(self.base_url).json()['posts']
        self.posts, self.subject = self.get_posts(self.json)

    def __str__(self):
        return ">>{0} {1}".format(self.no, self.subject)

    def get_posts(self, posts):
        _posts = []
        _subject = ''
        for pst in self.json:
            p = Post(pst)
            if p.no == self.no:
                _subject = p.sub
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
    woo_threads = woo.threads
    for thread in woo_threads:
        print(thread)


if __name__ == '__main__':
    main()