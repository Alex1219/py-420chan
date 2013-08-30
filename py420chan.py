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
        return ">>{0} {1}".format(self.thread_id, self.subject)

    def get_posts(self, posts):
        _posts = []
        _subject = ''
        for pst in posts:
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
    def __init__(self, post_info):
        for opt, val in post_info.iteritems():
            setattr(self, opt, val)  

    def __str__(self):
       return ">>{0}".format(self.no)

all_threads = []
all_posts = []
all_comments = []
board = Board('wooo').threads
for page in board:
    page_threads = page['threads']
    for th in page_threads:
        all_threads.append(Thread('wooo', th['no']))
for thread in all_threads:
    all_posts.append(thread.posts)

for i in all_posts:
    for j in i:
        all_comments.append(j.com.replace('\r', '').replace('\n', ''))

#print all_posts


# for post in all_posts:
#     all_comments.append(post.com)
# print all_comments



    #for th in page_threads:
    #print page
    #print x
       # _threads = [thread['no'] for thread in page_threads]
      #  print _threads
    #print page_threads
# for th in all_threads:
#     print th.keys()
#     _th = Thread('wooo', th['no']).posts
#     posts.append(_th)
# print posts
# thread = Thread('wooo', '3159492')
# posts = thread.posts
# get_common_terms(all_comments)