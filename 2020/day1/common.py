NUMBERS_FILE = "phase_1/numbers.txt"

def read_numbers(filename=NUMBERS_FILE):
    numbers = open(filename, "r").readlines()
    numbers.pop()
    numbers = [int(num[:-1]) for num in numbers]
    return numbers
