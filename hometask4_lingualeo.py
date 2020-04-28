import pickle
from os import system
from re import search
from random import randint
from getpass import getuser

user_dict = {}
attempts = 10

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
            update_user_dict(user_dict)

            print(user_dict)

        except KeyboardInterrupt:
            exit()
    print(user_dict)
    test = input(attempts)

def update_user_dict(addition):
    with open('user_dict.pickle', 'ab') as f:
        pickle.dump(user_dict, f)
    pass

def open_user_dict():
    with open('user_dict.pickle', 'rb') as f:
        fresh_user_dict = pickle.load(f)
    print(fresh_user_dict)
    return fresh_user_dict

def pre_examenation():
    try:
        system('clear')
    except:
        system('cls')
    print("""
        Теперь переходим к проверке.
        Я буду выводить слово или словосочетание на английском,
        а ты вводи его перевод на русском.
        """)
    pass

def examenation():
    global attempts
#    pre_examenation()
    user_dict = open_user_dict()
    print(user_dict)
    errors = 0
    for i in range(attempts):
        try:
            value = input(user_dict['hui']).strip()

            if not user_dict_validator_value(value):
                print("Это не слово или словосочетание на русском.")
                attempts += 1       # Чтобы ошибка ввода не считалась за неудачную попытку
                continue

            if value != user_dict[key]:
                print(f"Ошибка. Правильный ответ: {user_dict[key]}")

            else:
                print("Правильный ответ!")

        except KeyboardInterrupt:
            exit()

    print(user_dict)
    test = input("")






#hello_message()
print(get_user_dict())
print(user_dict)
print(attempts, 1488)
examenation()


#print("Сейчас у нас будет проверка, больше 3 ошибок нельзя")

#errors = 0
#bonus = 0

#for key in slovar.keys():
#    print("Ввeдите перевод слова", key, ": ")
#    answer = input(": ").strip().lower()
#    if slovar[key] == answer:
#        bonus += 1
#        print("Ваш счет составляет", bonus)
#    elif errors > 3:
#        print("game over")
#        break
#    else:
#        errors +=1
#        print(slovar[key], "- правильный ответ")