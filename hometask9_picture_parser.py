# Напишите парсер картинок с любого раздела сайта OZON, который их сохраняет на компьютер

import re
import json
import requests
from os import mkdir, path
from bs4 import BeautifulSoup


def print_hello_message():
    ...

def make_dir():
    while True:
        try:
            dir_for_pics = input("Введи название новой папки: ").strip()
            mkdir(dir_for_pics)
            return path.normpath(dir_for_pics)
        except FileExistsError:
            print("Папка с таким именем уже существует.")
            continue
        except KeyboardInterrupt:
            exit()

def get_user_ya_xml():
    print("Введи учётные данные ya.xml, если они есть, или нажми Enter.")
    params = {}
    try:
        while True:
            user = input('user=').strip()
            if user: break

            if not user:
                print("Попробуем так, но нас быстро забанят.")
                return params

        while True:
            key = input('key=').strip()
            if key: break

            if not key:
                print("Попробуем так, но нас быстро забанят.")
                return params

        params.update({'user': user, 'key': key})
        return params

    except KeyboardInterrupt:
        exit()

def get_pictures_list(params, url):
    s = requests.Session()
    s.headers.update({
        'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 YaBrowser/20.3.2.282 (beta) Yowser/2.5 Safari/537.36',
        'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language' : 'ru,en;q=0.9'
        })

    response = s.get(url, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')

    # with open("soup", "w") as f:
    #         print(soup, file=f)

    # # with open('soup', 'r') as f:
    # #     soup = f.read()

    # soup = BeautifulSoup(soup, 'html.parser')

    images = []
    # import pdb; pdb.set_trace()

    for script in soup.find_all('script'):
        ID = script.get('id')
        if ID and ID.startswith('state-searchResultsV2'):
            json_data = json.loads(str(script.contents[0]))

    for item in json_data['items']:
        images.append(item['images'])

    print(images)
    
    return images




def save_pictures():
    ...

# make_dir()

URL = 'https://www.ozon.ru/category/yazyki-programmirovaniya-33705/'

params = get_user_ya_xml()

get_pictures_list(params, URL)







# https://cdn1.ozone.ru/s3/multimedia-2/wc250/6007449950.jpg
# https://cdn1.ozone.ru/s3/multimedia-3/wc250/6007449951.jpg
# https://cdn1.ozone.ru/s3/multimedia-t/wc250/6000018281.jpg
# https://cdn1.ozone.ru/multimedia/wc250/1011395255.jpg