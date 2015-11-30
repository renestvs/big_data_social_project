import oauth2 as oauth
import json
import urllib
import time
import pymongo

client_mongo = pymongo.MongoClient("localhost", 27017)
db = client_mongo.nome_banco

CONSUMER_KEY = "{sua API key}"
CONSUMER_SECRET = "{sua API secret}"
ACCESS_KEY = "{seu Acess Token}"
ACCESS_SECRET = "{seu Acess Token Secret}"

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

q = 'Dilma'
max_id = '0'
continua = 1
URL = "https://api.twitter.com/1.1/search/tweets.json?q="+q+"&count=100"+"&lang=pt"

while(continua == 1):
        try:
                if(max_id == '0'):
                        pass
                        
                else:
                        URL = URL+"&max_id="+str(max_id)
                 
                max_id_ant = max_id
                response, data = client.request(URL, "GET")
                tweets = json.loads(data)
                for tweet in tweets['statuses']:

                        #Tweet capturado.
                        db.tweets.update({'id': tweet['id']},tweet, upsert=True)
                        max_id = tweet['id'] - 1

                time.sleep(2)
                if(max_id == max_id_ant):                     
                        continua = 0
                
        except Exception, e:

                time.sleep(15*60) #Pausa o crawler por 15 minutos.
                pass


