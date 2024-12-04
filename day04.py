from functions import lines, timer


@timer
def load_data(file):
    return lines(file)


@timer
def star_one(data_in):
    word = "XMAS"
    rows = len(data_in)
    cols = len(data_in[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]
    total = 0

    def next_letter(x, y, dx, dy, position):
        if position == len(word):
            return True
        if x < 0 or x >= rows or y < 0 or y >= cols or data_in[x][y] != word[position]:
            return False
        found = next_letter(x + dx, y + dy, dx, dy, position + 1)
        return found

    for row in range(rows):
        for col in range(cols):
            if data_in[row][col] == word[0]:
                for dx, dy in directions:
                    if next_letter(row, col, dx, dy, 0):
                        total += 1

    return total


@timer
def star_two(data_in):
    x_masses = ["MSMS", "MSSM", "SMMS", "SMSM"]
    rows = len(data_in)
    cols = len(data_in[0])
    total = 0
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if data_in[row][col] == "A":
                for x_mas in x_masses:
                    if data_in[row-1][col-1] == x_mas[0] and data_in[row+1][col+1] == x_mas[1] and data_in[row+1][col-1] == x_mas[2] and data_in[row-1][col+1] == x_mas[3]:
                        total += 1
    return total


@timer
def main():
    # data = []
    data = load_data("day04input.txt")
    # print(data)
    print(star_one(data))
    print(star_two(data))


if __name__ == "__main__":
    main()
