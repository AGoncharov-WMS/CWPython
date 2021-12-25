import requests
import pytest

global url
url = "https://petstore.swagger.io/v2/user"

global request

request = {'id': 777999, 'username': "Antuanetta", 'firstName': "Antuanetta", 'lastName': "Ioganna",
           'email': "ok@ok.ru", 'password': '123456', 'phone': "+7-906-332-33-33", 'userStatus': 0}


def test_get_login():
    url_auth = url + "/login?username=Admin&password=Admin"
    response_auth = requests.get(url_auth)
    # проверка успешна ли авторизация
    assert response_auth.status_code == 200


def test_post_create_user():
    print('Request = ', request)

    # так как серверов несколько, создаю пользователя несколько раз
    for i in range(5):
        print(str(i + 1) + ' раз')
        response_create_user = requests.post(url, json=request)
        # на 5 раз проверяю создался ли пользователь. message должно быть равно id
        if i == 4:
            print('Response post = ', response_create_user.json())
            assert response_create_user.json()['message'] == str(request['id'])

            response_create_user = requests.get(url + '/' + request['username'])
            print('Response get = ', response_create_user.json())
            assert response_create_user.json()['id'] == request['id']


def test_delete_user():
    # так как серверов несколько, удаляю пользователя несколько раз
    for i in range(5):
        print(str(i + 1) + ' раз')
        response_del_user = requests.delete(url + '/' + request['username'])
        # на 1 раз проверяю удалился ли пользователь. message должно быть равно username
        if i == 0:
            print('Response delete = ', response_del_user.json())
            assert response_del_user.json()['message'] == str(request['username'])

    # проверка наличия пользователя
    response = requests.get(url + '/' + request['username'])
    print('Response get = ', response.json())
    assert response.status_code == 404


# попытка удаления после удаления
def test_delete_after_delete_user():
    response_second_del = requests.delete(url + '/' + request['username'])
    assert response_second_del.status_code == 404


# выход из системы
def test_get_logout():
    response_logout = requests.get(url + '/logout')
    assert response_logout.json()['message'] == 'ok'
