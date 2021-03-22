def test_file_iteration1():
    with open_input_file("unit6_input_data.txt") as f:
        lines = []
        # we are walking through f as an iterator, so even if file is huge this code acts like a buffered reader!!
        for line in f:
            lines.append(line.strip())
        assert ['one', 'two', 'three', 'four', 'five'] == lines

        lines = []
        for line in f:
            lines.append(line.strip())
        # what happened here? read the link i gave above.
        assert [] == lines