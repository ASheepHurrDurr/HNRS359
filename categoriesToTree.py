import json
def main():
    categories = {}
    with open("2016-05-14 21-10_categories.txt", "r", encoding="utf-8") as input:
        for line in input:
            a = line.strip().split(",")
            cat = a[0]
            for i in range(1, len(a)):
                if a[i] in categories:
                    categories[a[i]].append(cat)
                else:
                    categories[a[i]] = [cat]
    with open("category-tree.txt", "w", encoding="utf-8") as output:
        output.write(json.dumps(categories))
    output.close()

if __name__ == "__main__":
    main()
