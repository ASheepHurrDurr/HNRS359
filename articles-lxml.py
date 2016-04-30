from lxml import etree

wikiFile = "enwiki-20160407-pages-articles.xml"
def main():
    with open("out.txt","w") as outfile:
        total = 0
        context = etree.iterparse(wikiFile, events=("start","end"))
        context = iter(context)
        event, root = next(context)
        for event, element in context:
            if element.text and event == "start" and element.tag == "{http://www.mediawiki.org/xml/export-0.10/}title":
                total += 1
                outfile.write("{}\n".format(element.text.encode("utf-8")))
            root.clear()
        outfile.write("{}\n".format(total))
        print("{} total articles".format(total))

if __name__ == "__main__":
    main()
