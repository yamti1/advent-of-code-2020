from .common import read_numbers

TARGET_SUM = 2020


def main():
    numbers = read_numbers()
    numbers.sort()
    results = find_sum_of_three_in_sorted_list(TARGET_SUM, numbers)
    product = results[0] * results[1] * results[2]

    return product


def find_sum_of_three_in_sorted_list(target_sum, l):
    small, middle, big = 0, len(l)/2 , len(l)-1
    while small < big:
        current_sum = sum([l[small], l[middle], l[big]])
        if current_sum == target_sum:
            return l[small], l[middle], l[big]
        
        too_big = current_sum > target_sum
        middle_increment = -1 if too_big else 1
        stopping_condition = lambda: middle - small == 1 if too_big else lambda: big - middle == 1
        while not stopping_condition():
            middle += middle_increment
            
            current_sum = sum([l[small], l[middle], l[big]])
            if current_sum == target_sum:
                return l[small], l[middle], l[big]
        
        if too_big:
            big -= 1
        else:
            small += 1
        middle = (big + small) / 2
    
    raise ValueError("Sum not found")

if __name__ == "__main__":
    print(main())
