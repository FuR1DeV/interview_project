from random import randint
# 3. Разработать генератор случайных чисел.
# В функцию передавать начальное и конечное число генерации (нуль необходимо исключить).
# Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону:
# “elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.


def random_int(a, b):
    return randint(a, b)


sps = [random_int(1, 10) for i in range(1, 11)]
dicts = {}
keys = range(0, 10)
for i in keys:
    dicts['elem_' + str(i)] = sps[i]

print(sps)
print(dicts)

