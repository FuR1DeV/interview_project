# 4. Написать программу, в которой реализовать две функции.
# В первой должен создаваться простой текстовый файл. Если файл с таким именем уже существует,
# выводим соответствующее сообщение. Необходимо открыть файл и подготовить два списка:
# с текстовой и числовой информацией. Для создания списков использовать генераторы.
# Применить к спискам функцию zip(). Результат выполнения этой функции должен должен
# быть обработан и записан в файл таким образом, чтобы каждая строка файла содержала
# текстовое и числовое значение. Вызвать вторую функцию. В нее должна передаваться ссылка
# на созданный файл. Во второй функции необходимо реализовать открытие файла и простой
# построчный вывод содержимого. Вся программа должна запускаться по вызову первой функции.

import random
import string
import os
from random import randint


def read_file(path):
    file = open(path, 'r', encoding='utf-8')
    for i in file.readlines():
        print(i)


def create_file():
    if os.path.exists('File.txt'):
        print('Файл уже существует!')
    my_file = open("File.txt", "w+", encoding='utf-8')
    text = [''.join(random.choice(string.ascii_lowercase) for _ in range(randint(1, 10))) for _ in range(1, 10)]
    numb = [randint(1, 100) for _ in range(1, 10)]
    for n, t in zip(text, numb):
        my_file.write(n + ' ' + str(t) + '\n')
    my_file.close()
    return read_file('File.txt')


create_file()
