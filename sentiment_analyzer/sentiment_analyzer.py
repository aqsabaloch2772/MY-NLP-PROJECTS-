# Project: Sentiment Analyzer
# Description: Classifies text sentiment as Positive, Negative, or Neutral

from textblob import TextBlob

def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Example usage
print(get_sentiment("I love learning about Artificial Intelligence!"))
print(get_sentiment("This course is okay."))
print(get_sentiment("I hate waiting for results."))
