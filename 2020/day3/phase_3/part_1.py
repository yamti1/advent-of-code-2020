
STEP_RIGHT_SIZE = 3
STEP_DOWN_SIZE = 1
INPUT_MAP_FILENAME = "input.txt"
TREE = "#"


def load_input_map(input_map_filename: str = INPUT_MAP_FILENAME):
    with open(input_map_filename, 'r') as f:
        return [line.strip() for line in f]


def count_trees_in_path(map, 
                        step_right_size: int = STEP_RIGHT_SIZE, 
                        step_down_size: int = STEP_DOWN_SIZE) -> int:
    offset = 0
    counter = 0
    map_width = len(map[0])
    for line in map[::step_down_size]:
        if line[offset] == TREE:
            counter += 1
        offset += step_right_size
        offset %= map_width
    return counter


def main():
    print(count_trees_in_path(load_input_map()))


if __name__ == "__main__":
    main()
