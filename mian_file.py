import urllib3
from bs4 import BeautifulSoup
from lxml import html
import requests
import webbrowser
import sys

class card():
    def __init__(self, reference):
        self.reference = reference
        self.url = "http://www.hager.pl/search/solr-search-test-page/70388.htm?solr%5Bq%5D="+ str(self.reference)

        self.http = urllib3.PoolManager()
        self.content = self.http.request('GET', self.url)
        self.soup = BeautifulSoup(self.content.data)
        self.name = self.soup.find(class_='solr-link solr-productnumber-link')

        self.url_profile = "http://www.hager.pl" + self.name.get('href')

        self.content_product = requests.get(self.url_profile)
        self.tree = html.fromstring(self.content_product.content)
        self.card = self.tree.xpath('//div[@class="button-container-right"]/a/@href')
        self.link  =  "http://www.hager.pl" + self.card[0]
        webbrowser.open_new(self.link)








if __name__ == "__main__":
    i = 1

    while sys.argv:
        name = str(sys.argv[i])
        ref = card(name)
        i+=1


