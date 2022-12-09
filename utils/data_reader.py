short = (min, max, map, enumerate, len, range, int)


def get_puzzle_input(file_name, is_raw=False, is_str=False):
    line = [line.strip("\n") if is_raw else line.strip() for line in open(f"data/{file_name}", "r").readlines()]
    return line if not is_str else line[0]
