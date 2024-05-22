from textblob import TextBlob


def analysis(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment


def converting_to_words(sentiment):
    if sentiment > 0.5:
        return "This is a Strongly Positive sentence :)"
    elif 0 < sentiment <= 0.5:
        return "This is a Positive sentence :)"
    elif sentiment < -0.5:
        return "This is a Strongly Negative sentence :("
    elif -0.5 <= sentiment < 0:
        return "This is a Negative sentence :("
    else:
        return "This is a neutral sentence :|"


def main():
    input_text = input("Enter your Sentence: ")
    sentiment_score = analysis(input_text)
    print(sentiment_score)
    statement = converting_to_words(sentiment_score)
    print(statement)


if __name__ == '__main__':
    main()
