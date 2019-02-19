from gym_demo.formatting import list_to_columns


def test_list_to_columns():
    column_output = list_to_columns(["one", "two", "three", "four", "five"])
    lines = column_output.splitlines()
    assert len(lines) == 2
    assert "three" in lines[0]
    assert "four" in lines[1]
