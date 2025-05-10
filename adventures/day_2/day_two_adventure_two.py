import sys
from adventures.day_2.day_two_adventure_one import is_report_safe
from adventures.day_2.file_parse_utils import parse_file_into_array

def is_report_safe_with_one_flaw(list_1: list[int]) -> bool:
    if len(list_1) in (1, 0):
        return True
    compare = lambda first, second: second > first  # noqa: E731
    difference = lambda first, second: 1 <= abs(first-second) <= 3  # noqa: E731
    if list_1[1] < list_1[0]:
        compare = lambda first, second: second < first  # noqa: E731
    validate_neighbours = lambda first, second: compare(first, second) and difference(first, second)  # noqa: E731
    for i in range(len(list_1)-1):
        if not (validate_neighbours(list_1[i], list_1[i+1])):
            if i+1 == len(list_1) -1:
                return True
            if i==1:
                return is_report_safe(list_1[: i] + list_1[i+1:]) or is_report_safe(list_1[:i+1] + list_1[i+2:]) or is_report_safe(list_1[:i-1] + list_1[i:])
            return is_report_safe(list_1[: i] + list_1[i+1:]) or is_report_safe(list_1[:i+1] + list_1[i+2:])
      
    return True

def count_safe_reports_with_one_flaw(my_arr: list[list[int]]) -> int:
    safe_reports = 0
    for li in my_arr:
        safe_reports += is_report_safe_with_one_flaw(list_1 = li)
    return safe_reports

def count_valid_reports(file_path: str) -> int:
    my_arr = parse_file_into_array(file_path=file_path)
    return count_safe_reports_with_one_flaw(my_arr = my_arr)

if __name__ == "__main__":
    file_path = sys.argv[1] 
    print(count_valid_reports(file_path=file_path))