"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым из них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from timeit import timeit
from collections import OrderedDict

dict_obj = {1: 'one', 2: 'two', 3: 'three'}
ordict_obj = OrderedDict(dict_obj)

print(type(dict_obj))
def dict_in():
    for i in range(4,7):
        dict_obj[i] = chr(93 + i)
    return dict_obj

def ordict_in():
    for i in range(4,7):
        ordict_obj[i] = chr(93 + i)
    return ordict_obj

def dict_get():
    dict_obj.get(3)
    return dict_obj

def ordict_get():
    ordict_obj.get(3)
    return ordict_obj

print(
    timeit(
        "dict_in()",
        setup="from __main__ import dict_in", number=100000))

print(
    timeit(
        "ordict_in()",
        setup="from __main__ import ordict_in", number=100000))

print(
    timeit(
        "dict_get()",
        setup="from __main__ import dict_get", number=100000))

print(
    timeit(
        "ordict_get()",
        setup="from __main__ import ordict_get", number=100000))



'''
Для 100 000 повторов:

Заполнение:
dict_in - 0.052789416
ordict_in - 0.050383874999999995

Получение элемента:
dict_get - 0.010291832999999986
ordict_get - 0.010450624999999991

Тип данных OrderedDict после Python3.6 потерял актуальность так как ключи-значения class 'dict' 
 перестали при выводе данных носить неупорядоченный характер.

Но при работе с .csv файлами OrderedDict используется до сих пор. 
'''