import hello;

def test_add_two_floats():
    assert hello.add_two_numbers(1.0, 2.4) == 3.4
    assert hello.add_two_numbers(1.0, -1.0) == 0.0
