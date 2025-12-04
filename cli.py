#!/usr/bin/env python3
"""
Командный интерфейс для калькулятора
"""
import calculator

def main():
    print("=== Калькулятор ===")
    print("Доступные операции: +, -, *, /, ^")
    
    try:
        a = float(input("Введите первое число: "))
        op = input("Введите операцию (+, -, *, /, ^): ").strip()
        b = float(input("Введите второе число: "))
        
        if op == '+':
            result = calculator.add(a, b)
        elif op == '-':
            result = calculator.subtract(a, b)
        elif op == '*':
            result = calculator.multiply(a, b)
        elif op == '/':
            result = calculator.divide(a, b)
        elif op == '^':
            result = calculator.power(a, b)
        else:
            print(f"Неизвестная операция: {op}")
            return
        
        print(f"Результат: {a} {op} {b} = {result}")
        
    except ValueError as e:
        print(f"Ошибка: {e}")
    except KeyboardInterrupt:
        print("\nВыход...")

if __name__ == "__main__":
    main()
