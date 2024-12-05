import functools
from time import perf_counter


def timer(func):
    """- courtesy of filakrad"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):        
        start_time = perf_counter()
        value = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time} seconds.")
        return value
    return wrapper_timer


def comma_separated_line(filename):
    with open(filename, "r", encoding="utf-8") as file_in:
        return list(file_in.read().strip("\n").split(", "))


def lines(filename):
    with open(filename, "r", encoding="utf-8") as file_in:
        return list(file_in.read().split("\n"))
    
def lines_of_numbers(filename, separator=" "):
    with open(filename, "r", encoding="utf-8") as file_in:
        return [[int(num) for num in line.split(separator)] for line in file_in.read().splitlines()]


def blocks_of_lines(file_name):
    """Read a file into blocks of lines."""
    with open(file_name, "r", encoding="utf-8") as file_in:
        content = file_in.read().strip()
    return [block.splitlines() for block in content.split("\n\n")]


def tuples(filename):
    with open(filename, "r", encoding="utf-8") as file_in:
        return [tuple(map(int, line.split())) for line in file_in.readlines()]
    
def columns(filename):
    with open(filename, "r", encoding="utf-8") as file_in:
        data = [[int(x) for x in line.split()] for line in file_in.readlines()]
        return list(map(list, zip(*data)))


def comma_separated_ranges(filename):
    with open(filename, "r", encoding="utf-8") as file_in:
        data_out = list()
        for tuple in file_in.read().split("\n"):
            data_out.append([list(map(int, (range.split("-"))))
                            for range in tuple.split(",")])
        return data_out
