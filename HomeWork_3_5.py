# 5. Усовершенствовать первую функцию из предыдущего примера.
# Необходимо во втором списке часть строковых значений заменить на значения
# типа example345 (строка+число). Далее — усовершенствовать вторую функцию
# из предыдущего примера (функцию извлечения данных). Дополнительно реализовать
# поиск определенных подстрок в файле по следующим условиям: вывод первого вхождения,
# вывод всех вхождений. Реализовать замену всех найденных подстрок на новое значение и
# вывод всех подстрок, состоящих из букв и цифр и имеющих пробелы только
# в начале и конце — например, example345.

import random
import string
import os
from random import randint


def read_file(path):
    file = open(path, 'r', encoding='utf-8')
    u = 0
    for i in file.readlines():
        if ' ' not in i:  # Вывод строк состоящих из букв и цифр без пробелов
            if 'a' in i and u == 0:  # Находим подстроку в строке и меняем её на новое значение
                print(f"Вывод первого вхождения 'a' в строке {i}, найденная подстрока меняется"
                      f" на новое значение ЭЛЬЧОКОПОКО! {i.replace('a', 'ЭЛЬЧОКОПОКО')}")
                u += 1
            elif 'a' in i:
                print(f"Вывод остальных вхождений 'a' в строке {i}, найденная подстрока меняется"
                      f" на новое значение ЭЛЬЧОКОПОКО! {i.replace('a', 'ЭЛЬЧОКОПОКО')}")


def create_file():
    if os.path.exists('File.txt'):
        print('Файл уже существует!')
    my_file = open("File.txt", "w+", encoding='utf-8')
    text = [''.join(random.choice(string.ascii_lowercase) for _ in range(randint(10, 20))) for _ in range(1, 30)]
    numb = [randint(1, 1000) for _ in range(1, 30)]
    for t, n in zip(text, numb):
        if int(n) % 2 == 0:
            my_file.write(t + ' ' + str(n) + '\n')
        else:
            my_file.write(t + str(n) + '\n')
    my_file.close()
    return read_file('File.txt')


create_file()
