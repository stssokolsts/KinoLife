#-*- coding: utf-8 -*-
__author__ = 'Евгений'

import requests
from selenium import webdriver
from KinoLife.settings import ACCESS_TOKEN, URL_VK_MOVIE
import urlparse


#Создаем объект драйвера
def get_access_token():
    driver = webdriver.Firefox()

    # Переходим по ссылке.
    # client_id - идентификатор созданного нами приложения
    # scope - права доступа
    driver.get("http://api.vkontakte.ru/oauth/authorize?"
               "client_id=4812218&scope=offline"
               "&redirect_uri=http://api.vk.com/blank.html"
               "&display=page&response_type=token")

    user = "sokolov590@mail.ru"
    password = "12CfynfAt21"

    # Находим элементы формы и вводим данные для авторизации
    user_input = driver.find_element_by_name("email")
    user_input.send_keys(user)
    password_input = driver.find_element_by_name("pass")
    password_input.send_keys(password)

    # Нажимаем на кнопку
    submit = driver.find_element_by_id("install_allow")
    submit.click()

    # Получаем необходимые данные для выполнения запросов к api
    current = driver.current_url
    access_list = (current.split("#"))[1].split("&")
    access_token = (access_list[0].split("="))[1] # acces_token
    expires_in = (access_list[1].split("="))[1] # срок времени действия токена
    user_id = (access_list[2].split("="))[1] # id нашей учетной записи в ВК
    # Закрываем окно браузера
    driver.close()
    print(access_token)
    return {'access_token': access_token, 'user_id' : user_id}


def search(q, runtime, year=''):
    """ поиск фильма в вк учитывая год, длительность и название """
    url = URL_VK_MOVIE
    if not(runtime == 0):
        longer = (runtime-10)*60
        shorter = (runtime+10)*60
    else:
        return ""
    name_date = q + " "+ str(year)
    hd = 1
    dict_main = {
        'access_token': ACCESS_TOKEN,
        'sort' : 2,
        'count' : 3,
        'extended' : 1,
        'longer' : longer,
        'shorter' : shorter
        }

    dict_main.update( {'q' : name_date, 'hd' : hd})
    try:
        req_temp = requests.get(url, params = dict_main).json().get('response',[])
        print(requests.get(url, params = dict_main).json())
        print("4 level")
        if not (req_temp == []):
            print(req_temp[0].get('player', ''))
            return req_temp[0].get('player', '')
        else:
            print("1")
            hd = 0
            dict_main.update({'q' : name_date, 'hd' : hd})
            req_temp = requests.get(url, params = dict_main).json().get('response', [])
            if not (req_temp == []):
                print(req_temp[0].get('player', ''))
                return req_temp[0].get('player', '')
            else:
                print("2")
                hd = 1
                dict_main.update({'q' : q, 'hd' : hd})
                req_temp = requests.get(url, params = dict_main).json().get('response', [])
                if not (req_temp == []):
                    print(req_temp[0].get('player', ''))
                    return req_temp[0].get('player', '')
                else:
                    print("3")
                    hd = 0
                    dict_main.update({'q' : q, 'hd' : hd})
                    req_temp = requests.get(url, params = dict_main).json().get('response', [])
                    if not (req_temp == []):
                        print(req_temp[0].get('player', ''))
                        return req_temp[0].get('player', '')
                    else:
                        return ""
    except requests.RequestException:
        return ""


YOUTUBE_URL = "https://www.youtube.com/embed/%s?feature=player_embedded"

def get_yt_url (url):
    if (url == ""):
        return ""
    else:
        y_id = urlparse.parse_qs(url).get('http://www.youtube.com/watch?v','')[0]
        s = YOUTUBE_URL %(y_id)
        print(s)
        return s
