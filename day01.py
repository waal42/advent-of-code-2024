from functions import columns, timer


@timer
def load_data(file):
    return columns(file)


@timer
def star_one(data_in):
    return sum([abs(y - x) for x, y in zip(sorted(data_in[0]), sorted(data_in[1]))])


@timer
def star_two(data_in):
    right_column = dict()
    for number in data_in[1]:
        if number in right_column.keys():
            right_column[number] += 1
        else:
            right_column[number] = 1
    total = 0
    for number in data_in[0]:
        if number in right_column.keys():
            total += number * right_column[number]
    return total


@timer
def main():
    # data = []
    data = load_data("day01input.txt")
    # print(data)
    print(star_one(data))
    print(star_two(data))


if __name__ == "__main__":
    main()
