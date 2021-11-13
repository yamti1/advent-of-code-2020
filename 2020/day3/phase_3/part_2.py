from functools import reduce

from .part_1 import load_input_map, count_trees_in_path


SLOPES = [
    # Right, Down
    (1, 1), 
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

def count_trees_through_slopes(map, slopes = SLOPES):
    return [count_trees_in_path(map, slope[0], slope[1]) for slope in slopes]


def main():
    print(
        reduce(
            lambda x, y: x * y, 
            count_trees_through_slopes(load_input_map())
    ))

if __name__ == "__main__":
    main()
