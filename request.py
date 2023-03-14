class Request:
    def __init__(self, request: str):
        split_request = request.split()
        self._amount = int(split_request[1])
        self._product = split_request[2]
        self._place_from = split_request[4]
        self._place_to = split_request[6]

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

    @property
    def place_from(self):
        return self._place_from

    @place_from.setter
    def place_from(self, place_from):
        self._place_from = place_from

    @property
    def place_to(self):
        return self._place_to

    @place_to.setter
    def place_to(self, place_to):
        self._place_to = place_to
