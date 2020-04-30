# Программа позволяет пользователю свой англо-русский словарь,
# а затем проверить свои знания. Словарь сохраняется в файл
# user_dict.pickle и может быть обновлён при запуске программы.


import pickle
from os import system, path
from re import search
from random import randint
from getpass import getuser


attempts = 10


def load_data():
    user_dict = {}
    if path.exists('user_dict.pickle'):
        with open('user_dict.pickle', 'rb') as f:
            user_dict = pickle.load(f)
    return user_dict


def save_data(user_dict):
    with open('user_dict.pickle', 'wb') as f:
        pickle.dump(user_dict, f)


def hello_message():
    try:
        system('clear')
    except:
        system('cls')
    print(f"""
    Привет, {getuser()}! Сейчас ты сможешь написать свой словарик и проверить свои знания.

    Каждый раз, когда ты заходишь в программу повторно, ты можешь дополнять свой словарик
    новыми парами слов или словосочетаний, а затем проверять свои знания всего словаря:
    тебе будет предложено правильно перевести несколько ({attempts}) случайных слов.

    Чтобы обнулить словарь, удали файл 'user_dict' (он расположен в этом же каталоге).
    Чтобы исправить перевод слова, введи его заново на английском и затем на русском.

    Внимание: при вводе учитывается регистр.

    Чтобы завершить ввод слов и перейти к проверке свои знаний, введи ':w' и нажми Enter.

    Чтобы выйти из программы, нажми Ctrl+C. Осторожно: введённые данные могут не сохраниться.
    """)


def user_dict_validator_key(key):
    if search(r'^[a-zA-Z -\']+$', key):
        return key
    return False


def user_dict_validator_value(value):
    if search(r'^[а-яА-Яё -,]+$', value):
        return value
    return False


def get_user_dict():
    while True:
        try:

            key = input("Введи слово или словосочетание на английском: ").strip()
            if key == ':w':
                break 
            if not user_dict_validator_key(key):
                print("Это не слово или словоочетание на английском.")
                continue

            value = input("Введи его перевод на русском: ").strip()
            if value == ':w':
                break
            if not user_dict_validator_value(value):
                print("Это не слово или словосочетание на русском.")
                continue

            user_dict[key] = value

        except KeyboardInterrupt:
            exit()


def pre_examenation():
    try:
        system('clear')
    except:
        system('cls')
    print("""
        Теперь переходим к проверке.
        Я буду выводить слово или словосочетание на английском,
        а ты вводи его перевод на русском.
        Если ты ошибёшься более трёх раз, ты проиграешь.
        """)
    pass


def examenation(user_dict):
    global attempts
    pre_examenation()
    print("get_user_dict pass, user_dict = ", user_dict)
    errors = 0
    try:
        for i in range(attempts):
            if errors < 3 and user_dict:
                attempt = user_dict.popitem()
                value = input(attempt[0] + ': ').strip()

                if not user_dict_validator_value(value):
                    print("Это не слово или словосочетание на русском.")
                    attempts += 1       # Чтобы ошибка ввода не считалась за неудачную попытку
                    continue

                if value != attempt[1]:
                    errors += 1
                    print(f"Ошибка №{errors}. Правильный ответ: {attempt[1]}")

                else:
                    print("Правильный ответ!")

        if errors == 3:
            print("Сегодня не твой день, повтори материал и возвращайся.")
        else: 
            print("Похоже, ты хорошо справляешься, мама бы тобой гордилась.")

    except KeyboardInterrupt:
            exit()



user_dict = load_data()
hello_message()
get_user_dict()
print("after get_user_dict ", user_dict)
save_data(user_dict)
examenation(user_dict)

