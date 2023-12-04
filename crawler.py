#importing requests for making http requests
#importing BeatifulSoup 


import requests
from bs4 import BeautifulSoup

#Starting or seeding url from where we have to start our crawling
SEED = 'https://towardsdatascience.com/a-gentle-introduction-to-web-scraping-with-python-b914a64b2fb8'


#Objective no 1 Defined a Queue for storing the url which is actually an array
QUEUE_for_URLS = [SEED]

#used to store urls which are crawled
Crawled = set()

#Objective no 5 set the depth limit
Depth_limit = 3


#deifining the data dictionary for storing the data during the process of crawling
ContentStorage = {}




#this function sends http request to url after fetching it from the url queue
def Extract(func):
    def inner(*args, **kwargs):
        current_url = QUEUE_for_URLS[-1]
        try:
            page = requests.get(current_url)
            page.raise_for_status()
            Crawled.add(current_url)
            # After getting a response, the response is sent to the func function
            func(page, *args, **kwargs)
        except requests.exceptions.RequestException as e:  # Error handling Objective No. 9
            print(f'Error fetching {current_url}: {e}')
    return inner



#using Beautiful Soup object parsing and sending it to func as an arg
def HTML_parser(func):
    
    def inner(page, *args, **kwargs):
        soup = BeautifulSoup(page.content, 'html.parser')
        func(soup, *args, **kwargs)
    return inner

@Extract
@HTML_parser

#implementing the main functionality of crawling
def Crawl(soup):
    global QUEUE_for_URLS
    global Depth_limit

    # Extracting the information
    paragraphs = soup.find_all('p')
    for idx, paragraph in enumerate(paragraphs):
        ContentStorage[f'paragraph_{idx+1}'] = paragraph.text

    if Depth_limit > 0:
        links = soup.find_all('a', href=True)
        for link in links:
            next_url = link['href']
            if next_url not in Crawled and next_url not in QUEUE_for_URLS:
                QUEUE_for_URLS.append(next_url)

#This function collects all the data based on the query of the user
def getContent(query=None):
    if query:
        
        filtered_data = {}
        for key, value in ContentStorage.items():
            if query.lower() in value.lower():
                filtered_data[key] = value
        return filtered_data
    else:
        return ContentStorage