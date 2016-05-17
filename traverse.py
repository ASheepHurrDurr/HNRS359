import json
import datetime

def isint(n):
    try:
        int(n)
        return True
    except ValueError:
        return False
def main():
    with open("2016-05-15 21-08_article-refs.csv","r", encoding="utf-8") as c:
        cites = {}
        for line in c.readlines():
            s = line.strip().split(", ")
            cite = [q.split(":") for q in s]
            for i in cite:
                if len(i) == 2 and isint(i[1]):
                    if i[0] in cites:
                        cites[i[0]] += int(i[1])
                    else:
                        cites[i[0]] = int(i[1])
    cites["other"] = 0
    for x in cites:
        if cites[x] < 10:
            cites["other"] += cites[x]
    json.dump(cites, open("{}_refs.csv".format(datetime.datetime.now().strftime("%Y-%m-%d %H-%M")), "w", encoding="utf-8"))


if __name__ == "__main__":
    main()
