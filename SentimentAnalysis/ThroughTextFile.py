from textblob import TextBlob


def analysis(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment


def getFile():
    with open("test.txt", "r") as f:
        text = f.read()
        return text

if __name__ == "__main__":
    text = getFile()
    value = analysis(text)
    print(value)