def add(a, b):
    """Сложение"""
    return a + b

def subtract(a, b):
    """Вычитание"""
    return a - b

def multiply(a, b):
    """Умножение"""
    return a * b

def divide(a, b):
    """Деление"""
    if b == 0:
        raise ValueError("Деление на ноль!")
    return a / b

# НОВАЯ ФУНКЦИЯ - среднее арифметическое
def average(numbers):
    """Среднее арифметическое списка чисел"""
    if not numbers:
        raise ValueError("Список не может быть пустым")
    return sum(numbers) / len(numbers)
