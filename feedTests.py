import feed

def testGetHtml():
    feeder = feed.feed()
    url = "https://en.wikipedia.org/wiki/Article"
    print(feeder.getHtml(url))

def testGetBody():
    feeder = feed.feed()
    url = "https://en.wikipedia.org/wiki/Sexual_stimulation"
    print(feeder.getBody(url))

def testAll():
    testGetBody()
    # testGetWikiBody()


if __name__ == "__main__":
    testAll()