# #дз На основе предыдущих занятий создайте класс User, у которого реализовано несколько методов и атрибутов:
# атрибут login
# атрибут password
# атрибут uniq_id
# любые другие атрибуты на ваше усмотрение

# валидация должна происходить с помощью методов validate_login  validate_password у отдельного класса Validate

# есть метод greet, который спрашивает User, 
# зарегистрирован он ли в этой системе.
# Если нет,тогда он предлагает зарегистрироваться
# (login и пароль проверяются на регулярных выражениях, а атрибут uniq_id генерируется программно).
# При правильной регистрации создается его профайл в файле login[рандомное число].txt.

# После этого можно войти на ресурс, в котором можно сыграть
# в любую из двух предложенных игр, которые можно найти здесь:
# http://pythonicway.com/component/tags/tag/4-python-games
# (проблемная ситуация в том, что эти игры написаны на Python 2 и их надо переписать)

import json
from os import path
from re import search
from uuid import uuid4
from hashlib import sha256
from getpass import getpass


def print_hello_message():
    print("""
    Привет. Если ты зарегистрирован, то можешь сыграть в любую из предложенных игр.
    Если нет, то сначала зарегистрируйся.

    Логин и пароль должны состоять из латиницы и стандартных символов: '~!@#$%', etc.
    Логин — от 1 до 32 символов, пароль — от 8 до 32.

    Для отказа от участия нажми Ctrl+C.
    """)

def load_data():
    """Подгружает словарь пользователей из файла, если файл пуст или
    не найден, возвращает словарь из одного дефолтного пользователя."""
    try:
        file_path = 'files/oop_users.json'
        if path.exists(path.normpath(file_path)):
            with open(file_path, 'r') as f:
                return json.load(f)
        return {'admin' : ['3b612c75a7b5048a435fb6ec81e52ff92d6d795a8b5a9c17070f6a63c97a53b2',
                           'b79b41c1-31c9-43f2-8e12-b7ffde754404']}
    except Exception:
        print("Упс! Что-то пошло не так :'(")
        exit()

def save_data(users):
    file_path = path.normpath('files/oop_users.json')
    with open(file_path, 'w') as f:
        json.dump(users, f, indent=4)

# def get_login():
#     while True:
#         login = input("Введи логин: ").strip()
#         if validate_login_or_pass(login):
#             if login not in users:
#                 return login

#             print("Ошибка! Такой логин уже существует.")
#             continue

#         print("Ошибка! Проверь логин на соответствие правилам.")
#         continue

# def get_password():
#     """Валидирует пароль и возвращает его в виде sha256."""
#     while True:
#         password = getpass("Введи пароль: ").strip()
#         if validate_login_or_pass(password):
#             password_conf = getpass("Введи пароль повторно: ").strip()
#             if password_conf == password:
#                 return sha256(password.encode('utf-8')).hexdigest()

#             print("Пароли не совпадают!")
#             continue

#         print("Ошибка! Проверь пароль на соответствие правилам.")
#         continue

class User(object):
    """I hate fucking oop."""
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.uniq_id = None
    def login(self):
        print(self.user_name, self.password)

class Validate(object):

    @staticmethod
    def validate_login(user_name):
        if search(r'^[!-~]{1,32}$', user_name):
            return user_name
        return False

    @staticmethod
    def validate_password(password):
        if search(r'^[!-~]{8,32}$', password):
            return password
        return False



print_hello_message()
users = load_data()


USER_LOGIN = 'abyr'
USER_PASSWORD = '123'

user = User(USER_LOGIN, USER_PASSWORD)
user.login()

# Validate.validate_login(user.user_name)
# Validate.validate_password(user.password)
        
        