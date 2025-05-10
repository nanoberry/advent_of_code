import sys
from adventures.day_2.file_parse_utils import parse_file_into_array


def is_report_safe(list_1: list[int]) -> bool:
    if len(list_1) in (1, 0):
        return True
    compare = lambda first, second: second > first
    difference = lambda first, second: 1 <= abs(first-second) <= 3
    if list_1[1] < list_1[0]:
        compare = lambda first, second: second < first
    for i in range(len(list_1)-1):
        if not (compare(list_1[i], list_1[i+1]) and difference(list_1[i], list_1[i+1])):
            return False
    return True
  
def count_safe_reports(my_arr: list[list[int]]) -> int:
    safe_reports = 0
    for li in my_arr:
        safe_reports += is_report_safe(list_1 = li)
    return safe_reports

def count_valid_reports(file_path: str) -> int:
    my_arr = parse_file_into_array(file_path=file_path)
    return count_safe_reports(my_arr = my_arr)

if __name__ == "__main__":
    file_path = sys.argv[1]
    print(count_valid_reports(file_path=file_path))

    