from django.shortcuts import render
from pymongo import MongoClient
from datetime import datetime

connection=MongoClient()
db=connection['test']

def home(request):
	return render(request,'myapp/home.html')

def view_notifications(request):
	return render(request,'myapp/view_notifications.html')

def twitter(request):
	results = db.newtweets.find().sort([("id", -1)])
	results = list(results)
	for result in results:
		print result

	return render(request,'myapp/twitter.html', {'results': results})


# def facebook(request):
# 	return render(request,'myapp/facebook.html')

def branches(request):

	return render(request,'myapp/branches.html')


def branch_data(request):
	return render(request,'myapp/branch_data.html')

def analysis(request):
	return render(request,'myapp/analysis.html')

def submit(request):
	info=request.POST['twitter']
	import twitter
	# import facebook
	api = twitter.Api(consumer_key = 'D45AD6GbKpE8vN6tCpYvIIZsT',
	consumer_secret = '9kHZC7KyH1kh4T1n298sMRcPwlGKGruMmS5OnDYw9WptGU4AMl',
	access_token_key = '143766231-SL0DxQAsxavibmDIwcsJENBQa83EQrZXODuRmX9I',
	access_token_secret = 'bk8dJ66csQVCFmggGbKSkm3sN5bewtLCTKmohvDBooHcA')
	status = api.PostUpdate(info)
	
	# graph = facebook.GraphAPI("EAAB7fdvk668BAJMZAsEwnxoPNkVeNMbGZC7BeLQVyA0QfPGI4A5f490MQ2uePv4ZC3C9CZBIkpoJLwqsyHdJpgm3T6nkwxQHeKVRH3pPISUYohBiwPSus4Yiak5ZChyC1dRglzX4jQUdvZCCsx4W3oXu1vTtc4YmeY2ZBJtbyXWw4aNIyi37ilDSvBfPelsMRkZD")	  
	# graph.put_object("me", "feed", message=info)
	return render(request,'myapp/home.html')	
	


