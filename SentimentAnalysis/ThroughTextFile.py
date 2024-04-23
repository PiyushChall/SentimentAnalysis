from textblob import TextBlob


def analysis(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment


def get_file():
    with open("test.txt", "r") as f:
        text = f.read()
        return text


def main():
    text = get_file()
    value = analysis(text)
    print(value)


if __name__ == "__main__":
    main()
