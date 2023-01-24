import requests
from bs4 import BeautifulSoup
import pandas as pd

# list of websites to scrape
websites = [
    'https://www.rentcafe.com/',
    'https://www.rent.com/',
    'https://www.rentdata.org/'
]

# empty list to store scraped data
data = []

# loop through
for website in websites:
    # make a request to the website
    response = requests.get(website)

    # parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # find the rental price, city, state and website
    