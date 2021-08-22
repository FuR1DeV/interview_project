# 3. Усовершенствовать родительский класс таким образом,
# чтобы получить доступ к защищенным переменным.
# Результат выполнения заданий 1 и 2 должен быть идентичным.

class ItemDiscount:
    __name = 'ElChocoPoco'
    __price = 100

    def access(self):
        n = self.__name
        p = self.__price
        return n, p


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return self.access()


a = ItemDiscountReport()
print(a.get_parent_data())
