from timeit import timeit


# Первый вариант, через «Решето Эратосфена»
def func1(n, num):
    array = [i for i in range(n)]
    array[1] = 0
    for i in range(2, n):
        if array[i] != 0:
            j = i + i
            while j < n:
                array[j] = 0
                j += i
    result = [i for i in array if i != 0]
    return result[num - 1]


print(timeit('func1(1000, 1)', number=100, globals=globals()))    # 0.025213326
print(timeit('func1(10000, 1)', number=100, globals=globals()))   # 0.25847677999999996
print(timeit('func1(100000, 1)', number=100, globals=globals()))  # 2.761469309
print('-' * 30)


# Второй вариант, через проверку на простоту числа
def prime(b):
    a = 2
    while b % a != 0:
        a += 1
    return a == b


def func2(_n, _num):
    array = [i for i in range(_n)]
    array[1] = 0
    for i in range(2, _n):
        if array[i] != 0 and prime(array[i]) is False:
            array[i] = 0
        i += 1
    result = [i for i in array if i != 0]
    return result[_num - 1]


print(timeit('func2(1000, 1)', number=100, globals=globals()))    # 0.44384444000000034
print(timeit('func2(10000, 1)', number=100, globals=globals()))   # 35.883198657
print(timeit('func2(100000, 1)', number=100, globals=globals()))  # Ждал больше 10минут, не дождался

# Вывод: Первый способ через «Решето Эратосфена» оказался очень эффективным, а второй способ через классическоую
# проверку на простоту числа даже не смог справится с массивом из 100_000 чисел.


