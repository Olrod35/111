#ДЗ 15. Декоратор
"""
Написать мини программу, которая будет проверять пароль пользователя и если пароль подходит будет авторизировать пользователя:
Программа должна хранить Имена и Пароли в глобальном словаре
Должна содержать три функции:
check_password() возвращающая -> bool
authenticate() -> bool
login() принимающая минимум 2 аргумента username, password возвращающая -> bool
функция login() должна быть с декоратором в котором будет вся логика проверки check_password и authenticate
у пользователя должно быть 3 попытки после чего программа завершается и выводит сообщение "Попытки истекли!",
при каждой не удачной попытки должно быть сообщение "У вас осталось Н попыток"
Сценарий: пользователь с консоли вводит Имя и Пароль, программа возвращает текст "Вы в системе!" или "Не правильное Имя или Пароль"
"""

from functools import wraps

USERS = {
    'Olha': '111111',
    'Talia': '222222'
}

def login_decorator(func):
    @wraps(func)
    def wrapper(username, password):
        if not check_password(username, password):
            print('Неправильное Имя или Пароль')
            return False
        if not authenticate():
            return False
        return func(username, password)

    return wrapper

def check_password(username: str, password: str) -> bool:
    return USERS.get(username, None) == password

def authenticate() -> bool:
    print('Вы в системе!')
    return True

@login_decorator
def login(_username: str, _password: str) -> bool:
    return True

if __name__ == "__main__":
    i = 3
    while i > 0:
        if login(input('Введите ваш логин:'), input('Введите ваш пароль:')):
            break
        i -= 1
