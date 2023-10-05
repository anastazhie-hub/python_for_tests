import send_request
import data

# функция для изменения значения в параметре login, чтобы ее не менять каждый раз
def change_user_body(login):
    # копирование тела запроса user_body из файла data
    current_user_body = data.user_body.copy()
    # изменение значения в параметре login
    current_user_body["login"] = login
    # возвращается новое тело с обновленным значением login
    return current_user_body

# Тест 1. Корректный логин
def test_authorization_correct():
    # В переменную user_body сохраняется логин для запроса со значением “a.ershova@asna.ru”
    user_body = change_user_body("a.ershova@asna.ru")
    # В переменную authorization_response сохраняется результат запроса на авторизацию
    authorization_response = send_request.post_authorization(user_body)

    # Проверяется, что код ответа равен 200
    assert authorization_response.status_code == 200

# Тест 2. Некорректный логин - не дописана буква "u" в конце

def test_authorization_incorrect():
    user_body = change_user_body("a.ershova@asna.r")
    authorization_response = send_request.post_authorization(user_body)

    assert authorization_response.status_code == 400

