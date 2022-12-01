def get_puzzle_input(file_name, is_raw=False):
    return [line.strip("\n") if is_raw else line.strip() for line in open(f"data/{file_name}", "r").readlines()]
