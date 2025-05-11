def parse_file_into_array(file_path: str) -> list[list[int]]:
    list_of_lists = []
    with open(f'{file_path}', 'r') as f:
        for line in f:
            list_of_lists.append(list(line))

    return list_of_lists