# 5. Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться
# в качестве аргумента в дочерний класс. Выполнить перегрузку методов конструктора
# дочернего класса (метод init, в который должна передаваться переменная — скидка),
# и перегрузку метода str дочернего класса. В этом методе должна пересчитываться цена
# и возвращаться результат — цена товара со скидкой. Чтобы все работало корректно, не
# забудьте инициализировать дочерний и родительский классы (вторая и третья строка
# после объявления дочернего класса).

class ItemDiscount:
    __name = 'ElChocoPoco'
    __price = 100
    discount_price = 10

    def new_price(self):
        self.__price = 80
        return self.__price

    def access(self):
        n = self.__name
        p = self.__price
        return n, p


class ItemDiscountReport(ItemDiscount):

    def __init__(self):
        self.discount = self.discount_price

    def __str__(self):
        res = self.new_price() / 100 * self.discount
        return self.new_price() - res

    def get_parent_data(self):
        self.new_price()
        return self.access()


a = ItemDiscountReport()
print(a.get_parent_data())
print(a.__str__())
