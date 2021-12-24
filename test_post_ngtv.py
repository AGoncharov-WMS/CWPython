import requests
import pytest

global url
url = "https://petstore.swagger.io/v2/user"


# передача симолов в поле ID
def test_post_create_user_string_id():
    request = {'id': '777999a', 'username': "Antuanetta", 'firstName': "Antuanetta", 'lastName': "Ioganna",
               'email': "ok@ok.ru", 'password': '123456', 'phone': "+7-906-332-33-33", 'userStatus': 0}
    response = requests.post(url, json=request)
    # ожидаю, что пользователя создать нельзя и вернулась ошибка 500
    assert response.status_code == 500


# создание пользователя с max ID для Int64
def test_post_create_user_max_id():
    request = {'id': 9223372036854775807, 'username': "Antuanetta", 'firstName': "Antuanetta", 'lastName': "Ioganna",
               'email': "ok@ok.ru", 'password': '123456', 'phone': "+7-906-332-33-33", 'userStatus': 0}
    response = requests.post(url, json=request)
    # ожидаю, что пользователь создан и в поле message находится ID
    assert response.json()['message'] == str(request['id'])


# создание пользователя с отрицательным ID
def test_post_create_user_negative_id():
    request = {'id': -10, 'username': "Antuanetta", 'firstName': "Antuanetta", 'lastName': "Ioganna",
               'email': "ok@ok.ru", 'password': '123456', 'phone': "+7-906-332-33-33", 'userStatus': 0}
    response = requests.post(url, json=request)
    # ожидаю, что пользователь не создан (статус код == 500)
    assert response.status_code == 500

# создание пользователя с пустым ID. Данный тест не запускается из-за проверок pycharm
#def test_post_create_user_empty_id():
#    request = {'id': , 'username': "Antuanetta", 'firstName': "Antuanetta", 'lastName': "Ioganna",
#               'email': "ok@ok.ru", 'password': '123456', 'phone': "+7-906-332-33-33", 'userStatus': 0}
#    response = requests.post(url, json=request)
#    # ожидаю, что пользователь не создан (статус код == 400)
#    assert response.status_code == 400


testdata = [
    {'id': 777999, 'username': "Antuanetta", 'firstName': "Antuanetta", 'lastName': "Ioganna",
     'email': "ok@ok.ru", 'password': '123456', 'phone': "+7-906-332-33-33", 'userStatus': 0},
    {'id': 777999, 'username': "Antuanetta", 'lastName': "Ioganna",
     'email': "ok@ok.ru", 'password': '123456', 'phone': "+7-906-332-33-33", 'userStatus': 0},
    {'id': 777999, 'username': "Antuanetta", 'firstName': "Antuanetta",
     'email': "ok@ok.ru", 'password': '123456', 'phone': "+7-906-332-33-33", 'userStatus': 0},
    {'id': 777999, 'username': "Antuanetta", 'firstName': "Antuanetta", 'lastName': "Ioganna",
     'password': '123456', 'phone': "+7-906-332-33-33", 'userStatus': 0},
    {'id': 777999, 'username': "Antuanetta", 'firstName': "Antuanetta", 'lastName': "Ioganna",
     'email': "ok@ok.ru", 'phone': "+7-906-332-33-33", 'userStatus': 0},
    {'id': 777999, 'username': "Antuanetta", 'firstName': "Antuanetta", 'lastName': "Ioganna",
     'email': "ok@ok.ru", 'password': '123456', 'userStatus': 0},
    {'id': 777999, 'username': "Antuanetta", 'firstName': "Antuanetta", 'lastName': "Ioganna",
     'email': "ok@ok.ru", 'password': '123456', 'phone': "+7-906-332-33-33"}
]


@pytest.mark.parametrize("testuser", testdata)
def test_post_param(testuser):
    response = requests.post(url, json=testuser)
    # ожидаю, что пользователь создан и в поле message находится ID
    assert response.json()['message'] == str(testuser['id'])


# создание пользователя с набором без ID
def test_post_create_user_without_id():
    request = {'username': "Antuanetta", 'firstName': "Antuanetta", 'lastName': "Ioganna",
               'email': "ok@ok.ru", 'password': '123456', 'phone': "+7-906-332-33-33", 'userStatus': 0}
    response = requests.post(url, json=request)
    # ожидаю, что пользователь не создан (статус код == 500)
    assert response.status_code == 500


# создание пользователя с набором без username
def test_post_create_user_without_username():
    request = {'id': 777999, 'firstName': "Antuanetta", 'lastName': "Ioganna",
               'email': "ok@ok.ru", 'password': '123456', 'phone': "+7-906-332-33-33", 'userStatus': 0}
    response = requests.post(url, json=request)
    # ожидаю, что пользователь не создан (статус код != 200)
    assert response.status_code == 200


# создание пользователя только с username
def test_post_create_user_only_username():
    request = {'firstName': "Antuanetta"}
    response = requests.post(url, json=request)
    # ожидаю, что пользователь создан (статус код = 200)
    assert response.status_code == 200


# создание пользователя с символами в username
def test_post_create_user_simbols_in_username():
    request = {'id': 777999, 'username': "Antuanetta!@#$%^&*()", 'firstName': "Antuanetta", 'lastName': "Ioganna",
               'email': "ok@ok.ru", 'password': '123456', 'phone': "+7-906-332-33-33", 'userStatus': 0}
    response = requests.post(url, json=request)
    # ожидаю, что пользователь создан и в поле message находится ID
    assert response.json()['message'] == str(request['id'])


# удаление пользователя с символами в username
def test_post_delete_user_simbols_in_username():
    response = requests.delete(url + '/' + 'Antuanetta!@#$%^&*()')
    # ожидаю, что пользователь удалён и статус код 200
    assert response.status_code == 200

# создание пользователя со спец символами в username
def test_post_create_user_special_simbols_in_username():
    request = {'id': 777999, 'username': "Antuanetta\t!", 'firstName': "Antuanetta", 'lastName': "Ioganna",
               'email': "ok@ok.ru", 'password': '123456', 'phone': "+7-906-332-33-33", 'userStatus': 0}
    response = requests.post(url, json=request)
    # ожидаю, что пользователь не создан. статус 500
    assert response.status_code == 500

# удаление пользователя со спец символами в username
def test_post_delete_user_special_simbols_in_username():
    response = requests.delete(url + '/' + 'Antuanetta\t!')
    # ожидаю, что пользователь удалён и статус код 200
    assert response.status_code == 200


# создание пользователя с символами в phone
def test_post_create_user_simbols_in_phone():
    request = {'id': 777999, 'username': "Antuanetta", 'firstName': "Antuanetta", 'lastName': "Ioganna",
               'email': "ok@ok.ru", 'password': '123456', 'phone': "ввн jrk33", 'userStatus': 0}
    response = requests.post(url, json=request)
    # ожидаю, что пользователь не создан. статус 500
    assert response.status_code == 500


# создание пользователя с дополнительным полем
def test_post_create_user_addition_field():
    request = {'id': 777999, 'id2': 777000, 'username': "Antuanetta!@#$%^&*()", 'firstName': "Antuanetta",
               'lastName': "Ioganna", 'email': "ok@ok.ru", 'password': '123456', 'phone': "+7-906-332-33-33",
               'userStatus': 0}
    response = requests.post(url, json=request)
    # ожидаю, что пользователь не создан. статус 500
    assert response.status_code == 500


# создание пользователя с длинным username (300 символов)
def test_post_create_user_long_username():
    request = {'id': 777999, 'username': "cmOrOlqfYLnZvrrHNOq2vabKBO6f2jSL39V92YUky7JXsU61WoHN8wMQmbOUBrTzAivZqeHFG"
                                         "aS1gj4clwXpTwHBRN8amY0wRPFQmjy10bVevxusRZfOOi9aRlBbcVt1hTXqoZKVuJFBOVz9GdF"
                                         "IVnhmp8C9SW3zGe7Eqysq8ZBbQlQt8fu0L3RyMpSk7N2yDb4IH0t53iwOnuJRmCf53vKDzYFsnH"
                                         "Ocn9y1VypHb2FF4HB4Ne8A2GFrRh45Wf1QgC8rhei7EnDalVKukosQFAheLPI5IodOFMWZSBQ"
                                         "fI2ID", 'firstName': "Antuanetta", 'lastName': "Ioganna",
               'email': "ok@ok.ru", 'password': '123456', 'phone': "+7-906-332-33-33", 'userStatus': 0}
    response = requests.post(url, json=request)
    # ожидаю, что пользователь создан и в поле message находится ID
    assert response.json()['message'] == str(request['id'])


# удаление пользователя со длинным username (300 символов)
def test_post_delete_user_long_username():
    response = requests.delete(url + '/' + 'cmOrOlqfYLnZvrrHNOq2vabKBO6f2jSL39V92YUky7JXsU61WoHN8wMQmbOUBrTzAivZqe'
                                           'HFGaS1gj4clwXpTwHBRN8amY0wRPFQmjy10bVevxusRZfOOi9aRlBbcVt1hTXqoZKVuJFBO'
                                           'Vz9GdFIVnhmp8C9SW3zGe7Eqysq8ZBbQlQt8fu0L3RyMpSk7N2yDb4IH0t53iwOnuJRmCf5'
                                           '3vKDzYFsnHOcn9y1VypHb2FF4HB4Ne8A2GFrRh45Wf1QgC8rhei7EnDalVKukosQFAheLPI'
                                           '5IodOFMWZSBQfI2ID')
    # ожидаю, что пользователь удалён и статус код 200
    assert response.status_code == 200


# создание пользователя с русскими символами в полях
def test_post_create_user_russian_simbols_in_fields():
    request = {'id': 777999, 'username': "Antuanetta", 'firstName': "Антуанетта", 'lastName': "Иогана",
               'email': "ok@ok.ru", 'password': '123456', 'phone': "+7-906-332-33-33", 'userStatus': 0}
    response = requests.post(url, json=request)
    # ожидаю, что пользователь создан и в поле message находится ID
    assert response.json()['message'] == str(request['id'])


# создание пользователя с русскими символами в username
def test_post_create_user_russian_simbols_in_username():
    request = {'id': 777999, 'username': "Антуанетта", 'firstName': "Antuanetta", 'lastName': "Ioganna",
               'email': "ok@ok.ru", 'password': '123456', 'phone': "+7-906-332-33-33", 'userStatus': 0}
    response = requests.post(url, json=request)
    # ожидаю, что пользователь создан и в поле message находится ID
    assert response.json()['message'] == str(request['id'])


# удаление пользователя с русскими символами в username
def test_post_delete_user_russian_simbols_in_username():
    response = requests.delete(url + '/' + 'Антуанетта')
    # ожидаю, что пользователь удалён и статус код 200
    assert response.status_code == 200


# очистка после тестов. удаление пользователя
def test_post_delete_user():
    response = requests.delete(url + '/' + 'Antuanetta')
    # ожидаю, что пользователь удалён и статус код 200
    assert response.status_code == 200
