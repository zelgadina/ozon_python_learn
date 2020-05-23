from matplotlib import pyplot
from simple_benchmark import benchmark


def calc_of_for(number, powers=6):
    cycle = []
    for n in range(2, powers):
        cycle.append(number**n)
    return cycle

def calc_of_comprehension(number, powers=6):
    cycle = [number**n for n in range(2, powers)]
    return cycle

def calc_of_while(number, powers=6):
    cycle = []
    n = 2
    while n < powers:
        cycle.append(number**n)
        n += 1
    return cycle

def calc_of_recursion(number, powers=5):
    if powers == 2:
        return [number**powers]

    else:
        rec = calc_of_recursion(number, powers-1)
        rec.append(number**powers)
        return rec

def calc_of_hardcode(number):
    return [number**2, number**3, number**4, number**5]


assert calc_of_for(2)[-1] == 32
assert calc_of_comprehension(2)[-1] == 32
assert calc_of_while(2)[-1] == 32
assert calc_of_recursion(2)[-1] == 32
assert calc_of_hardcode(2)[-1] == 32


funcs = [
        calc_of_for,
        calc_of_while,
        calc_of_comprehension,
        calc_of_recursion,
        calc_of_hardcode
        ]

arguments = {}
for i in range(10000):
    arguments[f'i{i}'] = i
arguments_name = 'series of natural numbers'

aliases = {
            calc_of_for: "for",
            calc_of_while: "while",
            calc_of_comprehension: "list comprehension",
            calc_of_recursion: "recursion",
            calc_of_hardcode: "hardcode"
            }

b = benchmark(funcs, arguments, arguments_name, function_aliases=aliases)
b.plot()
pyplot.savefig('powers_of_number.png')
pyplot.show(b)