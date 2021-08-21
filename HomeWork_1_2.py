# 2. Дополнить следующую функцию недостающим кодом:
"""
Функция принимает имя каталога и распечатывает его содержимое
в виде «путь и имя файла», а также любые другие
файлы во вложенных каталогах.

Эта функция подобна os.walk. Использовать функцию os.walk
нельзя. Данная задача показывает ваше умение работать с
вложенными структурами.
"""


def print_directory_contents(sPath):
    for address, dirs, files in sPath:
        for file in files:
            print(address + '/' + file)


folder = [('work', ['cooking'], ['photo.png', 'file.txt']),
          ('test/cooking', ['soup', 'cake'], ['recipes.txt']),
          ('test/cooking/soup', [], ['soup.txt']),
          ('test/cooking/cake', [], ['cake.txt'])]
print_directory_contents(folder)