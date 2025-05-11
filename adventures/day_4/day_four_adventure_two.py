import sys

from adventures.day_4.file_parse_utils import parse_file_into_array


def find_x_mas_crosses(matrix: list[list[str]]):
    x_mas = 0
    for i, rows in enumerate(matrix):
        for j, value in enumerate(rows):
            if i in (0, len(matrix)-1) or j in (0, len(rows)-1):
                continue
            if matrix[i][j] == "A":
                if (matrix[i-1][j-1] == "M" and matrix[i+1][j+1] == "S") or (matrix[i-1][j-1] == "S" and matrix[i+1][j+1] == "M"):
                    if (matrix[i-1][j+1] == "M" and matrix[i+1][j-1] == "S") or (matrix[i-1][j+1] == "S" and matrix[i+1][j-1] == "M"):
                        x_mas +=1
    return x_mas

def find_x_mas_crosses_from_file(file_path: str):
    my_matrix = parse_file_into_array(file_path=file_path)
    return find_x_mas_crosses(matrix=my_matrix)


if __name__ == "__main__":
    file_path = sys.argv[1]
    print(find_x_mas_crosses_from_file(file_path=file_path))