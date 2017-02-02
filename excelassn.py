import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'xgv7RXDAz3LptgruQCQ3ahIjp'
consumer_secret= '6F6UG4PHN0LfshdMWqY2x7PpcPtqqYEHLO5uoo2MmXi9b5hQ5p'

access_token='826273655181041664-VAh7wSgwrBswiCLbHnfZX6TZBHjT6Ol'
access_token_secret='hbxjBMgYEarhZArO8EzO1ll0vicqMMBpdysFmxkbiCztS'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('sports')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")