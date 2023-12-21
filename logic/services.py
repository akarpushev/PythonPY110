import json
import os
from store.models import DATABASE

def filtering_category(database: dict,
                       category_key: [int, str] = None,
                       ordering_key: [None, str] = None,
                       reverse: bool = False):
    if category_key is not None:
        data = list(DATABASE.values())
        result = [dict for dict in data if dict['category'] == category_key]
    else:
        result = list(database) #  TODO Трансформируйте database в список словарей
    if ordering_key is not None:
        result = sorted(result, key=lambda x: x[ordering_key], reverse=reverse)
    return result

# if __name__ == "__main__":
#     from store.models import DATABASE
#
#     test = [
#         {'name': 'Клубника', 'discount': None, 'price_before': 500.0,
#          'price_after': 500.0,
#          'description': 'Сладкая и ароматная клубника, полная витаминов, чтобы сделать ваш день ярче.',
#          'rating': 5.0, 'review': 200, 'sold_value': 700,
#          'weight_in_stock': 400,
#          'category': 'Фрукты', 'id': 2, 'url': 'store/images/product-2.jpg',
#          'html': 'strawberry'},
#
#         {'name': 'Яблоки', 'discount': None, 'price_before': 130.0,
#          'price_after': 130.0,
#          'description': 'Сочные и сладкие яблоки - идеальная закуска для здорового перекуса.',
#          'rating': 4.7, 'review': 30, 'sold_value': 70, 'weight_in_stock': 200,
#          'category': 'Фрукты', 'id': 10, 'url': 'store/images/product-10.jpg',
#          'html': 'apple'}
#     ]
#
#     print(filtering_category(DATABASE, 'Фрукты', 'price_after', True) == test)  # True

def view_in_cart() -> dict:
    if os.path.exists('cart.json'):  # Если файл существует
        with open('cart.json', encoding='utf-8') as f:
            return json.load(f)
    cart = {'products': {}}  # Создаём пустую корзину
    with open('cart.json', mode='x', encoding='utf-8') as f:   # Создаём файл и записываем туда пустую корзину
        json.dump(cart, f)
    return cart

def add_to_cart(id_product: str):
    cart = view_in_cart()
    if id_product in cart["products"]:
        if id_product in DATABASE.keys():
            cart['products'][id_product] += 1
    else:
        if id_product in DATABASE.keys():
            cart['products'][id_product] = 1
    with open('cart.json', mode='w', encoding='utf-8') as f:
         json.dump(cart, f)
    return True

def remove_from_cart(id_product: str) -> bool:
    cart = view_in_cart()
    if id_product in cart["products"]:
        del cart['products'][id_product]
        with open('cart.json', mode='w', encoding='utf-8') as f:
            json.dump(cart, f)
    else:
        return False
    return True
#
if __name__ == "__main__":
    # Проверка работоспособности функций view_in_cart, add_to_cart, remove_from_cart
    # Для совпадения выходных значений перед запуском скрипта удаляйте появляющийся файл 'cart.json' в папке
    print(view_in_cart())  # {'products': {}}
    print(add_to_cart('1'))  # True
    print(add_to_cart('0'))  # False
    print(add_to_cart('1'))  # True
    print(add_to_cart('2'))  # True
    print(view_in_cart())  # {'products': {'1': 2, '2': 1}}
    print(remove_from_cart('0'))  # False
    print(remove_from_cart('1'))  # True
    print(view_in_cart())  # {'products': {'2': 1}}

    # Предыдущий код, что был для проверки filtering_category закомментируйте