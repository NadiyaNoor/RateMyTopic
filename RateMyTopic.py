import sys, csv, re
import tweepy
from textblob import TextBlob

class RateThis:

    def __init__(self):
        self.tweets = []
    

    def analyzeTweets(self, searchTopic, numOfTweets):
        ''' Getting Tweets and Analyzing Data'''

        # Authenticate Keys Provided by Twitter
        consumerKey = "8IsgAfkOJQDB6CE0x1UNp6ymc"
        consumerSecret = "NAWkRpoVhMPUBFGZ8Ov8WccsyWzs2EArfdt5fZmXqpDDAxwiwQ"
        accessToken = "1105641397640675328-y7AjMBlXBn3p0nTZCnShEpgzcR8CHd"
        accessTokenSecret = "h2vDCQ3foveZ4octreu68SiTFnk888smK3YMPAVigAwX9"
        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth)

        # Searching for Tweets
        self.tweets = tweepy.Cursor(api.search, q=searchTopic, lang = "en").items(numOfTweets)

        # Initailzing Varaibles to be Analyzed
        polarity = 0
        positive = 0
        negative = 0
        neutral = 0

        # Analyzing Sentiment/Polarity
        for tweet in self.tweets:
            analysis = TextBlob(tweet.text)
            polarity += analysis.sentiment.polarity

            if (analysis.sentiment.polarity == 0):
                neutral += 1
            elif (analysis.sentiment.polarity > 0):
                positive += 1
            else:
                negative += 1
        
        # Tweet Average
        positive = self.percentage(positive, numOfTweets)
        negative = self.percentage(negative, numOfTweets)
        neutral = self.percentage(neutral, numOfTweets)

        # Polarity Average
        polarity = polarity / numOfTweets

        return positive, neutral, negative 


    def cleanTweet(self, tweet):
        ''' Removing links, special characters, etc from tweet '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) 


    def percentage(self, part, whole):
        ''' Calculate Percentage '''
        perc = 100 * float(part) / float(whole)
        return format(perc, '.2f')