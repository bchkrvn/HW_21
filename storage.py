from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def add(self, title, amount):
        pass

    @abstractmethod
    def remove(self, title, amount):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass

    @abstractmethod
    def is_item(self, title):
        pass
