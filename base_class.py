from exceptions import ItemNotFound, NotFreeSpace, NotEnoughItem
from storage import Storage


class BaseClass(Storage):
    def __init__(self, capacity=None):
        self._items = {}
        self._capacity = capacity

    def add(self, title, amount):
        free_space = self.get_free_space()

        if free_space < amount:
            raise NotFreeSpace('Нет свободного места')

        if self.is_item(title):
            self.items[title] += amount
        else:
            self.items[title] = amount

    def remove(self, title, amount):
        if not self.is_item(title):
            raise ItemNotFound(f'Товар с именем "{title}" не найден')

        amount_in_store = self.items[title]

        if amount_in_store < amount:
            raise NotEnoughItem(f'Товара меньше ({amount_in_store}) чем нужно ({amount})')

        self.items[title] -= amount

        if self.items[title] == 0:
            del self.items[title]

    def get_free_space(self):
        occupied_space = sum(self.items.values())
        return self.capacity - occupied_space

    def is_item(self, title):
        return title in self.items

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items)

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        self._items = items

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity
