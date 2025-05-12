from collections import defaultdict
import sys


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
    pages_visited = set()
    for page in pages:
        if pages_visited.intersection(relative_order[int(page)]):
            return 0 
        pages_visited.add(page)
    return pages[len(pages)//2]

def find_middle_number_of_legal_lines(file_path: str) -> int:
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
    print(find_middle_number_of_legal_lines(file_path=file_path))




