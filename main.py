#1
class InvalidUsernameError(Exception):
    def __init__(self, username):
        self.username = username

#InvalidLengthError
#InvalidCharacterError
#DublicateUsrnameErro

def register_user(username):
    if len(username) < 5:
        raise InvalidUsernameError(username)
    else:
        print("Вас зареєстровано!")
#приклад використання
try:
    username = input("ВВедіть ім'я користувача")
    register_user(username)
except InvalidUsernameError as e:
    print(f"Неправильне ім'я користувача {e.username} "
          f'мінімум 5 символів')