import requests
import pytest

global url
url = "https://petstore.swagger.io/v2/user"


# передача симолов в поле ID
def test_post_create_user_string_id():
    request_create_user_string_id = {'id': '777999a', 'username': "Antuanetta", 'firstName': "Antuanetta",
                                     'lastName': "Ioganna", 'email': "ok@ok.ru", 'password': '123456',
                                     'phone': "+7-906-332-33-33", 'userStatus': 0}
    response_create_user_string_id = requests.post(url, json=request_create_user_string_id)
    # ожидаю, что пользователя создать нельзя и вернулась ошибка 500
    assert response_create_user_string_id.status_code == 500


# создание пользователя с отрицательным ID
def test_post_create_user_negative_id():
    request_create_user_negative_id = {'id': -10, 'username': "Antuanetta", 'firstName': "Antuanetta",
                                       'lastName': "Ioganna", 'email': "ok@ok.ru", 'password': '123456',
                                       'phone': "+7-906-332-33-33", 'userStatus': 0}
    response_create_user_negative_id = requests.post(url, json=request_create_user_negative_id)
    # ожидаю, что пользователь не создан (статус код == 500)
    assert response_create_user_negative_id.status_code == 500

# создание пользователя с пустым ID. Данный тест не запускается из-за проверок pycharm
#def test_post_create_user_empty_id():
#    request = {'id': , 'username': "Antuanetta", 'firstName': "Antuanetta", 'lastName': "Ioganna",
#               'email': "ok@ok.ru", 'password': '123456', 'phone': "+7-906-332-33-33", 'userStatus': 0}
#    response = requests.post(url, json=request)
#    # ожидаю, что пользователь не создан (статус код == 400)
#    assert response.status_code == 400


# создание пользователя с набором без ID
def test_post_create_user_without_id():
    request_create_user_without_id = {'username': "Antuanetta", 'firstName': "Antuanetta", 'lastName': "Ioganna",
               'email': "ok@ok.ru", 'password': '123456', 'phone': "+7-906-332-33-33", 'userStatus': 0}
    response_create_user_without_id = requests.post(url, json=request_create_user_without_id)
    # ожидаю, что пользователь не создан (статус код == 500)
    assert response_create_user_without_id.status_code == 500


# создание пользователя с набором без username
def test_post_create_user_without_username():
    request_create_user_without_username = {'id': 777999, 'firstName': "Antuanetta", 'lastName': "Ioganna",
               'email': "ok@ok.ru", 'password': '123456', 'phone': "+7-906-332-33-33", 'userStatus': 0}
    response_create_user_without_username = requests.post(url, json=request_create_user_without_username)
    # ожидаю, что пользователь не создан (статус код != 200)
    assert response_create_user_without_username.status_code != 200


# создание пользователя с символами в username
def test_post_create_user_simbols_in_username():
    request_create_user_simbols_in_username = {'id': 777999, 'username': "Antuanetta!@#$%^&*()",
                                               'firstName': "Antuanetta", 'lastName': "Ioganna", 'email': "ok@ok.ru",
                                               'password': '123456', 'phone': "+7-906-332-33-33", 'userStatus': 0}
    response_create_user_simbols_in_username = requests.post(url, json=request_create_user_simbols_in_username)
    # ожидаю, что пользователь не создан (статус код != 200)
    assert response_create_user_simbols_in_username.status_code != 200


# удаление пользователя с символами в username
def test_post_delete_user_simbols_in_username():
    response_delete_user_simbols_in_username = requests.delete(url + '/' + 'Antuanetta!@#$%^&*()')
    # ожидаю, что пользователь удалён и статус код 200
    assert response_delete_user_simbols_in_username.status_code == 200

# создание пользователя со спец символами в username
def test_post_create_user_special_simbols_in_username():
    request_create_user_special_simbols_in_username = {'id': 777999, 'username': "Antuanetta\t!",
                                                       'firstName': "Antuanetta", 'lastName': "Ioganna",
               'email': "ok@ok.ru", 'password': '123456', 'phone': "+7-906-332-33-33", 'userStatus': 0}
    response_create_user_special_simbols_in_username = requests.post(
        url, json=request_create_user_special_simbols_in_username)
    # ожидаю, что пользователь не создан. статус 500
    assert response_create_user_special_simbols_in_username.status_code == 500

# удаление пользователя со спец символами в username
def test_post_delete_user_special_simbols_in_username():
    response_delete_user_special_simbols_in_username = requests.delete(url + '/' + 'Antuanetta\t!')
    # ожидаю, что пользователь удалён и статус код 200
    assert response_delete_user_special_simbols_in_username.status_code == 200


# создание пользователя с символами в phone
def test_post_create_user_simbols_in_phone():
    request_create_user_simbols_in_phone = {'id': 777999, 'username': "Antuanetta", 'firstName': "Antuanetta",
                                            'lastName': "Ioganna", 'email': "ok@ok.ru", 'password': '123456',
                                            'phone': "ввн jrk33", 'userStatus': 0}
    response_create_user_simbols_in_phone = requests.post(url, json=request_create_user_simbols_in_phone)
    # ожидаю, что пользователь не создан. статус 500
    assert response_create_user_simbols_in_phone.status_code == 500


# создание пользователя с дополнительным полем
def test_post_create_user_addition_field():
    request_create_user_addition_field = {'id': 777999, 'id2': 777000, 'username': "Antuanetta!@#$%^&*()",
                                          'firstName': "Antuanetta", 'lastName': "Ioganna", 'email': "ok@ok.ru",
                                          'password': '123456', 'phone': "+7-906-332-33-33", 'userStatus': 0}
    response_create_user_addition_field = requests.post(url, json=request_create_user_addition_field)
    # ожидаю, что пользователь не создан. статус 500
    assert response_create_user_addition_field.status_code == 500


# очистка после тестов. удаление пользователя
def test_post_delete_user():
    response_delete_user = requests.delete(url + '/' + 'Antuanetta')
    # ожидаю, что пользователь удалён и статус код 200
    assert response_delete_user.status_code == 200
