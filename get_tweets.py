from twython import Twython, TwythonError, TwythonStreamer
import json
from pymongo import MongoClient
from datetime import datetime
from pytz import timezone


APP_KEY='89EQ56Eu68qqcrsyZsRoMrvkn'
APP_SECRET='RG91hfKTDapKrbgs2VBLUIVuVQ2ySsJjiamamd7ZBgA657Yg3f'
OAUTH_TOKEN='3037145274-2sQqGfMUIEp6doT5sgdOAed9LuQjz4pZkbBSZoG'
OAUTH_TOKEN_SECRET='Z4bnlRu0PepUh3TjR72JyTQ8huT0L1EgNGaoi3kbKaMyC'

connection=MongoClient()
db=connection['test']


class MyStreamer(TwythonStreamer):
	def on_success(self, data):
		if 'text' in data:
			print data['text'].encode('utf-8')
			print data['created_at']
			d= datetime.strptime(data['created_at'],'%a %b %d %H:%M:%S +0000 %Y').timezone(UTC + 0530)
			#d = pytz.timezone('Asia/Calcutta').localize(d)
			data['date'] = d.strftime('%d-%m-%Y')
			data['time'] = d.strftime('%H:%M')
			data['status'] = "unresolved"
			tweet_record=data
			tweet_record['newid']=data['id_str']
			db['newtweets'].insert(tweet_record)

	def on_error(self, status_code, data):
		print status_code,data

stream = MyStreamer(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
stream.statuses.filter(track='@dtptraffic')


