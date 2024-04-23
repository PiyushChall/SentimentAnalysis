from textblob import TextBlob


def analysis(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment


def converting_to_words(sentiment):
    if sentiment > 0.3:
        return "This is a positive sentence :)"
    elif sentiment < -0.3:
        return "This is a negative sentence :("
    else:
        return "This is a neutral sentence :|"


def main():
    input_text = input("Enter your Sentence: ")
    sentiment = analysis(input_text)
    statement = converting_to_words(sentiment)
    print(statement)


if __name__ == '__main__':
    main()
