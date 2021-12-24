import requests
import pytest
#vvb
global url
url = "https://petstore.swagger.io/v2/user"

global request

request = {'id': 777999, 'username': "Antuanetta", 'firstName': "Antuanetta", 'lastName': "Ioganna",
           'email': "ok@ok.ru", 'password': '123456', 'phone': "+7-906-332-33-33", 'userStatus': 0}


def test_get_login():
    urlAuth = url + "/login?username=Admin&password=Admin"
    response = requests.get(urlAuth)
    # проверка успешна ли авторизация
    assert response.status_code == 200


def test_post_create_user():
    print('Request = ', request)

    # так как серверов несколько, создаю пользователя несколько раз
    for i in range(5):
        print(str(i + 1) + ' раз')
        response = requests.post(url, json=request)
        # на 5 раз проверяю создался ли пользователь. message должно быть равно id
        if i == 4:
            print('Response post = ', response.json())
            assert response.json()['message'] == str(request['id'])

            response = requests.get(url + '/' + request['username'])
            print('Response get = ', response.json())
            assert response.json()['id'] == request['id']


def test_delete_user():
    # так как серверов несколько, удаляю пользователя несколько раз
    for i in range(5):
        print(str(i + 1) + ' раз')
        response = requests.delete(url + '/' + request['username'])
        # на 1 раз проверяю удалился ли пользователь. message должно быть равно username
        if i == 0:
            print('Response delete = ', response.json())
            assert response.json()['message'] == str(request['username'])
    # проверка наличия пользователя
    response = requests.get(url + '/' + request['username'])
    print('Response get = ', response.json())
    assert response.status_code == 404


# попытка удаления после удаления
def test_delete_after_delete_user():
    response = requests.delete(url + '/' + request['username'])
    assert response.status_code == 404


# выход из системы
def test_get_logout():
    response = requests.get(url + '/logout')
    assert response.json()['message'] == 'ok'
