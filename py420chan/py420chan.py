import requests
import json

API = 'http://api.420chan.org'

class Board(object):
	"""
	Return an instance containing thread information for a particular board.
	"""
	
	def __init__(self,board, catalog=False):
		self.board = board
		self.catjson = requests.get("http://api.420chan.org/categories.json").json()['categories']
		self.boards = requests.get("http://api.420chan.org/boards.json").json()['boards']
		self.base_url = "{0}/{1}/{2}.json".format(API, board, 'catalog' if catalog else 'threads')
		
	def threads(self,pages):
		_threads = []
		totalpage = 0
		page = requests.get(self.base_url).json()
		while totalpage < pages:
			newpage  = page[totalpage]['threads']
			for thread in newpage:
				_threads.append(json.dumps(thread))
				totalpage += 1
			return _threads
	
	def boardinfo(self):
		"""
		Get category information on the board
		"""
		
		for board_ in self.boards:
			if  board_['board'].encode('utf-8') ==  self.board:
				return json.dumps(board_)
	
	def category(self,catnum):
		"""
		Get information on the caregory selected
		"""
		
		if catnum > 7:
			return None
		else:
			return json.dumps(self.catjson[catnum-1])
	

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
