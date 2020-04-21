from random import randint
from getpass import getuser

# 'id уровня сложности': количество попыток
lvls = {'1': 12,
		'2': 9,
		'3': 6}

def hello_message():
	username = getuser()
	print("""
	Привет, {username}!
	Я - игра "Угадай число". Я загадала число от 1 до 100. Попробуй отгадать его!

	Для выхода нажми Ctrl+C.
	""".format(username=username))

def lvl_description():
	print("""
	Выбери уровень сложности (введи номер):
	[1] normal ({lvl_1} попыток)
	[2] nightmare ({lvl_2} попыток)
	[3] hell ({lvl_3} попыток)

	""".format(lvl_1=lvls['1'], lvl_2=lvls['2'], lvl_3=lvls['3']))

def total_attempts_select():
	while True:
		try:
			lvl = input().strip()
			if lvl in lvls:
				return lvls[lvl]
			else:
				print("Некоректное значение, попытайся снова.\n")
				continue
		except KeyboardInterrupt:
			exit()
#		except:
#			print("Что-то пошло не так, попытайся снова.\n")

def num_generator():
	return randint(1, 100)

def check_user_guess(guess):

	if not guess.isdecimal():
		return "is not num"

	if int(guess) != secret_number:
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
		while current_num_attempts > 1:
			guess = input().strip()
			checked_guess = check_user_guess(guess)

			if checked_guess == "is not num":
				print("Это не число, введи нормально!")
				continue
			if checked_guess == "my num is less":
				current_num_attempts -= 1
				print("Моё число меньше. У тебя есть ещё попытки: ", current_num_attempts)
				continue
			if checked_guess == "my num is greater":
				current_num_attempts -= 1
				print("Моё число больше. У тебя есть ещё попытки: ", current_num_attempts)
				continue
			if checked_guess == "guessed":
				print(getuser().upper() + "WINS!\n Потребовалось попыток: ", current_num_attempts)
				end = input("Для выхода нажми Ctrl+C или Enter.")
				exit()
		print("""
			Ты проиграл. Не знаю, утешит ли это тебя эта информация, но 
			согласно теории игр и теории информации пользователю всегда 
			достаточно задать не более чем log2 N вопросов типа "больше n?".
			В твоём случае всё ещё проще, ведь тебе не приходится тратить
			отдельный вопрос для проверки на равенство.
			""")
	except KeyboardInterrupt:
			exit()





#def game_body_input_validator(input):



hello_message()
lvl_description()
total_attempts = total_attempts_select()
secret_number = num_generator()
game_body(total_attempts)

