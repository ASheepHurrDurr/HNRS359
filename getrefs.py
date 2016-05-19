import json
import datetime
import operator

def main():
    cites = {}
    total = 0
    articles = 0
    noRefs = 0
    with open("2016-05-19 10-00_article-refs.csv", "r", encoding="utf-8") as infile:
        for line in infile:
            try:
                j = json.loads(line.strip())
                for i in j:
                    if len(j[i]) == 0:
                        noRefs += 1
                    else:
                        for k in j[i]:
                            if len(k[0].strip().lower()) > 0 and k[0].strip().lower() in cites:
                                cites[k[0].strip().lower()] += 1
                            elif len(k[0].strip().lower()) > 0 and k[0].strip().lower() not in cites:
                                cites[k[0].strip().lower()] = 1
                            elif len(k[1].strip().lower()) > 0 and k[1].strip().lower() in cites:
                                cites[k[1].strip().lower()] += 1
                            elif len(k[1].strip().lower()) > 0 and k[1].strip().lower() not in cites:
                                cites[k[1].strip().lower()] = 1
                            total += 1
                articles += 1
            except json.decoder.JSONDecodeError:
                print(line)
        with open("{}_refs.json".format(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")), "w", encoding="utf-8") as outFile:
            json.dump(cites, outFile)
        with open("{}_refs.csv".format(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")), "w", encoding="utf-8") as csvOut:
            for i in cites:
                csvOut.write(i.replace(",","") + "," + str(cites[i]) + "\n")
        print("{} total articles".format(articles))
        print("{} total cites".format(total))
        print("{} articles had no citations".format(noRefs))
        print("{} average number of cites per article".format(total / articles))

if __name__ == "__main__":
    main()
