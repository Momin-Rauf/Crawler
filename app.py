# First of all I installed Flask using (pip install Flask)
#flask is used here for rendering the data on the search.html using templates
#when user enters the content to be searched data is crawled from the site and diplayed on the
# search.html file as key value pair 

#used request for sending http_requests


# Importing flask and render_template and request along with pandas
from flask import Flask, render_template, request
import pandas as pd  

#import crawl_page from crawler this in this crawl_page module all the implementation of the
#crawling is done
from crawler import Crawl, QUEUE_for_URLS, Depth_limit, getContent

app = Flask(__name__)


# this function is defined to kepp crawling the website untill there is url in the queue to be crawled max_dept imported from the crawler is taken into consideration 

def perform_crawling():
    global Depth_limit
    while QUEUE_for_URLS and Depth_limit > 0:
        Crawl()
        Depth_limit -= 1

#defining the routes of the homepage which is rendered first
@app.route('/')

#rendering the index.html in the start where form is given for the user for content search
def index():
    return render_template('index.html')

#route for search 
@app.route('/search', methods=['POST'])


#this search method is trigered when query is given by the user in the form
def search():
    query = request.form.get('query', '')
    
    #performing the crawling
    # we have used this link for crawling https://towardsdatascience.com/a-gentle-introduction-to-web-scraping-with-python-b914a64b2fb8

    if query:
        global QUEUE_for_URLS, Depth_limit
        QUEUE_for_URLS = ['https://towardsdatascience.com/a-gentle-introduction-to-web-scraping-with-python-b914a64b2fb8']
        Depth_limit = 3
        perform_crawling()

    result_dict = getContent(query)
    result_df = pd.DataFrame(list(result_dict.items()), columns=['Key', 'Value']).sort_values('Key')
    return render_template('search.html', query=query, result=result_df)



#main method
if __name__ == '__main__':
    app.run(debug=True)
