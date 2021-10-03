import tweepy

auth = tweepy.OAuthHandler("v77b43mpLKdyiTjKU0FVLzXqf", "GfFIDUbCgRzl0c1jrlKAUlgFuB95sb0uFCOsR8LHR6N0ifAbFz")
auth.set_access_token("2903795962-M2gsCURRx8RbiES36kmcil1QFl9V9S7MfkqBYVC", "yj3M9TMIh8gHOOHWbPkvRHyyrCxeWNQi0jsn2hzRTrGdh")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(f"Tweet >> {tweet.text}\n\n")


