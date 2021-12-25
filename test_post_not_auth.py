import requests
import pytest

global url
url = "https://petstore.swagger.io/v2/user"

global request

request = {'id': 777999, 'username': "Antuanetta", 'firstName': "Antuanetta", 'lastName': "Ioganna",
           'email': "ok@ok.ru", 'password': '123456', 'phone': "+7-906-332-33-33", 'userStatus': 0}


# проверка создания пользователя без авторизации
def test_post_create_user():
    response_create_user = requests.post(url, json=request)
    print('Response post = ', response_create_user.json())
    # если пользователь создан то в message записан id, а нам этого не надо
    assert response_create_user.json()['message'] != str(request['id'])


# проверка удаления пользователя без авторизации
def test_delete_user():
    response_del_user = requests.delete(url + '/' + request['username'])
    print('Response delete = ', response_del_user.json())
    # если пользователь удалён то в message записан username, а нам этого не надо. Без авторизации удалять нельзя
    assert response_del_user.json()['message'] != str(request['username'])


# проверка выхода из системы без авторизации
def test_get_logout():
    response_logout = requests.get(url + '/logout')
    # Ожидаю сообщение, что авторизация не выполнена
    assert response_logout.json()['message'] != 'ok'
