import calculator

def test_add():
    assert calculator.add(2, 3) == 5

def test_subtract():
    assert calculator.subtract(5, 2) == 3

def test_average():
    """Тест для новой функции"""
    assert calculator.average([1, 2, 3, 4, 5]) == 3
    assert calculator.average([10, 20]) == 15
