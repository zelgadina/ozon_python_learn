def is_it_palindrome(string):
	string = ''.join([s for s in string if s.isalpha()]).casefold()
	if (string == string[::-1]) and string:
		return True
	return False

string = input("""
	Введите строку, а я проверю, является ли она палиндромом.
	Можно вводить с пробелами и знаками препинания:
	учитываются только буквы.
	""")

if is_it_palindrome(string):
	print("Это палиндром.")
else:
	print("Это не палиндром.")
