from datetime import date
from getpass import getuser

def hello():
	username = getuser()
	print("""
	Привет, {username}.
	Эта программа вычисляет, сколько лет тебе будет в заданном году в будущем на основании твоего текущего возраста.
	Для выхода нажми Ctrl+C.

	""".format(username=username))

def current_age_validator(user_input_age_string):
	if not user_input_age_string.isdecimal():
		return False
	if int(user_input_age_string) < 0:
		return False
	
	return True

def get_current_age():
	while True:
		try:
			user_input_age = input("Введи свой возраст (количество полных лет): ").strip()
			if current_age_validator(user_input_age):
				return int(user_input_age)
			else:
				print("Некоректное значение, попытайся снова.\n")
				continue
		except KeyboardInterrupt:
			exit()
		except:
			print("Что-то пошло не так, попытайся снова.\n")

def current_year():
	current_year = date.today().year
	return current_year

def future_year_validator(user_input_year_string):
	if not user_input_year_string.isdecimal():
		is_not_year = "Это не год, введи нормально.\n"
		return False, is_not_year
	if int(user_input_year_string) <= current_year():
		is_not_future = "Это не будущее, мы занимаемся только предсказаниями.\n"
		return False, is_not_future
	
	return True, None
	
def get_future_year():
	while True:
		try:
			user_input_year = input("Введи год, твой возраст в котором тебе интересен: ").strip()
			if future_year_validator(user_input_year)[0]:
				return int(user_input_year)
			else:
				print(future_year_validator(user_input_year)[1]) # Сообщение о конкретной ошибке ввода
		except KeyboardInterrupt:
			exit()
		except:
			print("Что-то пошло не так, попытайся снова.\n")

def calc_future_age(current_age, future_year):
	difference_of_years = future_year - current_year()
	future_age = current_age + difference_of_years
	return future_age

def print_future_age(future_age, future_year):
	print("Твой возраст в {year} году: {age}.".format(year=future_year, age=future_age))


hello()
current_age = get_current_age()
future_year = get_future_year()
future_age = calc_future_age(current_age=current_age, future_year=future_year)
print_future_age(future_age=future_age, future_year=future_year)
