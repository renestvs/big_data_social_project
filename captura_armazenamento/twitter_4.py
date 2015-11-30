import oauth2 as oauth
import json
import time

CONSUMER_KEY = "shYS8VE8csGaWh0r0ADqayHRT"
CONSUMER_SECRET = "QrPA2vRmDzBUXVIbIZkQIoYJCFaMPJzsqomp91RGE7NApXGoNq"
ACCESS_KEY = "2162977602-err5eNtwLqxeljQtMbOBJjXgKlE4EO1Cy78eBcf"
ACCESS_SECRET = "cH8HGKLfJRjJ7QB3wTteg7xICqyTJQ9LApGNWDD0RpyNZ"

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

q = 'Dilma' #termo a ser buscado
url = "https://api.twitter.com/1.1/search/tweets.json?q="+str(q)+"&count=100"+"&lang=pt"

response, data = client.request(url, "GET")
tweets = json.loads(data)
for tweet in tweets['statuses']:
	print str(tweet)

