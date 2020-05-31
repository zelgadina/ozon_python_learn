# #дз Написать код для класса Calculator, у которого есть все методы,
# которые выполняют математические операции = сложение, вычитание,
# деление, умножение. Класс должен быть покрыт тестами, в котором
# тестируется его работа, если пользователь забивает 1.цифру 2.букву 3.Пустой символ

from decimal import Decimal


def check_operands(func):
    def wrapper(a, b):
        a, b = Decimal(str(a)), Decimal(str(b))
        return func(a, b)
    return wrapper


class Calculator(object):
    @staticmethod
    @check_operands
    def addition(a, b):
        return a + b

    @staticmethod
    @check_operands
    def subtraction(a, b):
        return a - b

    @staticmethod
    @check_operands
    def multiplication(a, b):
        return a * b
    
    @staticmethod
    @check_operands
    def division(a, b):
        return a / b