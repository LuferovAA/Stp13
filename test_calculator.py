import calculator

def test_add():
    assert calculator.add(2, 3) == 5

def test_subtract():
    assert calculator.subtract(5, 2) == 3

def test_average():
    """НАМЕРЕННО НЕПРАВИЛЬНЫЙ ТЕСТ"""
    assert calculator.average([1, 2, 3]) == 10  # Должно быть 2, а не 10!
