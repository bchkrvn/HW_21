from base_class import BaseClass
from exceptions import  NotFreeSpace


class Shop(BaseClass):
    def __init__(self):
        super().__init__(capacity=20)

    def add(self, title, amount):
        if not self.is_item(title) and self.get_unique_items_count() >= 5:
            raise NotFreeSpace('В магазине уже есть 5 различных товаров')
        super().add(title, amount)
