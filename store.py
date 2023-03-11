from storage import Storage
from exceptions import ItemNotFound


class Store(Storage):
    def __init__(self):
        super().__init__(capacity=100)

    def add(self, title, amount):
        free_space = self.get_free_space()

        if free_space < amount:
            amount = free_space

        if self.is_item(title):
            self.items[title] += amount
        else:
            self.items[title] = amount

    def remove(self, title, amount):
        if self.is_item(title):
            amount_in_store = self.items[title]

            if amount_in_store < amount:
                amount = amount_in_store

            self.items[title] -= amount
        else:
            raise ItemNotFound(f'Товар с именем "{title}" не найден')

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

