# 6. Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс
# ItemDiscountReport на два класса. Инициализировать классы необязательно.
# Внутри каждого поместить функцию get_info, которая в первом классе будет
# отвечать за вывод названия товара, а вторая — его цены. Далее реализовать выполнение
# каждой из функции тремя способами.

class ItemDiscount:
    __name = 'ElChocoPoco'
    __price = 100

    def access(self):
        n = self.__name
        p = self.__price
        return n, p

# Реализация разными способами
class ItemDiscountReportName(ItemDiscount):

    def __str__(self):
        return f"Название {self.access()[0]}"

    def get_info(self):
        return f"Название {self.access()[0]}"


class ItemDiscountReportPrice(ItemDiscount):

    def __str__(self):
        return f"Цена {self.access()[1]}"

    def get_info(self):
        return f"Цена {self.access()[1]}"


a = ItemDiscountReportName()
b = ItemDiscountReportPrice()
c = [a, b]

for items in c:
    print(items.get_info())

for items in c:
    print(items)
