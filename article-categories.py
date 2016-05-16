from lxml import etree
import re
import datetime
import codecs
from wikiUtil import idify, categoryRE, refRE, wikiRE

wikiFile = "enwiki-20160407-pages-articles.xml"
outFile = "{}_article-categories.csv".format(datetime.datetime.now().strftime("%Y-%m-%d %H-%M"))
def main():
    out = codecs.open(outFile,"w","utf-8")
    total = 0
    context = etree.iterparse(wikiFile, events=("start","end"))
    context = iter(context)
    event, root = next(context)
    for event, element in context:
        if event == "end" and element.tag == "{http://www.mediawiki.org/xml/export-0.10/}page":
            for child in element.iterdescendants():
                if child.tag == "{http://www.mediawiki.org/xml/export-0.10/}title" and not wikiRE.match(child.text):
                    for c in element.iterdescendants():
                        if c.tag == "{http://www.mediawiki.org/xml/export-0.10/}text":
                            if c.text:
                                if not "#REDIRECT" in c.text:
                                    total += 1
                                    out.write(idify(child.text))
                                    for m in categoryRE.findall(c.text):
                                        out.write(", " + idify(m))
                                    out.write("\n")
            element.clear()
        root.clear()
    out.write("{} total articles\n".format(total))
    print("{} total articles".format(total))
    out.close()


if __name__ == "__main__":
    main()
