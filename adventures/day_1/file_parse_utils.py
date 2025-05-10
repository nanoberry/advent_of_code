def parse_file_into_lists(file_path: str) -> tuple[list[int], list[int]]:
    list_1 = []
    list_2 = []
    with open(f'{file_path}', 'r') as f:
        for line in f:
            num1, num2 = map(int, line.split())
            list_1.append(num1)
            list_2.append(num2)
    return list_1, list_2