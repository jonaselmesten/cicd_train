import calculator


class TestCalculator:

    def test_add(self):
        assert 4 == calculator.add(2, 2)

    def test_sub(self):
        assert 2 == calculator.subtract(4, 2)

    def test_string_add(self):
        assert isinstance(calculator.add_and_return_string(1, 2), str)
