import sys
from adventures.day_1.file_parse_utils import parse_file_into_lists

def total_distance_between_two_lists(list_1: list[int], list_2: list[int])-> int:
    copy_list_1 = list_1.copy()
    copy_list_2 = list_2.copy()
    copy_list_1.sort()
    copy_list_2.sort()
    total_diff = 0
    for i in range(max(len(copy_list_1), len(copy_list_2))):
        if i >= len(copy_list_1):
            total_diff += copy_list_2[i]
        elif i >= len(copy_list_2):
            total_diff += copy_list_1[i]
        else:
            total_diff += abs(copy_list_2[i] - copy_list_1[i])
    return total_diff


def get_total_diff_from_file(file_path: str) -> int:
    list_1, list_2 = parse_file_into_lists(file_path=file_path)
    return total_distance_between_two_lists(list_1 = list_1, list_2 = list_2)

if __name__ == "__main__":
    file_path = sys.argv[1]
    print(get_total_diff_from_file(file_path = file_path))

