import json
import requests
from re import match
from time import sleep
from os import mkdir, path
from urllib import request
from bs4 import BeautifulSoup


def print_hello_message():
    print("""
    Введи URL любого раздела сайта Ozon вида 'https://www.ozon.ru/category/<имя_категории>/',
    и я скачаю все картинки товаров этого раздела со всех страниц в папку, которую ты укажешь.
    """)

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

def get_url():
    while True:
        try:
            url = input("Введи URL раздела: ").strip()
            if not match(r'https:\/\/www\.ozon\.ru\/category\/(.+)\/$', url):
                print("Похоже, это не сайт Озона или раздел, который я не умею парсить.")
                continue
            if request.urlopen(url).getcode() != 200:
                print("Неверный адрес раздела или сервер не отвечает.")
                continue
            return url
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

    images = []

    try:
        for script in soup.find_all('script'):
            ID = script.get('id')
            if ID and ID.startswith('state-searchResultsV2'):
                json_data = json.loads(str(script.contents[0]))
                break

        for item in json_data['items']:
            images.append(item['images'])

    except Exception as Ex:
        print("Нас забанили, или закончились страницы в данном разделе.")
        print(Ex)
    finally:
        return images

def get_pictures_links_from_all_pages(url):
    params = get_user_ya_xml()
    all_pictures = []
    for page in range(1, 10):
        params['page'] = page
        pics_of_page = get_pictures_list(params, url)
        if not pics_of_page:
            break
        all_pictures.append(pics_of_page)
        print(f"Page {page} done.")
        sleep(15)
    return all_pictures

def unpack_pictures_lists(pictures_lists):
    pictures = []
    for l1 in pictures_lists:
        for l2 in l1:
            pictures.extend(l2)
    return pictures

def save_pictures(all_pictures, dir):
    for picture in all_pictures:
        pic = requests.get(pic, stream=True)
        file_path = path.join(dir, pic[-14:])
        with open(file_path, "wb") as f:
            f.write(pic.content)



user_dir = make_dir()
URL = get_url()

all_pictures = get_pictures_links_from_all_pages(URL)

pictures_list = unpack_pictures_lists(all_pictures)

save_pictures(pictures_list, user_dir)




