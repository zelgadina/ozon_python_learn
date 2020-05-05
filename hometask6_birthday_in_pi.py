from getpass import getuser


def hello_message():
    print(f"""
        Привет, {getuser()}!
        Введи свою дату рождения, а я скажу, на какой позиции
        в числе π она находится. Можешь писать год, месяц и день
        в любом порядке, но без разделителей. Например:
        \t11092011

        Чтобы выйти из программы, нажми Ctrl+C.
        """)

def load_pi():
    try:
        with open('pi.txt', 'r') as f:
            return f.read()
    except Exception:
        print("Что-то пошло не так, убедитесь в наличии файла pi.txt.")
        exit()

def get_birth():
    while True:
        try:
            birth = input("Введи дату рождения: ")
            if birth.isdecimal():
                return birth
            print("Введи дату в корректном формате.")
        except KeyboardInterrupt:
            exit()
        except Exception:
            print("Упс! Похоже, что-то пошло не так.")
            continue

def check_in_pi(birth, pi):
    in_pi = pi.find(birth)
    if in_pi != -1:
        print(f"Твоя дата рождения в числе π находится на {in_pi -1} позиции после запятой!")
    else:
        print("Похоже, в ближайших четырёх миллионах знаков такая дата не встречается.")


hello_message()

birth = get_birth()
pi = load_pi()

check_in_pi(birth, pi)

