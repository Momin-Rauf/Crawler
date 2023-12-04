Assignment No 2 Documentation 
NAME: MUHAMMAD MOMIN RAUF
CMS 366523
SECTION BESE-12A
GITHUB REPOSITORY LINK :

Task: Implement a Web Spider(Crawler) with all the mentioned requirements given in the assignment
•	Tools used:
Programing Language: Python
•	Libraries: BeautifulSoup4 for crawling & flask for interacting with html file
•	CSS3 has been used for Styling
I have used request for sending http requests
GUI
Index.html
 
Search.html
 
File Structure:
Template (folder)
Index.html
Search.html
App.py (For connecting with html files using flask)
Crawler.py (For implementing Crawler) 


Total Functions
Crawler.py
•	def Extract(func):
this function sends http request to url after fetching it from the url queue
After getting a response, the response is sent to the func function


•	def HTML_parser(func):
using Beautiful Soup object parsing and sending it to func as an arg
•	def Crawl(soup):
implementing the main functionality of crawling
•	def getContent(query=None):
getting the data according to the query given by the user
App.py
•	def perform_crawling():
this function is defined to kepp crawling the website untill there is url in the queue to be crawled max_dept imported from the crawler is taken into consideration
•	def search():
this search method is trigered when query is given by the user in the form
