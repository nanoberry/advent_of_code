import re
import sys

def multiply_legal_muls_after_do(file_path: str):
    with open(file_path, 'r') as file:
        data = file.read()

    tokens = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", data)

    mul_enabled = True
    total = 0

    for token in tokens:
        if token == "do()":
            mul_enabled = True
        elif token == "don't()":
            mul_enabled = False
        elif token.startswith("mul("):
            if mul_enabled:
                a, b = map(int, token[4:-1].split(","))
                total += a * b

    return total

if __name__ == "__main__":
    file_path = sys.argv[1]
    print(multiply_legal_muls_after_do(file_path=file_path))