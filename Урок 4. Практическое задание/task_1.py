"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается

И прошу вас обратить внимание, что то, что часто ошибочно называют генераторами списков,
на самом деле к генераторам отношения не имеет. Это называется "списковое включение" - list comprehension.
"""

from timeit import timeit

from numpy import number


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr

numbers_10 = [i for i in range(10)]
numbers_100 = [i for i in range(100)]
numbers_1000 = [i for i in range(1000)]


print(
    timeit(
        "func_1(numbers_10)",
        setup="from __main__ import func_1, numbers_10", number=100000))

print(
    timeit(
        "func_1(numbers_100)",
        setup="from __main__ import func_1, numbers_100", number=100000))

print(
    timeit(
        "func_1(numbers_1000)",
        setup="from __main__ import func_1, numbers_1000", number=100000))


print(
    timeit(
        "func_2(numbers_10)",
        setup="from __main__ import func_2, numbers_10", number=100000))

print(
    timeit(
        "func_2(numbers_100)",
        setup="from __main__ import func_2, numbers_100", number=100000))

print(
    timeit(
        "func_2(numbers_1000)",
        setup="from __main__ import func_2, numbers_1000", number=100000))

'''
func_1() оптимизирована через list comprehension.

Время исполнения на 100 000 вызовах функции: 

Для списка из 10 элементов:

func_1 = 0.10923670799999999
func_2(LC) = 0.11461066700000089

Для списка из 100 элементов:

func_1 = 0.772536334
func_2(LC) = 0.6708927500000001

Для списка из 1000 элементов:

func_1 = 8.180449584000002
func_2(LC) = 6.923252875000001

ВЫВОД: List comprehension позволяет оптимизировать значительно время
        только при увеличении вводимых элементов.
        Так же при работе с малым количеством элементов, ЦИКЛ проявляет себя незначительно быстрее LS.
'''
