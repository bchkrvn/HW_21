class ItemNotFound(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'ItemNotFound: {self.message}'
        else:
            return f'ItemNotFound'


class NotFreeSpace(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'NotFreeSpace: {self.message}'
        else:
            return f'NotFreeSpace'
