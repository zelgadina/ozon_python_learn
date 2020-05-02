import pickle
from re import search
from os import system, path
from random import randrange
from getpass import getuser


def load_names():
    """Возвращает множество кортежей вида '(name, gender)'."""
    names = set()
    if path.exists('names.pickle'):
        with open('names.pickle', 'rb') as f:
            names = pickle.load(f)
    return names

def save_names(names):
    """Сохраняет множество кортежей вида '(name, gender)'."""
    with open('names.pickle', 'wb') as f:
        pickle.dump(names, f)

def hello_message():
    print(f"""
        Привет, {getuser()}!
        Тебе нужно поздравить весь отдел и сказать каждому
        пару хороших слов, а ты едва знаешь коллег? Не беда,
        ведь перед тобой автоматичсекий поздравлятор! Просто
        введи имена и фамилии тех, кого надо поздравить, и
        укажи пол каждого, а я сам добавлю стереотипные
        сексистские банальности вроде "смелый", "сильный",
        "добрая", etc.
        Тебе останется только распечатать их.

        Имена и фамилии будут сохранены в файл 'names.pickle'
        в текущей директории и ты сможешь дополнить их и 
        использовать в следующий раз. Но не удаляй файл
        'epithets.pickle', а то всё сломается.

        В текущей версии программы поддерживается только
        русский язык, а также не подерживается удаление
        имён из списка.

        Когда закончишь перечислять имена, введи ':w' и
        нажми Enter.

        Чтобы выйти из программы до её завершения, нажми Ctrl+C.
        Осторожно: введённые данные могут не сохраниться.
        """)

def unpack_current_names(names):
    print("\tТекущий список сотрудников:")
    for name in names:
        print(f"{name[0]} : {name[1]}")

def validate_name(name):
    if search(r'^[а-яА-ЯЁё \-,]+$', name):
        return name
    return False

def validate_gender(gender):
    if gender in genders:
        return gender
    return False 

def make_set_of_names():
    while True:
        try:

            name = input("Введи имя, фамилию и/или отчество: ").strip()
            if name == ':w':
                break
            if not validate_name(name):
                print("Я поддерживаю только кириллический ввод, давай снова.")
                continue

            gender = input("Укажи пол (m или f): ").strip()
            if gender == ':w':
                break
            if not validate_gender(gender):
                print("Не понимаю, что ты хочешь этим сказать, давай снова.")
                continue

            names.add((name, gender))

        except KeyboardInterrupt:
            exit()

def load_epithets():
    """Возвращает словарь положительных эпитетов для каждого гендера вида
    'gender': ['epithet1', 'epithet2', ...]."""
    try:
        with open('epithets.pickle', 'rb') as f:
            epithets = pickle.load(f)
    except pickle.UnpicklingError:
        epithets = {'f': 'Файл не найден или испорчен.', 'm': 'Файл не найден или испорчен.'}
    return epithets

def generate(names):
    """Вычисляет длину списка эпитетов для каждого гендера,
    чтобы определить верхнюю границу индекса, и генерирует
    строку с именем и случайным эпитетом в корректном роде."""
    lengths = {}
    for gender in epithets.keys():
        lengths[gender] = len(epithets[gender])

    for name, gender in names:
        el_index = randrange(0, lengths[gender])
        epithet = epithets[gender][el_index]
        print(f"{name}, ты {epithet}!")


hello_message()

names = load_names()
epithets = load_epithets()
genders = epithets.keys()

unpack_current_names(names) if names else print("Список имён пуст.")

make_set_of_names()
save_names(names)

generate(names)
