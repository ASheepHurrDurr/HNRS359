import lxml
wikiFile = "enwiki-20160407-pages-articles.xml"
def main ():
    with open("out.txt","wb") as output:
        xml.sax.parse(wikiFile, WikipediaXMLHandler(output))
        print("%d total articles" % count)

class WikipediaXMLHandler(xml.sax.ContentHandler):
    def __init__(self, file):
        self.map = {}
        self.output = file
        self.count = 0
    def startDocument(self):
        print("Parsing {}".format(wikiFile))
    def startElement(self, name, attrs):
        self.map[name] = ''
        self.tag = name
    def characters(self, content):
        self.map[self.tag] += content
    def endElement(self, name):
        if name == "title":
            self.count += 1
            self.output.write("{}\n".format(self.map[name]).encode("utf-8"))
    def endDocument(self):
        print("{} total articles".format(count))


if __name__ == "__main__":
    main()
