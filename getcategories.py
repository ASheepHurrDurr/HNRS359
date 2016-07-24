import json
import datetime
from wikiUtil import idify

def main():
    adjlist = {}
    revadjlist = {}
    total = 0
    articles = 0
    with open("2016-05-22 11-25_categories.txt", "r", encoding="utf-8") as infile:
        for line in infile:
            try:
                j = json.loads(line.strip())
                for i in j:
                    for k in j[i]:
                        total += 1
                        if i in adjlist:
                            adjlist[idify(i)].append(idify(k))
                        else:
                            adjlist[idify(i)] = [idify(k)]
                        if k in revadjlist:
                            revadjlist[idify(k)].append(idify(i))
                        else:
                            revadjlist[idify(k)] = [idify(i)]
            except Exception:
                print(line)
        converged = False
        newCats = {}
        with open("{}_adjList.json".format(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")), "w", encoding="utf-8") as adj:
            with open("{}_revAdjList.json".format(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")), "w", encoding="utf-8") as revadj:
                json.dump(adjlist, adj)
                json.dump(revadjlist, revadj)
        print("{} total cites".format(total))

if __name__ == "__main__":
    main()
