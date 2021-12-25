import requests
import pytest

global url
url = "https://petstore.swagger.io/v2/user"


# создание пользователя с max ID для Int64
def test_post_create_user_max_id():
    request_create_user_max_id = {'id': 9223372036854775807, 'username': "Antuanetta", 'firstName': "Antuanetta",
                                  'lastName': "Ioganna", 'email': "ok@ok.ru", 'password': '123456',
                                  'phone': "+7-906-332-33-33", 'userStatus': 0}
    response_create_user_max_id = requests.post(url, json=request_create_user_max_id)
    # ожидаю, что пользователь создан и в поле message находится ID
    assert response_create_user_max_id.json()['message'] == str(request_create_user_max_id['id'])


# создание пользователя с нулевым ID
def test_post_create_user_zero_id():
    request_zero_id = {'id': 0, 'username': "Antuanetta", 'firstName': "Antuanetta", 'lastName': "Ioganna",
               'email': "ok@ok.ru", 'password': '123456', 'phone': "+7-906-332-33-33", 'userStatus': 0}
    response_zero_id = requests.post(url, json=request_zero_id)
    # ожидаю, что пользователь создан и в поле message находится ID
    assert response_zero_id.json()['message'] == str(request_zero_id['id'])


# Параметризованный тест. Создание пользователя при отсутсвии одного из полей
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
    response_param_create_user = requests.post(url, json=testuser)
    # ожидаю, что пользователь создан и в поле message находится ID
    assert response_param_create_user.json()['message'] == str(testuser['id'])


# создание пользователя только с username
def test_post_create_user_only_username():
    request_only_username = {'firstName': "Antuanetta"}
    response_only_username = requests.post(url, json=request_only_username)
    # ожидаю, что пользователь создан (статус код = 200)
    assert response_only_username.status_code == 200


# создание пользователя с длинным username (300 символов)
def test_post_create_user_long_username():
    request_create_long_username = {'id': 777999, 'username': "cmOrOlqfYLnZvrrHNOq2vabKBO6f2jSL39V92YUky7JXsU61WoHN8"
                                                              "wMQmbOUBrTzAivZqeHFGaS1gj4clwXpTwHBRN8amY0wRPFQmjy10bV"
                                                              "evxusRZfOOi9aRlBbcVt1hTXqoZKVuJFBOVz9GdFIVnhmp8C9SW3zG"
                                                              "e7Eqysq8ZBbQlQt8fu0L3RyMpSk7N2yDb4IH0t53iwOnuJRmCf53vK"
                                                              "DzYFsnHOcn9y1VypHb2FF4HB4Ne8A2GFrRh45Wf1QgC8rhei7EnDal"
                                                              "VKukosQFAheLPI5IodOFMWZSBQfI2ID",
                                    'firstName': "Antuanetta", 'lastName': "Ioganna",
               'email': "ok@ok.ru", 'password': '123456', 'phone': "+7-906-332-33-33", 'userStatus': 0}
    response_create_long_username = requests.post(url, json=request_create_long_username)
    # ожидаю, что пользователь создан и в поле message находится ID
    assert response_create_long_username.json()['message'] == str(request_create_long_username['id'])


# удаление пользователя со длинным username (300 символов)
def test_post_delete_user_long_username():
    response_del_long_username = requests.delete(url + '/' + 'cmOrOlqfYLnZvrrHNOq2vabKBO6f2jSL39V92YUky7JXsU61WoHN8'
                                                             'wMQmbOUBrTzAivZqeHFGaS1gj4clwXpTwHBRN8amY0wRPFQmjy10b'
                                                             'VevxusRZfOOi9aRlBbcVt1hTXqoZKVuJFBOVz9GdFIVnhmp8C9SW3'
                                                             'zGe7Eqysq8ZBbQlQt8fu0L3RyMpSk7N2yDb4IH0t53iwOnuJRmCf5'
                                                             '3vKDzYFsnHOcn9y1VypHb2FF4HB4Ne8A2GFrRh45Wf1QgC8rhei7E'
                                                             'nDalVKukosQFAheLPI5IodOFMWZSBQfI2ID')
    # ожидаю, что пользователь удалён и статус код 200
    assert response_del_long_username.status_code == 200


# создание пользователя с русскими символами в полях
def test_post_create_user_russian_simbols_in_fields():
    request_russian_simbols_in_fields = {'id': 777999, 'username': "Antuanetta", 'firstName': "Антуанетта",
                                         'lastName': "Иогана", 'email': "ok@ok.ru", 'password': '123456',
                                         'phone': "+7-906-332-33-33", 'userStatus': 0}
    response_russian_simbols_in_fields = requests.post(url, json=request_russian_simbols_in_fields)
    # ожидаю, что пользователь создан и в поле message находится ID
    assert response_russian_simbols_in_fields.json()['message'] == str(request_russian_simbols_in_fields['id'])


# создание пользователя с русскими символами в username
def test_post_create_user_russian_simbols_in_username():
    request_russian_simbols_in_username = {'id': 777999, 'username': "Антуанетта", 'firstName': "Antuanetta",
                                           'lastName': "Ioganna", 'email': "ok@ok.ru", 'password': '123456',
                                           'phone': "+7-906-332-33-33", 'userStatus': 0}
    response_russian_simbols_in_username = requests.post(url, json=request_russian_simbols_in_username)
    # ожидаю, что пользователь создан и в поле message находится ID
    assert response_russian_simbols_in_username.json()['message'] == str(request_russian_simbols_in_username['id'])


# удаление пользователя с русскими символами в username
def test_post_delete_user_russian_simbols_in_username():
    response_russian_simbols_in_username = requests.delete(url + '/' + 'Антуанетта')
    # ожидаю, что пользователь удалён и статус код 200
    assert response_russian_simbols_in_username.status_code == 200


# очистка после тестов. удаление пользователя
def test_post_delete_user():
    response_delete_user = requests.delete(url + '/' + 'Antuanetta')
    # ожидаю, что пользователь удалён и статус код 200
    assert response_delete_user.status_code == 200
