import requests
from bs4 import BeautifulSoup
# from Utilities import *


class feed(object): #feeds the web crawler

    def __init__(self):
        return

    def getHtml(self, url):
        http = requests.get(url)
        soup = BeautifulSoup(http.content, "html.parser")
        return str(soup)



    def isASCII(string):
        for s in string:
            if(ord(s) > 127):
                return False
        return True

    def getBody(self, url):
        block = self.getHtml(url).splitlines()
        begin = "<p><b>" + self.getTitle(url)
        for i in block:
            if i.startswith(begin):
                startIndex = block.index(i)
        return startIndex
    

    def getTitle(self, url):
        block = self.getHtml(url).splitlines()[5][7:]
        individuals = block.split(" ")
        numWordsInTitle = individuals.index("-")
        title = ""
        for word in individuals[:numWordsInTitle]: 
            title += word + " "
        title = title[:-1]
        return title





