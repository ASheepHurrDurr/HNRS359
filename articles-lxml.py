from lxml import etree
import codecs
import re

wikiFile = "enwiki-20160407-pages-articles.xml"
outFile = "articles.txt"
def main():
    with codecs.open(outFile,"w","utf-8") as out:
        wikiRE = re.compile(r"^(((Wikipedia)|(Category)|(Template)|(File)|(Portal)):)|(.+\(disambiguation\)\s*$)")
        total = 0
        context = etree.iterparse(wikiFile, events=("start","end"))
        context = iter(context)
        event, root = next(context)
        for event, element in context:
            if event == "start" and element.tag == "{http://www.mediawiki.org/xml/export-0.10/}title" and element.text and not wikiRE.match(element.text):
                total += 1
                out.write("{}:{}\n".format(total,element.text))
            root.clear()
        out.write("{} total articles\n".format(total))
        out.close()
        print("{} total articles".format(total))

if __name__ == "__main__":
    main()
