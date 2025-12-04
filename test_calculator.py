import calculator
import pytest

def test_add():
    """Тест сложения"""
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0

def test_subtract():
    """Тест вычитания"""
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(0, 5) == -5

def test_multiply():
    """Тест умножения"""
    assert calculator.multiply(3, 4) == 12
    assert calculator.multiply(0, 100) == 0

def test_divide():
    """Тест деления"""
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(5, 2) == 2.5
    
def test_divide_by_zero():
    """Тест деления на ноль"""
    with pytest.raises(ValueError, match="Нет мистер фиш"):
        calculator.divide(10, 0)

def test_power():
    """Тест возведения в степень"""
    assert calculator.power(2, 3) == 8
    assert calculator.power(5, 0) == 1

def test_all_operations():
    """Комплексный тест"""
    assert calculator.add(calculator.multiply(2, 3), calculator.subtract(10, 4)) == 12
