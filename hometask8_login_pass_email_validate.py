# Сделать программу, которая собирает данные пользователей - 
# в нем можно ввести логин пользователя и почту, и если 
# с помощью проверки регулярными выражениями валидны, тогда 
# они записываются в файл. В другом случае, пользователю говорится, 
# что у него ошибка в введеных данных и нужно заново ввести данные.

import json
from os import path
from re import search
from validate_email import validate_email


def print_hello_message():
    print("""
    Добро пожаловать на анимешный форум для девочек, Анон. Снова.
    Мы объявляем набор модераторов. Чтобы принять участие, тебе нужно
    зарегистрироваться. Для регистрации используй любой свой фейковый ящик,
    если он работает. Мы гарантируем, что никакие данные не будут переданы
    третьим лицам.

    Логин и пароль должны состоять из латиницы и стандартных символов: '~!@#$%', etc.
    Длина — от 8 до 32 символов.

    Для отказа от участия нажми Ctrl+C.
    """)
    ...

def load_data():
    """Подгружает словарь пользователей из файла, если файл пуст или
    не найден, возвращает словарь из одного дефолтного пользователя."""
    try:
        file_path = 'files/users.json'
        if path.exists(path.normpath(file_path)):
            with open(file_path, 'r') as f:
                return json.load(f)
        return {'admin123' : ['123', 'admin@test.com']}
    except Exception:
        print("Упс! Что-то пошло не так :'(")
        exit()

def validate_login_or_pass(value):
    if search(r'^[!-~]{8,32}$', value):
        return value
    return False

def get_login():
    while True:
        login = input("Введи логин: ").strip()
        if validate_login_or_pass(login):
            if login not in users:
                return login
            print("Ошибка! Такой логин уже существует.")
            continue
        else:
            print("Ошибка! Проверь логин на соответствие правилам.")
            continue

def get_password():
    while True:
        password = input("Введи пароль: ").strip()
        if validate_login_or_pass(password):
            password_conf = input("Введи пароль повторно: ").strip()
            if password_conf == password:
                return password
            else:
                print("Пароли не совпадают!")
                continue
        else:
            print("Ошибка! Проверь пароль на соответствие правилам.")
            continue

def validate_email_():
    """Валидирует email и проверяет, что в users нет зарегистрированных
    пользователей с таким же."""
    while True:
        try:
            email = input("Введи email: ").strip()
            if not validate_email(email):
                print("Похоже, такого email не существует, введи реальный.")
                continue

            for user in users:
                assert email != users[user][1]
                continue

            return email

        except AssertionError:
            print("Ошибка! Этот email уже занят.")
            continue

def create_user():
    try:
        login = get_login()
        password = get_password()
        email = validate_email_()
        users[login] = [password, email]

    except KeyboardInterrupt:
        exit()

def save_data(users):
    file_path = path.normpath('files/users.json')
    with open(file_path, 'w') as f:
        json.dump(users, f, indent=4)


print_hello_message()
users = load_data()
new_user = create_user()
save_data(users)