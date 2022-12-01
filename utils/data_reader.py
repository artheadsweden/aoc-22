# import builtins
# from typing import List


# def read_task(file_name: str, sep: str =',', t: type =None):
#     data = [value.strip() for value in open(file_name, 'r', encoding='utf-8').read().strip().split(sep)][0]
#     match t:
#         case builtins.int:
#             data = [d for d in data.split()]
#             return [int(d) for d in data]
#         case _:
#             return data
#     # Add more wrappers as needed


def get_puzzle_input(file_name, is_raw=False):
    return [line.strip("\n") if is_raw else line.strip() for line in open(f"data/{file_name}", "r").readlines()]
