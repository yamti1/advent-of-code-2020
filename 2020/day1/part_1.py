from .common import read_numbers

TARGET_SUM = 2020


def main():
    numbers = read_numbers()
    numbers.sort()
    results = find_sum_in_sorted_list(TARGET_SUM, numbers)
    product = results[0] * results[1]

    return product


def find_sum_in_sorted_list(target_sum, l):
    small, big = 0, -1
    while True:
        current_sum = l[small] + l[big]
        if current_sum > target_sum:
            big -= 1
            continue
        if current_sum < target_sum:
            small += 1
            continue
        return l[small], l[big]


if __name__ == "__main__":
    print(main())

