from exceptions import ItemNotFound, NotEnoughItem, NotFreeSpace
from request import Request
from shop import Shop
from store import Store

shop = Shop()
store = Store()

shop.add('печеньки', 5)
shop.add('собачки', 2)

store.add('печеньки', 6)
store.add('собачки', 4)
store.add('коробки', 5)
store.add('носки', 3)
store.add('шапки', 5)
store.add('хлеб', 10)

places = {
    'магазин': shop,
    'магазина': shop,
    'склад': store,
    'склада': store,
}


def main(shop, store, places):
    while True:
        print('\nНапишете запрос в формате: "Доставить <кол-во> <товар> из <место> в <место>"')
        user_input = input('Ваш запрос: ')
        request = Request(user_input)

        try:
            place_from = places[request.place_from]
            place_to = places[request.place_to]

        except KeyError:
            print('Доставить и отправить товар можно из магазина или склада')
            continue

        try:
            place_from.remove(request.product, request.amount)

        except ItemNotFound as e:
            print(e)
            continue
        except NotEnoughItem as e:
            print(e)
            continue

        try:
            place_to.add(request.product, request.amount)

        except NotFreeSpace as e:
            print(e)
            place_from.add(request.product, request.amount)
            continue

        print_info(request, shop, store)


def print_info(request, shop, store):
    print('\nНужное количество есть на складе')
    print(f'Курьер забрал {request.amount} {request.product} из {request.place_from}')
    print(f'Курьер везет {request.amount} {request.product} из {request.place_from} в {request.place_to}')
    print(f'Курьер привез {request.amount} {request.product} из {request.place_from} в {request.place_to}')

    print('На складе хранится:')
    for item, amount in store.items.items():
        print(f'{amount} {item}')

    print('\nВ магазине хранится:')
    for item, amount in shop.items.items():
        print(f'{amount} {item}')


main(shop, store, places)
