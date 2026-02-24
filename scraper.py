import requests
from bs4 import BeautifulSoup

url = input("Enter website URL: ")

try:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    print("\nPage Title:")
    print(soup.title.string)

except requests.exceptions.RequestException:
    print("Error fetching the website.")
