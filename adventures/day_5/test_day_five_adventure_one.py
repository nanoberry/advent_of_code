import tempfile
import os
from adventures.day_5.day_five_adventure_one import find_middle_number_of_legal_lines

def test_find_middle_number_of_legal_lines():
    test_data =  """1|3
                    2|4
                    1,2,3
                    3,2,1
                    4,1,2
                    """
 
    with tempfile.NamedTemporaryFile(delete=False, mode='w+', suffix=".txt") as temp_file:
        temp_file.write(test_data)
        temp_file_path = temp_file.name

    try:
        result = find_middle_number_of_legal_lines(temp_file_path)
        assert result == 2
    finally:
        os.remove(temp_file_path)
