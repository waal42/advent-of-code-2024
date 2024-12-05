from functions import blocks_of_lines, timer


@timer
def load_data(file):
    raw_rules, raw_pages = blocks_of_lines(file)
    rules = dict()
    for rule in raw_rules:
        if rule.split("|")[1] not in rules.keys():
            rules[rule.split("|")[1]] = [rule.split("|")[0]]
        else:
            rules[rule.split("|")[1]].append(rule.split("|")[0])
    pages = [page.split(",") for page in raw_pages]
    return rules, pages


@timer
def star_one(rules_in, pages_in):
    middle = list()
    for pages in pages_in:
        ordered = True
        for page in range(len(pages)):
            if ordered:
                for other in pages[page+1:]:
                    if pages[page] in rules_in.keys():
                        if other in rules_in[pages[page]]:
                            ordered = False
                            break
            else:
                break
        if ordered:
            middle.append(pages[len(pages)//2])
    return sum([int(page) for page in middle])
            


@timer
def star_two(data_in):
    pass


@timer
def main():
    # data = []
    rules, pages = load_data("day05input.txt")
    # print(rules, pages)
    print(star_one(rules, pages))
    # print(star_two(data))


if __name__ == "__main__":
    main()
