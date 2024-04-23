import requests
from bs4 import BeautifulSoup
from textblob import TextBlob


def analysis(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment


def analyze_article(url):
    # Get the response from the provided url by the user
    response = requests.get(url)
    if response.status_code == 200:
        # Parsing
        soup = BeautifulSoup(response.text, 'html.parser')
        article_text = ' '.join([p.get_text() for p in soup.find_all('p')])
        sentiment = analysis(article_text)
        return sentiment
    else:
        print("Failed to fetch article from the provided URL.")
        return None


def converting_to_words(sentiment):
    if sentiment > 0.5:
        return "This is a Strongly Positive sentence :)"
    elif 0 < sentiment <= 0.5:
        return "This is a Positive sentence :)"
    elif sentiment < -0.5:
        return "This is a Strongly Negative sentence :("
    elif -0.5 <= sentiment < 0:
        return "This is a Positive sentence :("
    else:
        return "This is a neutral sentence :|"


def main():
    article_url = input("Enter the URL of the article: ")
    sentiment_score = analyze_article(article_url)
    if sentiment_score is not None:
        statement = converting_to_words(sentiment_score)
        print(statement)


if __name__ == '__main__':
    main()
