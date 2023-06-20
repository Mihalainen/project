import request
import data
def new_kit_body():
    change_kit_body = data.kit_body.copy()
    change_kit_body["name"] = "AAAA"
    return change_kit_body

def positive_assert(name):
    # В переменную user_body сохраняется обновленное тело запроса
    kit_body = new_kit_body()
    # В переменную user_response сохраняется результат запроса на создание пользователя:
    user_response = request.create_new_kit(new_kit_body)

    # Проверяется, что код ответа равен 201
    assert user_response.status_code == 201
    # Проверяется, что в ответе есть поле authToken, и оно не пустое
    assert user_response.json()["authToken"] != ""



    # Строка, которая должна быть в ответе
    str_kit = kit_body["name"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

