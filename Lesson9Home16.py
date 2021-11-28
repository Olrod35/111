#ДЗ16
"""В программу написанную в прошлом ДЗ добавить новый функционал (не изменяя старого)
username and password получать из командной строки как не обязательные аргументы.
Если оба аргумента переданы и имя и пароль прошли проверку то программа завершает работу не меняя прошлого поведения.
Если не правильное имя или пароль даем 3 попытки как и раньше.
Если передать только имя, то спрашивать только пароль, и наоборот, спрашивать пароль если передать только имя.
Основная идея в том что-бы расширить функционал прошлой программы, а не переписывать!"""

USERS = {
    'Olha': '111111',
    'Talia': '222222'
}

def decorator_for_login(func):
    def wrapper(username, password=USERS.get('Olha')):
        if not check_password(username, password=USERS.get('Olha')):
            return False
        if not auth():
            return False
        return func(username, password=USERS.get('Olha'))
    return wrapper

def auth():
    return True

def check_password(username, password=USERS.get('Olha')):
    if USERS.get(username) == password:
        return True

@decorator_for_login
def login(username, password=USERS.get('Olha')):
    print("Вы в системе!")
    return True

def main():
    i = 3
    while i > 0:
        print("У Вас осталось", i, "попыток")
        username = input("Введите Ваш логин:")
        password = input("Введите Ваш пароль:")
        if login(username, password):
            break
        print("Неправильное имя или пароль")
        i -= 1
        if i == 0:
            print("Попытки истекли")

if __name__ == "__main__":
    main()