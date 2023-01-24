import requests
from bs4 import BeautifulSoup
import pandas as pd

class Scraper:
    def __init__(self):
        # website to scrape
        self.url = 'https://www.rentcafe.com/' 
        
        # empty list to store data
        self.data = []

        # list of cities and states
        self.uscities = pd.read_csv("C:/Users/kleib/Code/kleibo/Projects/Rent-Heat-Map/data/uscities.csv")

    def webScrape(self):
        state_abrv = self.uscities['state_id']
        city = self.uscities['city_ascii']
        city = city.str.replace(" ", "-")

        # Vectorization
        web_path = (self.url + 'average-rent-market-trends/us/' + state_abrv + '/' + city + '/').to_list()

        for i in web_path[:2]:
        # make a request to the website
            
            print(i)
            page = requests.get(str(i))
            print(page.status_code)
        # parse the HTML
            soup = BeautifulSoup(page.text, 'html.parser')


            print(soup.find('title'))

test = Scraper()
test.webScrape()

    