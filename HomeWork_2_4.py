# 4. Реализовать возможность переустановки значения цены товара.
# Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены.
# Следует проверить это, вызвав соответствующий метод родительского класса и функцию
# дочернего (функция, отвечающая за отображение информации о товаре в одной строке).

class ItemDiscount:
    __name = 'ElChocoPoco'
    __price = 100

    def new_price(self):
        self.__price = 200
        return self.__price

    def access(self):
        n = self.__name
        p = self.__price
        return n, p


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        self.new_price()
        return self.access()


a = ItemDiscountReport()
print(a.get_parent_data())
