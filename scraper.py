import requests
from bs4 import BeautifulSoup

def scrape_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = [title.text for title in soup.find_all('h2')]
        return titles
    else:
        return []

if __name__ == "__main__":
    url = "https://example.com"
    print(scrape_data(url))