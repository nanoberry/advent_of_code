import sys
from collections import defaultdict

from adventures.day_1.file_parse_utils import parse_file_into_lists

def calculate_similarity_score_from_two_lists(list_1: list[int], list_2: list[int]) -> int:
    dict_of_list_2 = defaultdict(lambda:0)
    for id in list_2:
        dict_of_list_2[id] += 1
    similarity_score = 0
    for id in list_1:
        similarity_score += id * dict_of_list_2.get(id, 0)
    return similarity_score

def find_similarity_score_from_file(file_path: str) -> int:
    list_1, list_2 = parse_file_into_lists(file_path=file_path)
    return calculate_similarity_score_from_two_lists(list_1=list_1, list_2=list_2)

if __name__ == "__main__":
    file_path = sys.argv[1]
    print(find_similarity_score_from_file(file_path=file_path))

        