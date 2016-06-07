import re
import json
import math

def idify(text):
    return text.strip().replace(" ", "_")
def inRange(num):
    total = 0
    for l in open("2016-05-19 10-00_article-refs.csv"):
        try:
            j = json.loads(l)
        except:
            print("oops")
        for k in j:
            if len(j[k]) > num:
                total += 1
    return total
def avgLen(num):
    total = 0
    count = 0
    for l in open("2016-05-31 07-05_article-refs.csv"):
        try:
            j = json.loads(l)
        except:
            print("oops")
        for k in j:
            total += 1
            count += j[k]
    average = count / total
    variance = 0
    for l in open("2016-05-31 07-05_article-refs.csv"):
        try:
            j = json.loads(l)
        except:
            print("oops")
        for k in j:
            variance += (j[k] - average)*(j[k] - average)
    return math.sqrt(variance / total)
def stddev():
    article = 0
    total = 0
    for l in open("2016-05-19 10-00_article-refs.csv"):
        article += 1
        try:
            j = json.loads(l)
        except:
            pass
        for k in j:
            total += len(j[k])
    average = total / article
    variance = 0
    for l in open("2016-05-19 10-00_article-refs.csv"):
        try:
            j = json.loads(l)
        except:
            pass
        for k in j:
            variance += (len(j[k]) - average)*(len(j[k]) - average)
    return math.sqrt(variance / article)
categoryRE = re.compile(r"\[\[(Category:.+?)(?:\|.*)*\]\]")
refRE = re.compile(r"(?:{{[cC]ite ([a-zA-Z\s]+))|{{([cC]itation).*}}")
wikiRE = re.compile(r"^(((Wikipedia)|(Category)|(Template)|(File)|(Portal)):)|(.+\(disambiguation\)\s*$)")
wikiFile = "enwiki-20160501-pages-articles.xml"
