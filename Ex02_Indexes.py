# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint

def find_indexes(array, minn, maxx):
    indexes = []
    for i in range(len(array)):
        if minn <= array[i] <= maxx:
            indexes.append(i)
    return indexes

array = [randint(-100,100) for i in range(10)]
print(array)

minn = int(input('Введите нижнюю границу диапазона: '))
maxx = int(input('Введите верхнюю границу диапазона: '))
print(find_indexes(array, minn, maxx))