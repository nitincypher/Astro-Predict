# import libraries
import urllib.request as urllib2
from bs4 import BeautifulSoup
import configparser

def getObjectList():
    # specify the url
    quote_page = 'https://www.astroleague.org/al/obsclubs/urban/urbanld.html'

    config = configparser.ConfigParser()
    config.read('../config.ini')
    if config['PROXY']['USE_PROXY'] == "true":
        #Comment The Proxy Block if you don't require
        #Proxy Block
        proxy = urllib2.ProxyHandler({
            'http': config['PROXY']['HTTP'],
            'https': config['PROXY']['HTTPS']
        })
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
        #Proxy Block
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)

    # query the website and return the html to the variable ‘page’
    page = urllib2.urlopen(quote_page)

    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')

    # Take out the <div> of name and get its value
    table = soup.find('table', attrs={'border': '1'})
    rows = table.findAll(lambda tag: tag.name=='tr')

    #Take out names, urls, processed image count for the row entries
    data=[]
    firstElement=True #Flag to remove table header
    for row in rows:
        if firstElement==True:
            firstElement=False
            continue
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        if cols[0]:
            data.append(cols[0]) # Get rid of empty values
    return data
