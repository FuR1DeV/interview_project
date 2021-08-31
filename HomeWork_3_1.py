# 1. Написать программу, которая будет содержать функцию для получения имени файла
# из полного пути до него. При вызове функции в качестве аргумента должно передаваться
# имя файла с расширением. В функции необходимо реализовать поиск полного пути по имени
# файла, а затем «выделение» из этого пути имени файла (без расширения).

import os
from os import path


def find(name):
    root_to_file = 'c:'
    for root, dirs, files in os.walk(root_to_file):
        if name in files:
            print(os.path.join(root, name))
            return path.splitext(path.basename(str(os.path.join(root, name))))[0]


print(find('File.txt'))
