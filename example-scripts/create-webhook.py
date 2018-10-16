from TwitterAPI import TwitterAPI

import os

CONSUMER_KEY = os.environ.get('CONSUMER_KEY', None)
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET', None)

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', None)
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET', None)

#The environment name for the beta is filled below. Will need changing in future		
ENVNAME = 'env-beta'
WEBHOOK_URL = '{URL HERE}'


twitterAPI = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

r = twitterAPI.request('account_activity/all/:%s/webhooks' % ENVNAME, {'url': WEBHOOK_URL}, None, 'POST')

print r.text
       
