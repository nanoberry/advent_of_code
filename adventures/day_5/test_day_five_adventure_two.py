from adventures.day_5.day_five_adventure_two import get_middle_from_illegal_lines

def test_get_middle_from_illegal_lines(tmp_path):
    content = """1|2
                2|3
                4,1,3
                3,2,1
                1,4,2
                2,1,4
                """
    test_file = tmp_path / "input.txt"
    test_file.write_text(content)
    result = get_middle_from_illegal_lines(str(test_file))
    assert result == 4
