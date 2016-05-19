from lxml import etree
import re
import datetime
import codecs
import json
from wikiUtil import idify, categoryRE, refRE, wikiRE

wikiFile = "enwiki-20160501-pages-articles.xml"
outFile = "{}_article-refs.csv".format(datetime.datetime.now().strftime("%Y-%m-%d %H-%M"))
def main():
    out = codecs.open(outFile,"w","utf-8")
    total = 0
    context = etree.iterparse(wikiFile, events=("start","end"))
    context = iter(context)
    event, root = next(context)
    for event, element in context:
        if event == "end" and element.tag == "{http://www.mediawiki.org/xml/export-0.10/}page":
            elms = {}
            for child in element.iterdescendants():
                if child.tag == "{http://www.mediawiki.org/xml/export-0.10/}ns":
                    elms["ns"] = child.text
                elif child.tag == "{http://www.mediawiki.org/xml/export-0.10/}title":
                    elms["title"] = child.text
                elif child.tag == "{http://www.mediawiki.org/xml/export-0.10/}text":
                    elms["text"] = child.text
            if elms.get("ns") == "0" and elms.get("title") and elms.get("text") and "#redirect" not in elms["text"].lower():
                total += 1
                out.write(json.dumps({elms["title"]: refRE.findall(elms['text'])}) + "\n")
            element.clear()
            root.clear()
    out.write("{} total articles\n".format(total))
    print("{} total articles".format(total))
    out.close()


if __name__ == "__main__":
    main()
