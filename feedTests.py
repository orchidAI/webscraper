import feed

def testGetHtml():
    feeder = feed.feed()
    url = "https://en.wikipedia.org/wiki/Article"
    print(feeder.getHtml(url))

def testAll():
    testGetHtml()
    # testGetWikiBody()


if __name__ == "__main__":
    testAll()