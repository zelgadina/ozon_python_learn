from random import randint
from getpass import getuser

lvls = {'1': 12,
		'2': 9,
		'3': 6}

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
	[1] normal ({lvl_1} попыток)
	[2] nightmare ({lvl_2} попыток)
	[3] hell ({lvl_3} попыток)

	""".format(lvl_1=lvls['1'], lvl_2=lvls['2'], lvl_3=lvls['3']))

def lvl_select():
	while True:
		try:
			lvl = input().strip()
			if lvl in lvls:
				return lvl
			else:
				print("Некоректное значение, попытайся снова.\n")
				continue
		except KeyboardInterrupt:
			exit()
#		except:
#			print("Что-то пошло не так, попытайся снова.\n")


hello()
lvl_description()
lvl_select()
