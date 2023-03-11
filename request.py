class Request:
    def __init__(self, from_, to, amount, product):
        self._from = from_
        self._to = to
        self._amount = amount
        self._product = product

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, product):
        self._product = product
