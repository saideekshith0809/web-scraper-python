import requests
from bs4 import BeautifulSoup

def scrape_quotes(url):
    # Send request and get HTML
    response = requests.get(url)

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find quote elements
    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    # Display extracted data
    if not quotes:
        print("❌ No quotes found. Check the URL or page structure.")
        return

    for quote, author in zip(quotes, authors):
        print(quote.text)
        print("- " + author.text)
        print()

# ---- MAIN ----
url = input("Enter website URL to scrape: ")
scrape_quotes(url)

