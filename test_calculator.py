import calculator

def test_add():
    assert calculator.add(2, 3) == 5

def test_subtract():
    assert calculator.subtract(5, 2) == 3

def test_average():
    """Исправленный тест"""
    assert calculator.average([1, 2, 3]) == 2  # Теперь правильно!
