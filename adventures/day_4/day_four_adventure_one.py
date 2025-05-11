import sys
from adventures.day_4.file_parse_utils import parse_file_into_array


def find_all_xmas(matrix: list[list[str]]) -> int:
    xmas = 0
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if element == 'X':
                coordinates_of_ms = check_if_M_nearby(matrix=matrix, i=i, j=j)
                for coord in coordinates_of_ms:
                    a_coordinates = ((coord[0] + (coord[0] - i)), (coord[1] + (coord[1] - j)))
                    s_coordinates = ((a_coordinates[0] + (a_coordinates[0] - coord[0])), (a_coordinates[1] + (a_coordinates[1] - coord[1])))
                    print(a_coordinates, s_coordinates)
                    if s_coordinates[0] > len(matrix) -1 or s_coordinates[0] < 0 or s_coordinates[1] > (len(row) -1) or s_coordinates[1] < 0:
                        continue
                    xmas += check_if_as(matrix=matrix, coordinates=(a_coordinates, s_coordinates))
    return xmas



def check_if_M_nearby(matrix: list[list[str]], i: int, j: int) -> list[tuple[int, int]]:
    new_i_options = [i]
    if i!=0:
        new_i_options.append(i-1)
    if i!= len(matrix)-1:
        new_i_options.append(i+1)
    new_j_options = [j]
    if j!=0:
        new_j_options.append(j-1)
    if j!= len(matrix[0])-1:
        new_j_options.append(j+1)
    m_coordinates = []
    for option_i in new_i_options:
        for option_j in new_j_options:
            if option_i == i and option_j == j:
                continue
            if matrix[option_i][option_j] == 'M':
                m_coordinates.append((option_i, option_j))
    return m_coordinates

def check_if_as(matrix: list[list[str]], coordinates: tuple[tuple[int, int], tuple[int, int]]) -> int:
    a_coordinates = coordinates[0]
    s_coordinates = coordinates[1]
    if matrix[a_coordinates[0]][a_coordinates[1]] == 'A' and matrix[s_coordinates[0]][s_coordinates[1]] == 'S':
        return 1
    return 0

def find_all_xmas_from_file(file_path: str) -> int:
    my_matrix = parse_file_into_array(file_path=file_path)
    xmas = find_all_xmas(matrix=my_matrix)
    return xmas

if __name__ == "__main__":
    file_path = sys.argv[1]
    print(find_all_xmas_from_file(file_path=file_path))
