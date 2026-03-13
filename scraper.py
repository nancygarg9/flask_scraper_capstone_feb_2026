# this module is used for scraping - core logic is here

# functions to scrape quotes and build Pandas DF.

import requests
import pandas as pd 
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.DEBUG)

def scrape_quotes(limit=5):  #default arg
    url = "https://quotes.toscrape.com/"
    # url="https://books.toscrape.com/" # enhance using this for books and author
    response = requests.get(url) # fetches webpage. 
    if response.status_code!=200: # 200 is for successful fetch, and you can later enhance it by using multiple try and except block here. for eg if you get 404 - you can catch the exception and print a better message like Page not found.
        logging.error("Failed to fetch the website and it returned code as : ", response.status_code)
        return [] # store them in a list but here since we didnt get the webage we return an empty list
    
    soup = BeautifulSoup(response.text,"html.parser") # parses the html response that we received above from that url.
    #print(soup.prettify())
    #<span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>
    quotes = [q.text  for q in soup.find_all("span", class_="text")]  #list comprehension
    # quotes will be list of all the quotes - just the text that we wanted.
    #return quotes # list of ALL the quotes but i shud return only the limit
    return quotes[:limit] # 0-4 get the first five quotes, start=0, stop =limi-1,

# Pandas Dataframe - very handy for tabular form of representation
def quotes_to_df(quotes):

    df = pd.DataFrame(quotes,columns=["Quote"])
    # convert our list of quotes into pandas timeframe that will look something like this:

    '''
        Quote
    0   <actual quote>“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
    1   “It is our choices, Harry, that show what we truly are, far more than our abilities.”

    '''

    return df



