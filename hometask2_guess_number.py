from random import randint
from getpass import getuser

# 'id уровня сложности': количество попыток
lvls = {'1': 12,
        '2': 9,
        '3': 6}

def hello_message():
    username = getuser()
    print(f"""
    Привет, {username}!
    Я - игра "Угадай число". Я загадала натуральное число от 1 до 100. Попробуй отгадать его!\n
    Для выхода нажми Ctrl+C.
    """)

def lvl_description():
    print(f"""
    Выбери уровень сложности (введи номер):
    [1] normal ({lvls['1']} попыток)
    [2] nightmare ({lvls['2']} попыток)
    [3] hell ({lvls['3']} попыток)
    """)

def total_attempts_select():
    while True:
        try:
            lvl = input().strip()
            if lvl in lvls:
                return lvls[lvl]

            print("Некоректное значение, попытайся снова.\n")
            continue

        except KeyboardInterrupt:
            exit()

def check_user_guess(guess):
    if not guess.isdecimal():
        return "is not num"
    if int(guess) > secret_number:
        return "my num is less"
    if int(guess) < secret_number:
        return "my num is greater"
    return "guessed"

def game_body(total_attempts):
    print("Всего попыток: ", total_attempts)
    print("Какое число я загадала?")
    current_num_attempts = total_attempts
    try:
        while current_num_attempts > 0:

            guess = input().strip()
            checked_guess = check_user_guess(guess)

            if checked_guess == "is not num":
                print("Это не натуральное число от 1 до 100, введи нормально!")
                continue
            if checked_guess == "my num is less":
                current_num_attempts -= 1
                print(f"Моё число меньше. Осталось попыток: {current_num_attempts}/{total_attempts}")
                continue
            if checked_guess == "my num is greater":
                current_num_attempts -= 1
                print(f"Моё число больше. Осталось попыток: {current_num_attempts}/{total_attempts}")
                continue
            if checked_guess == "guessed":
                print(f"{getuser().upper()} WINS!\n Потребовалось попыток: {total_attempts - current_num_attempts}\n")
                break

            print("""
            Ты проиграл. Не знаю, утешит ли это тебя это знание, но 
            согласно теории игр и теории информации пользователю всегда 
            достаточно задать не более чем log2 N вопросов типа "больше n?".
            В твоём случае всё ещё проще, ведь тебе не приходится тратить
            отдельный вопрос для проверки на равенство.
            """)
    except KeyboardInterrupt:
            exit()


hello_message()
lvl_description()
total_attempts = total_attempts_select()
secret_number = randint(1, 100)
game_body(total_attempts)
end = input("Для выхода нажми Ctrl+C или Enter.")
exit()
