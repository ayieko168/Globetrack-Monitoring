import tweepy
import json

auth = tweepy.OAuthHandler("8XGKvagxcmwj9kdtAuSLVDSA7", "lDVNbzpRYuC7vH6bMOfU9BzyWVOD69Oxx7DUBEImmXBCNPp9AF")
auth.set_access_token("2903795962-TUC4w4SQV9rA5GUnDAbYaOnXzej632if36LNkBK", "yaune6hyys23Gu6G8jb2Oi8XUS3RiL7IqjFQzeNQ08kLQ")

api = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        dictionary = status._json
        # print("\n\n", json.dumps(dictionary, indent=2))
        print("[TWWET] >> ", dictionary['text'])

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=MyStreamListener())
myStream.filter(track=['KRA', 'Kenya Revenue Authority', 'Revenue', 'Tax'])


