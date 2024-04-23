from textblob import TextBlob


def analysis(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment


def user_input():
    input_text = input("Enter your Sentence: ")
    sentiment = analysis(input_text)
    print(sentiment)


if __name__ == '__main__':
    user_input()
