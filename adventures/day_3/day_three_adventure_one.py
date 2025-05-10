import re
import sys

def multiply_legal_muls(file_path: str) -> list[list[int]]:
    legal_muls = list()
    with open(f'{file_path}', 'r') as f:
        for line in f:
            legal_muls.extend(re.findall(r"mul\((\d{1,3}),\s*(\d{1,3})\)", line))
    total_mul = 0
    for legal_mul in legal_muls:
        num_1, num_2 = legal_mul
        total_mul += int(num_1)*int(num_2)
    return total_mul

if __name__ == "__main__":
    file_path = sys.argv[1]
    print(multiply_legal_muls(file_path=file_path))
