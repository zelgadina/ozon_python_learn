# Программа позволяет пользователю свой англо-русский словарь,
# а затем проверить свои знания. Словарь сохраняется в файл
# user_dict.pickle и может быть обновлён при запуске программы.


import pickle
from os import system, path
from re import search
from getpass import getuser


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

    Чтобы обнулить словарь, удали файл 'user_dict.pickle' (он расположен в этом же каталоге).
    Чтобы исправить перевод слова, введи его заново на английском и затем на русском.

    Внимание: при вводе учитывается регистр.

    Чтобы завершить ввод слов и перейти к проверке свои знаний, введи ':w' и нажми Enter.

    Чтобы выйти из программы до её завершения, нажми Ctrl+C.
    Осторожно: введённые данные могут не сохраниться.
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
        Если ты ошибёшься трижды, ты проиграешь.
        """)


def examenation(user_dict):
    global attempts
    pre_examenation()
    errors = 0
    len_dict = len(user_dict)
    try:
        for i in range(attempts):
            if errors < 3 and user_dict:
                attempt = user_dict.popitem()
                value = input(attempt[0] + ': ').strip()

                if not user_dict_validator_value(value):
                    print("Это не слово или словосочетание на русском.")
                    attempts += 1       # Чтобы ошибка ввода не считалась за неудачную попытку
                    user_dict[attempt[0]] = attempt[1]
                    continue

                if value != attempt[1]:
                    errors += 1
                    print(f"Ошибка №{errors}. Правильный ответ: {attempt[1]}")

                else:
                    print("Правильный ответ!")

        if errors < 3 and errors < len_dict:
            print("Похоже, ты хорошо справляешься, мама бы тобой гордилась.")
        else:
            print("Сегодня не твой день, повтори материал и возвращайся.")   

    except KeyboardInterrupt:
            exit()


attempts = 10

user_dict = load_data()     # Загрузка пользовательского словаря или его создание.

hello_message()

get_user_dict()             # Получение от пользователя новых слов.

save_data(user_dict)

examenation(user_dict)