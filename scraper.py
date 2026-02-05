import requests
from bs4 import BeautifulSoup

def scrape_quotes(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    for quote, author in zip(quotes, authors):
        print(quote.text)
        print("- " + author.text)
        print()

url = input("Enter website URL: ")
scrape_quotes(url)
