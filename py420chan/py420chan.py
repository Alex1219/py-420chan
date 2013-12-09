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
		self.board = board
		self.no = no
		self.base_url = "{0}/{1}/res/{2}.json".format(API, board, no)
		self.threadjson =  requests.get(self.base_url).json()
		
		
	@property
	def now(self):
		return self.threadjson['posts'][0]['now']
		
	@property
	def name(self):
		return self.threadjson['posts'][0]['name']
		
	@property
	def id(self):
		return self.threadjson['posts'][0]['id']
	
	@property
	def sub(self):
		return self.threadjson['posts'][0]['sub']
	
	@property
	def com(self):
		return self.threadjson['posts'][0]['com']
	
	@property
	def filename(self):
		return self.threadjson['posts'][0]['filename']
	
	@property
	def ext(self):
		return self.threadjson['posts'][0]['ext']
		
	@property
	def w(self):
		return self.threadjson['posts'][0]['w']
	
	@property
	def h(self):
		return self.threadjson['posts'][0]['h']
	
	@property
	def h(self):
		return self.threadjson['posts'][0]['h']
	
	@property
	def tn_h(self):
		return self.threadjson['posts'][0]['tn_h']
	
	@property
	def time(self):
		return self.threadjson['posts'][0]['time']
	
	@property
	def fsize(self):
		return self.threadjson['posts'][0]['fsize']
	
	@property
	def replies(self):
		return self.threadjson['posts'][0]['replies']


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