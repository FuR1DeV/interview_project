# 2. Инкапсулировать оба параметра (название и цену) товара родительского класса.
# Убедиться, что при сохранении текущей логики работы программы будет
# сгенерирована ошибка выполнения.

class ItemDiscount:
    __name = 'ElChocoPoco'
    __price = 100


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return self.__name, self.__price


a = ItemDiscountReport()
print(a.get_parent_data())
