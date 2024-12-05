from functions import lines, timer
import re


@timer
def load_data(file):
    return lines(file)[0]


@timer
def star_one(data_in):
    pattern = re.compile(r"mul\(\d{1,3}\,\d{1,3}\)")
    matches = re.findall(pattern, data_in)
    total = 0
    for match in matches:
        total += eval(match[3:].replace(",", "*"))
    return total


@timer
def star_two(data_in):
    pattern = r"mul\(\d{1,3}\,\d{1,3}\)|don\'t\(\)|do\(\)"
    matches = [match.group() for match in re.finditer(pattern, data_in)]
    operational = True
    total = 0
    for instr in matches:
        if not operational and instr == "do()":
            operational = True
        elif operational and instr == "don't()":
            operational = False
        elif operational and re.match(r"mul\(\d{1,3}\,\d{1,3}\)", instr):
            total += eval(instr[3:].replace(",", "*"))
    return total


@timer
def main():
    # data = []
    data = load_data("day03input.txt")
    # print(data)
    print(star_one(data))
    print(star_two(data))


if __name__ == "__main__":
    main()
