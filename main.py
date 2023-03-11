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


def main():
    user_input = input('Ваш запрос: ')

    for i, word in enumerate(user_input.split()):
        if word.isdigit():
            amount = int(word)
            product = user_input.split()[i + 1]
            break

    request = Request('склад', 'магазин', amount, product)

    if not store.is_item(request.product):
        print(f'Товар "{request.product}" не найден')
        return None

    if shop.get_free_space() < request.amount or shop.get_unique_items_count() > 4:
        print('В магазин недостаточно места, попробуйте что то другое')
        return None

    if store.items[request.product] > request.amount:
        print('Нужное количество есть на складе')
        store.remove(request.product, request.amount)
        print(f'Курьер забрал {request.amount} {request.product} со склада')
        print(f'Курьер везет {request.amount} {request.product} со склада в магазин')
        shop.add(request.product, request.amount)
        print(f'Курьер везет {request.amount} {request.product} со склада в магазин\n')

        print('На складе хранится:')
        for item, amount in store.items.items():
            print(f'{amount} {item}')

        print('\nВ магазине хранится:')
        for item, amount in shop.items.items():
            print(f'{amount} {item}')

    else:
        print('Не хватает на складе, попробуйте заказать меньше')


while True:
    main()
