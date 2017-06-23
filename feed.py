import requests
from bs4 import BeautifulSoup
# from Utilities import *


class feed(object): #feeds the web crawler


    def getHtml(self, url):
        http = requests.get(url)
        soup = BeautifulSoup(http.content, "html.parser")
        return soup

    def getWikiBody(url):
        html = getHtml(url)

