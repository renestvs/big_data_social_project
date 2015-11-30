import json
import tweepy
import time
import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.twitter_got

class StdOutListener(StreamListener):
    def on_data(self, data):
        tweet = json.loads(data)
        try:
            db.tweets.update({'id': tweet['id']},tweet, upsert=True)
        except (Exception):
            #Exceção: Aqui perdeu-se um tweet.
            pass
    def on_error(self, status):
        print (status)

class Crawler():
    default_parameters = {"CONSUMER_KEY": "{sua API key}",
                          "CONSUMER_SECRET": "{sua API secret}", 
                          "ACCESS_KEY": "{seu Acess Token}", 
                          "ACCESS_SECRET": "{seu Acess Token Secret}"}
    
    def __init__(self, param = default_parameters):
        self.params = param
    def crawleia(self,track):
        auth = tweepy.OAuthHandler(self.params['CONSUMER_KEY'], self.params['CONSUMER_SECRET'])
        auth.set_access_token(self.params['ACCESS_KEY'], self.params['ACCESS_SECRET'])
        api = tweepy.API(auth)
        l = StdOutListener()
        stream = Stream(auth, l)
        stream.filter(track = track)

if __name__ == '__main__':
    whie(True):
        try:
            c = Crawler()
            c.crawleia(['Dilma','Aecio','Marina Silva'])
        except(Exception):
            #Exemplo de exceção: perda de conexão.
            pass