import hello


def test_add_two_floats(self):
    assert hw_1.add_two_numbers(1.0, 2.4) == 3.4
    assert hw_1.add_two_numbers(0.0, 0.0) == 0.0
    assert hw_1.add_two_numbers(-1.0, -1.2) == -2.2
    assert hw_1.add_two_numbers(1.0, -1.0) == 0.0
