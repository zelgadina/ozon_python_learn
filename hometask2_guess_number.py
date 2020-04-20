from random import randint
from getpass import getuser

NORMAL = 12
NIGHTMARE = 9
HELL = 6

lvls = {NORMAL, NIGHTMARE, HELL}

def hello():
	username = getuser()
	print("""
	Привет, {username}!
	Я - игра "Угадай число". Я загадала число от 1 до 100. Попробуй отгадать его!

	Для выхода нажми Ctrl+C.

	""".format(username=username))

def lvl_description():
	print("""
	Выбери уровень сложности (введи номер):
	[1] normal ({normal} попыток)
	[2] nightmare ({nightmare} попыток)
	[3] hell ({hell} попыток)

	""".format(normal=NORMAL, nightmare=NIGHTMARE, hell=HELL))

def lvl_select():
	while True:
		try:
			lvl_description()
			lvl = input()
			if lvl == NORMAL:
				return NORMAL
			if lvl == NIGHTMARE:
				return NIGHTMARE
			if lvl == HELL:
				return HELL
			else:
				print("Некоректное значение, попытайся снова.\n")
				continue
		except KeyboardInterrupt:
			exit()
		except:
			print("Что-то пошло не так, попытайся снова.\n")

def lvl_validator(lvl_user_input) -> bool:
	if lvl_user_input in lvls:
		return True
	return False

