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
            ns = element.find("{http://www.mediawiki.org/xml/export-0.10/}ns")
            title = element.find("{http://www.mediawiki.org/xml/export-0.10/}title")
            rev = element.find("{http://www.mediawiki.org/xml/export-0.10/}revision")
            if rev is not None and title is not None and ns is not None and ns.text == "0":
                content = rev.find("{http://www.mediawiki.org/xml/export-0.10/}text")
                if content is not None and "#REDIRECT" not in content.text:
                    total += 1
                    out.write(title.text)
                    for i in categoryRE.findall(content.text):
                        out.write(", " + i)
                    out.write("\n")
            element.clear()
        root.clear()
    out.write("{} total articles\n".format(total))
    print("{} total articles".format(total))
    out.close()


if __name__ == "__main__":
    main()
