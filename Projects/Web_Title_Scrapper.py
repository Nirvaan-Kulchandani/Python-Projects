# 6️⃣ Web Scraper	    requests, beautifulsoup4	Scrape titles from a website

import requests
from bs4 import BeautifulSoup

# def fetch_data(url):
    
#     response = requests.get(url)
#     try:
#         if response.status_code == 200:
#             return response.text
#     except Exception:
#         print("Error while fetching data from the URL.")


def scrape_titles(url):

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    tag = 'h1'
    titles = soup.find_all(tag)

    try:
        if titles:
            print(f"{len(titles)} {tag} tag(s) found: ")
            for i, title in enumerate(titles, start=1):
                print(f"\t{i}. {title.get_text()}")
        else:
            print("No titles found in the HTML content.")
    except Exception:
        print("Error while scraping titles from the HTML content.")


scrape_titles("https://www.quickref.ME/")