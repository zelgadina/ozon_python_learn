from os import path
import pickle

def load_data():
	if path.exists('user_dict.pickle'):
		with open('user_dict.pickle', 'rb') as f:
			user_dict = pickle.load(f)
	else:
		with open('user_dict.pickle', 'wb') as f:
			user_dict = pickle.dump(user_dict, f)
	return user_dict


def get_user_dict():
    while True:
        try:

            key = input("Введи слово или словосочетание на английском: ").strip()
            if key == ':w':
                break

            value = input("Введи его перевод на русском: ").strip()
            if value == ':w':
                break

            user_dict[key] = value
#           update_user_dict(user_dict)

        except KeyboardInterrupt:
            exit()


def update_user_dict(addition):
    with open('user_dict.pickle', 'ab') as f:
        pickle.dump(user_dict, f)
    pass

load_data()
get_user_dict()
print(user_dict)