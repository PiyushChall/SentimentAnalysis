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


def main():
    article_url = input("Enter the URL of the article: ")
    sentiment_score = analyze_article(article_url)
    if sentiment_score is not None:
        print("Sentiment Score:", sentiment_score)


if __name__ == '__main__':
    main()
