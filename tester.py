from loginInstagram import *
from getPostsbyHashtag import *
from getCommnets_Likes_Post import *
from getRecentActivity import *
from getInfoUser import *
from funtionsApiInstagram import *
from getSuggested import *
from busquedaInstagram import *

import json
import pandas as pd
def readCredentilas():
	with open('credentials.json') as file:
		data = json.load(file)['credentials']
	return data
jsonData=readCredentilas()
session,head=login_Instagram_Session(jsonData['user'],jsonData['password'])
API=login_Instagram_Api(jsonData['user'],jsonData['password'])

# results=getPostsbyHashtag(session,head,API,'tech',5)
# print(results)

# results=getComentsPost(session,head,'https://www.instagram.com/p/B-2DXQEJ9EK/')
# print(results)
# results=getLikesPost(session,head,'https://www.instagram.com/p/B-2DXQEJ9EK/')
# print(results)

# results=getActivityRecent(session,head)
# print(results)

# results=getSuggested(session,head)
# print(results)

# results=busquedaInstagram(session,head,'hashtag','python')
# print(results)

# results=busquedaInstagram(session,head,'place','Mexico')
# print(results)

#results=getInfoUser(session,head,'itbearyoutube')
#print(results)

#follow(API,results['id'][0])
#unfollow(API,results['id'][0])

# results=getPostsbyHashtag(session,head,API,'tech',5)
# print(results)
# print(results['shortcode'][0])
# likePost(API,results['idpost'][0])
# commentPosts(API,results['idpost'][0],'Hola de parte de mi')
result=getTimeline(API,'itbearyoutube',8)
print(result)
