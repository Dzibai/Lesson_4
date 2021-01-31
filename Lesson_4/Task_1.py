from timeit import timeit
from random import randint
from cProfile import run

# 3 задача из 2 урока

# _num = randint(10 ** numb, 10 ** (numb + 1))
# Генерирую число с n-ным кол-вом цифр


# Способ 1, через рекурсию
def _func1(_numb):
    _num = randint(10 ** _numb, 10 ** (_numb + 1))
    return _num


def func1(numb):
    if numb < 10:
        return numb
    else:
        return int(f'{numb % 10}{func1(numb // 10)}')


print(timeit('func1(_func1(100))', number=100, globals=globals()))  # 0.009900177999999999
print(timeit('func1(_func1(500))', number=100, globals=globals()))  # 0.170061974
print(timeit('func1(_func1(900))', number=100, globals=globals()))  # 0.6825906620000001
run('func1(_func1(900))')

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.007    0.007 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 Task_1.py:12(_func1)
#    901/1    0.007    0.000    0.007    0.007 Task_1.py:17(func1)
#        1    0.000    0.000    0.000    0.000 random.py:174(randrange)
#        1    0.000    0.000    0.000    0.000 random.py:218(randint)
#        1    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#        1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

print('-' * 30)
# Способ 2, через переворот строки


def func2(numb):
    _num = randint(10 ** numb, 10 ** (numb + 1))
    res = ''
    for number in str(_num):
        res = f'{number}{res}'
    return res


print(timeit('func2(10)', number=100, globals=globals()))    # 0.0004110429999999998
print(timeit('func2(100)', number=100, globals=globals()))   # 0.0011177480000000017
print(timeit('func2(1000)', number=100, globals=globals()))  # 0.016645423
run('func2(10000)')

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#       1    0.005    0.005    0.005    0.005 Task_1.py:45(func2)
#       1    0.000    0.000    0.000    0.000 random.py:174(randrange)
#       1    0.000    0.000    0.000    0.000 random.py:218(randint)
#       1    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#       1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#       1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       3    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

print('-' * 30)

# Способ 3, через массив


def func3(numb):
    _num = randint(10 ** numb, 10 ** (numb + 1))
    result = ''
    i = 0
    lst = []
    for a in str(_num):
        lst.append(a)
    for _ in lst:
        result = f'{lst[i]}{result}'
        i += 1
    return result


print(timeit('func3(10)', number=100, globals=globals()))    # 0.0008091650000000006
print(timeit('func3(100)', number=100, globals=globals()))   # 0.0043829520000000025
print(timeit('func3(1000)', number=100, globals=globals()))  # 0.034301927999999995
run('func3(10000)')

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000    0.007    0.007 <string>:1(<module>)
#        1    0.006    0.006    0.007    0.007 Task_1.py:73(func3)
#        1    0.000    0.000    0.000    0.000 random.py:174(randrange)
#        1    0.000    0.000    0.000    0.000 random.py:218(randint)
#        1    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#        1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
#   10001    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#       1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


# В результате можно сделать вы вод, что переворот строки оказался наилучшим вариантом для решения этой задачи, так как
# он имеет константную сложность. Второй вариант лучше и в плане времени выполнения и в плане обьема самого кода,
# вариант с рекурсией оказался очень не эффективным!


