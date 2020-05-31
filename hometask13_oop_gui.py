# #дз На прошлом занятии вы написали класс User, игры и несколько тестов к нему.
# Теперь пришла пора обернуть реализацию в реальные интерфейсы - сделайте
# реализацию регистрации/ авторизации на PyQt с формой. На первом экране
# пользователя спрашивают, зареган он или нет - если нет, тогда выдается форма
# регистрации, если да, авторизации (файл с данными пользователя по прежнему
# хранится  в json). После регистрации пользователя предоставлется возможность
# вызывать различные игры, которые вы реализовали. 
# Задание повышенной сложности. На его выполнение дается НЕДЕЛЯ

import sys
import hometask13_oop as oop
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit


def display_window():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setGeometry(300, 100, 530, 400)
    window.setWindowTitle('Game')
    window.setWindowIcon(QIcon('files/favicon.png'))

    hello_message = QLabel(window)
    hello_message.setText(oop.User.greet())
    hello_message.move(50, 20)

    # import pdb; pdb.set_trace()

    b_authorize = QPushButton('Войти', window)
    b_authorize.move(60, 250)
    auth_or_reg = QLabel(window)
    auth_or_reg.setText("или")
    auth_or_reg.move(220, 250)
    b_register = QPushButton('Зарегистрироваться', window)
    b_register.move(320, 250)

    # auth_login_message = QLabel(window)
    # auth_login_message.setText("Логин")
    # auth_login_message.move(50, 170)
    # auth_login = QLineEdit(window)
    # auth_login.move(50, 200)

    # auth_pass_message = QLabel(window)
    # auth_pass_message.setText("Пароль")
    # auth_pass_message.move(50, 250)
    # auth_pass = QLineEdit(window)
    # auth_pass.move(50, 280)

    # reg_login_message = QLabel(window)
    # reg_login_message.setText("Логин")
    # reg_login_message.move(300, 170)
    # reg_login = QLineEdit(window)
    # reg_login.move(300, 200)

    # reg_pass_message = QLabel(window)
    # reg_pass_message.setText("Пароль")
    # reg_pass_message.move(300, 250)
    # reg_pass = QLineEdit(window)
    # reg_pass.move(300, 280)


    window.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    display_window()