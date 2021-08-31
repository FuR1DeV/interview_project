# 2. Написать программу, которая запрашивает у пользователя ввод числа.
# На введенное число она отвечает сообщением, целое оно или дробное.
# Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
# Если они совпадают, программа должна возвращать значение True, иначе False.

a = input('Введите целое или дробное число ')


def reply_num(num):
    try:
        if int(num):
            return f"{num} введенное вами число является целым!"

    except ValueError:
        print(f"{num} введенное вами число является дробным!")
        c = list(str(num))
        numb = []
        res_left = 0
        for i in c:
            if i.isnumeric():
                numb.append(int(i))
            else:
                res_left = int("".join(list(map(str, numb))))
                numb.clear()
        res_right = int("".join(list(map(str, numb))))
        return True if res_right == res_left else False


print(reply_num(a))
