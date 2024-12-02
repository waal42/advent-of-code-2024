from pprint import pprint
from functions import lines_of_numbers, timer


@timer
def load_data(file):
    report = dict()
    report["unchecked"] = lines_of_numbers(file, " ")
    return report


@timer
def star_one(data_in):
    safe = 0
    data_in["safe"] = list()
    data_in["unsafe"] = list()
    for levels in data_in["unchecked"]:
        if ((levels == sorted(levels) or levels == sorted(levels, reverse=True)) and all(1 <= abs(levels[i] - levels[i + 1]) <=3 for i in range(len(levels) - 1))):
            data_in["safe"].append(levels)
        else:
            data_in["unsafe"].append(levels)
    return len(data_in["safe"])



@timer
def star_two(data_in):
    data_in["tolerated"] = list()
    data_in["intolerated"] = list()
    for levels in data_in["unsafe"]:
        tolerated = False
        for i in range(len(levels)):
            dampened = levels[:i] + levels[i + 1:]
            if ((dampened == sorted(dampened) or dampened == sorted(dampened, reverse=True)) and all(1 <= abs(dampened[i] - dampened[i + 1]) <=3 for i in range(len(dampened) - 1))):
                tolerated = True
                break
        if tolerated:
            data_in["tolerated"].append((levels, dampened))
            tolerated = False
        else:
            data_in["intolerated"].append(levels)
    return len(data_in["safe"]) + len(data_in["tolerated"])


@timer
def main():
    # data = []
    report = load_data("day02input.txt")
    # print(data)
    print(star_one(report))
    print(star_two(report))


if __name__ == "__main__":
    main()
