# #дз Написать код для класса Calculator, у которого есть все методы,
# которые выполняют математические операции = сложение, вычитание,
# деление, умножение. Класс должен быть покрыт тестами, в котором
# тестируется его работа, если пользователь забивает 1.цифру 2.букву 3.Пустой символ

from pytest import raises
from hometask12_calculator import Calculator
from decimal import Decimal, InvalidOperation, DivisionByZero

def test_add():
    assert Calculator.addition(1, 100500) == Decimal('100501')
    with raises(InvalidOperation):
        Calculator.addition('kek', 'лул')
    with raises(InvalidOperation):
        Calculator.addition(None, 1)
    with raises(InvalidOperation):
        Calculator.addition('', '')

def test_sub():
    assert Calculator.subtraction(-10, -12.009) == Decimal('2.009')
    with raises(InvalidOperation):
        Calculator.subtraction(1, 'haskell')
    with raises(InvalidOperation):
        Calculator.subtraction(1337, None)
    with raises(InvalidOperation):
        Calculator.subtraction('', '')

def test_mul():
    assert Calculator.multiplication(100, 3) == Decimal('300')
    with raises(InvalidOperation):
        Calculator.multiplication('one', 'two')
    with raises(InvalidOperation):
        Calculator.multiplication(None, None)
    with raises(InvalidOperation):
        Calculator.multiplication('', '')

def test_div():
    assert Calculator.division(1.23e+2, 2) == Decimal('61.5')
    with raises(InvalidOperation):
        Calculator.division(1, 'ab')
    with raises(InvalidOperation):
        Calculator.division(None, None)
    with raises(InvalidOperation):
        Calculator.division('', '')
    with raises(DivisionByZero):
        Calculator.division(1, 0)