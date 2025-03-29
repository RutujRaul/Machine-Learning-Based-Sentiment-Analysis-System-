from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.5:
        label = "Very Positive"
    elif polarity > 0:
        label = "Positive"
    elif polarity == 0:
        label = "Neutral"
    elif polarity < -0.5:
        label = "Very Negative"
    else:
        label = "Negative"

    return {
        "label": label,
        "score": abs(polarity),  
        "neutral": 1 - abs(polarity) 
    }
