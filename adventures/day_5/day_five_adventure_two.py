from collections import defaultdict
import functools
import sys


def smaller(first: int, second:int, relative_order: dict):
    if second in relative_order.get(first, {}):
        return -1
    if first == second:
        return 0
    return 1

def make_dict_from_comparison(file_path: str) -> dict[int, set]:
    relative_order = defaultdict(set)
    with open(file_path, 'r') as f:
        for line in f:
            if '|' not in line:
                continue
            first_second = [int(x.strip()) for x in line.split('|')]
            if len(first_second)<= 1:
                break
            relative_order[int(first_second[0])].add(first_second[1])
    return relative_order

def check_if_legal_line(pages: list[int], relative_order: dict[int, set]) -> int:
    sorted_pages = sorted(pages, key=functools.cmp_to_key((lambda x, y: smaller(first=x, second=y, relative_order=relative_order))))
    if pages == sorted_pages:
        return 0
    return sorted_pages[len(sorted_pages)//2]

def get_middle_from_illegal_lines(file_path: str):
    middle_page_sum = 0
    relative_order = make_dict_from_comparison(file_path=file_path)
    with open(file_path, 'r') as f:
        for line in f:
            if ',' not in line:
                continue
            page_numbers = [int(x) for x in line.split(',')]
            middle_page_value = check_if_legal_line(pages=page_numbers, relative_order=relative_order)
            middle_page_sum += middle_page_value
    return middle_page_sum

if __name__ == "__main__":
    file_path = sys.argv[1]
    print(get_middle_from_illegal_lines(file_path=file_path))


    
