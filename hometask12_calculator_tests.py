# #дз Написать код для класса Calculator, у которого есть все методы,
# которые выполняют математические операции = сложение, вычитание,
# деление, умножение. Класс должен быть покрыт тестами, в котором
# тестируется его работа, если пользователь забивает 1.цифру 2.букву 3.Пустой символ

from pytest import raises
from hometask12_calculator import Calculator
from decimal import Decimal, InvalidOperation, DivisionByZero

def test_add_happy():
    assert Calculator.addition(1, 100500) == Decimal('100501')

def test_add_letters():
    with raises(InvalidOperation):
        Calculator.addition('kek', 'лул')

def test_add_none_a():
    with raises(InvalidOperation):
        Calculator.addition(None, 1)

def test_sub_happy():
    assert Calculator.subtraction(-10, -12.009) == Decimal('2.009')

def test_sub_letters():
    with raises(InvalidOperation):
        Calculator.subtraction(1, 'haskell')

def test_sub_none_b():
    with raises(InvalidOperation):
        Calculator.subtraction(1337, None)

def test_mul_happy():
    assert Calculator.multiplication(100, 3) == Decimal('300')
    
def test_mul_letters():
    with raises(InvalidOperation):
        Calculator.multiplication('one', 'two')

def test_mul_none_a_b():
    with raises(InvalidOperation):
        Calculator.multiplication(None, None)

def test_div_happy():
    assert Calculator.division(1.23e+2, 2) == Decimal('61.5')

def test_div_letters():
    with raises(InvalidOperation):
        Calculator.division(1, 'ab')

def test_div_none_a_b():
    with raises(InvalidOperation):
        Calculator.division(None, None)

def test_div_zero():
    with raises(DivisionByZero):
        Calculator.division(1, 0)