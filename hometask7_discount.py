import json
from os import path
from getpass import getuser
from decimal import Decimal

def print_hello_message():
    print(f"""
    Привет, {getuser()}!
    Перед тобой программа применения скидок. Она принимает на вход два
    .json-файла: в одном должны быть перечислены товары, в другом —
    скидки для категорий товаров или отдельных позиций.

    Формат .json-файла с товарами должен соответствовать следующей схеме:
    {{
        "id": {{
            "category": "",
            "price": "",
            "title": ""
        }},
        ...
    }}

    Формат .json-файла со скидками должен соответствовать следующей схеме:
    {{
        "category": {{
            "all": float,
            "category_1": float,
            ...
        }},
        "title": {{
            "": float,
            ...
        }},
        ...
    }}
    """)

def load_data():
    """Принимает пользовательский ввод, пытается найти файл по указанному пути"""
    while True:
        try:
 
            file_path = input("Введите путь к файлу:\n").strip()
            if path.exists(path.normpath(file_path)):

                with open(file_path, 'r') as f:
                    return json.load(f)

            print(f"Файл с именем '{file_path}' не найден, попробуйте снова.")
            continue

        except KeyboardInterrupt:
            exit()
        except Exception:
            print("Упс! Что-то пошло не так.\n :'( Возможно, файл повреждён.")
            continue

def apply_discounts(products, discounts):
    """Для каждого товара из словаря проверяет наличие скидки по категории или по имени.
    Применяет самую большую из найденных скидок и возвращает итоговую цену товара."""
    for product in products:
        try:
            possible_discount = [0.0]
            prod_title = products[product]['title']
            prod_category = products[product]['category']
            prod_price = Decimal(products[product]['price'])

            if prod_title in discounts['title']:
                possible_discount.append(discounts['title'][prod_title])

            if prod_category in discounts['category']:
                possible_discount.append(discounts['category'][prod_category])

            if 'all' in discounts['category']:
                possible_discount.append(discounts['category']['all'])

            price = prod_price * (Decimal('1.0') - Decimal(str(max(possible_discount))))
            price = price.quantize(Decimal("0.01"))
            assert 0 <= price <= prod_price

        except AssertionError:
            print(f"В скидках для продукта {prod_title} содержится ошибка! Вот цена без учёта скидки: {prod_price}")
        except KeyboardInterrupt:
            exit()
        except Exception:
            print("Упс! Что-то пошло не так. Возможно, данные в некорректном формате.")
            exit()
        else:
            print(f"\nПродукт '{prod_title}' с максимальной скидкой {max(possible_discount)} стоит {price}.")


print_hello_message()

print("\nСначала надо загрузить базу данных продуктов.")
products = load_data()
print("\nТеперь надо загрузить базу данных скидок.")
discounts = load_data()

apply_discounts(products, discounts)