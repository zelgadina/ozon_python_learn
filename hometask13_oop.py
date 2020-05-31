import json
from re import search
from uuid import uuid4
from os import path, mkdir
from getpass import getpass
from hashlib import sha256, md5


def make_dir():
    if not path.isdir('oop_users'):
        mkdir('oop_users')

def save_data(user):
    new_user = ({user.login: [user.password, str(user.uuid)]})
    file_path = path.normpath(f'oop_users/{user.login}_{md5(user.login.encode()).hexdigest()}.json')
    with open(file_path, 'w') as f:
        json.dump(new_user, f, indent=4)

def check_user_registration():
    while True:
        try:
            answer = input("Ты уже зарегистрирован? (y/n)").strip().casefold()
            if answer == ('y' or 'yes'):
                authorize()
                break
            if answer == ('n' or 'no'):
                print("Тогда сначала зарегистрируйся.")
                break
            print("Введи 'y' или 'n'.")
            continue
        except KeyboardInterrupt:
            exit()

def authorize():
    try:
        while True:
            login = input("Введи логин: ").strip()
            file_path = f'oop_users/{login}_{md5(login.encode()).hexdigest()}.json'
            if path.exists(path.normpath(file_path)):
                break
            else:
                print("Неверный логин!")
                continue
        with open(file_path, 'r') as f:
            user = json.load(f)
        while True:
            password = getpass("Введи пароль: ").strip()
            import pdb; pdb.set_trace()
            if sha256(password.encode('utf-8')).hexdigest() == user[login][0]:
                print("Авторизация прошла успешно!")
                import snake
                exit()
            else:
                print("Неверный пароль!")
                continue
    except KeyboardInterrupt:
        exit()

class User(object):
    def __init__(self, login, password, uuid):
        self.login = login
        self.password = password
        self.uuid = uuid

    @staticmethod
    def greet():
        return """
Привет. Если ты зарегистрирован, то можешь сыграть в змейку.
Если нет, то сначала зарегистрируйся.

Логин и пароль должны состоять из латиницы и стандартных символов:
'~!@#$%', etc.
Логин — от 1 до 32 символов, пароль — от 8 до 32.
    """

    @staticmethod
    def get_login():
        while True:
            try:
                login = input("Введи логин: ").strip()
                if Validate.validate_login(login):
                    file_path = f'oop_users/{login}_{md5(login.encode()).hexdigest()}.json'
                    if not path.exists(path.normpath(file_path)):
                        return login

                    print("Ошибка! Такой логин уже существует.")
                    continue

                print("Ошибка! Проверь логин на соответствие правилам.")
                continue
            except KeyboardInterrupt:
                exit()

    @staticmethod
    def get_password():
        """Валидирует пароль и возвращает его в виде sha256."""
        while True:
            try:
                password = getpass("Введи пароль: ").strip()
                if Validate.validate_password(password):
                    password_conf = getpass("Введи пароль повторно: ").strip()
                    if password_conf == password:
                        return sha256(password.encode('utf-8')).hexdigest()

                    print("Пароли не совпадают!")
                    continue

                print("Ошибка! Проверь пароль на соответствие правилам.")
                continue
            except KeyboardInterrupt:
                exit()

class Validate(object):

    @staticmethod
    def validate_login(user_name):
        if search(r'^[!-~]{1,32}$', user_name):
            return True
        return False

    @staticmethod
    def validate_password(password):
        if search(r'^[!-~]{8,32}$', password):
            return True
        return False

if __name__ == "__main__":
    make_dir()

    User.greet()

    check_user_registration()

    login = User.get_login()
    password = User.get_password()
    uuid = uuid4()

    user = User(login, password, uuid)

    save_data(user)

    print("""
    Отлично, теперь давай сыграем.
    """)

    import snake
    exit()