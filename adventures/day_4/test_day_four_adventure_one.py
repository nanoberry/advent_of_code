from adventures.day_4.day_four_adventure_one import find_all_xmas

def test_find_all_xmas_all_directions_one_matrix():
    matrix = [
        ['X', 'M', 'A', 'S', '.', '.', '.', '.'],  
        ['.', '.', '.', '.', '.', '.', '.', '.'],  
        ['X', '.', '.', '.', '.', '.', '.', '.'],  
        ['.', 'M', '.', '.', '.', '.', '.', '.'],  
        ['.', '.', 'A', '.', '.', '.', '.', '.'],  
        ['.', '.', '.', 'S', '.', '.', '.', '.'],  
        ['X', '.', '.', '.', '.', '.', '.', '.'],  
        ['M', '.', '.', '.', '.', '.', '.', '.'],  
        ['A', '.', '.', '.', '.', '.', '.', '.'],  
        ['S', '.', '.', '.', '.', '.', '.', '.'],  
    ]

    result = find_all_xmas(matrix)
    expected = 3
    assert result == expected, f"Expected {expected}, but got {result}"

test_find_all_xmas_all_directions_one_matrix()
