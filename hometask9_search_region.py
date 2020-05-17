import requests
from bs4 import BeautifulSoup


def print_hello_message():
    print("""
    Привет, юзернейм!
    Ты можешь получить список ссылок, которые выдаёт Яндекс при поиске в
    определённом регионе. Для этого тебе может оказаться достаточно
    ввести текст запроса и код региона, но лучше также загляни сюда:
    https://xml.yandex.ru/settings/ и получи свой уникальный идентификатор,
    а затем введи его в программу. Таким образом тебя не забанят. Возможно,
    не забанят и без этого, но лучше не рисковать.
    Результат поиска в виде полезных ссылок ты увидишь на экране, а также
    в сохранённом файле вида <код_региона>_<текст_запроса>.txt.

    Вот несколько популярных кодов регионов:
    213 - Москва
    1 - Москва и Московская область
    2 - Сант-Петербург
    187 - Украина
    149 - Беларусь
    159 - Казахстан

    Более подробный список можешь посмотреть здесь:
    https://yandex.ru/dev/xml/doc/dg/reference/regions-docpage

    Чтобы выйти из программы до её завершения, нажми Ctrl+C.
    """)

def get_user_ya_xml():
    print("Введи учётные данные ya.xml, если они есть, или нажми Enter.")
    try:
        while True:
            user = input('user=').strip()
            if user: break

            if not user:
                print("Попробуем так, но нас быстро забанят.")
                return False

        while True:
            key = input('key=').strip()
            if key: break

            if not key:
                print("Попробуем так, но нас быстро забанят.")
                return False
        return user, key

    except KeyboardInterrupt:
        exit()

def get_user_request():
    while True:
        try:
            request = input("Введите запрос: ")
            if request:
                return request
            print("Пустая строка не считается!")
            continue
        except KeyboardInterrupt:
            exit()

def get_user_region():
    while True:
        try:
            region = input("Введите регион поиска: ").strip()
            if region.isdecimal():
                return region
            print("Только цифры, пожалуйста.")
            continue
        except KeyboardInterrupt:
            exit()

def search_with_lr(query):

    s = requests.Session()
    s.headers.update({
        'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 YaBrowser/20.3.2.282 (beta) Yowser/2.5 Safari/537.36',
        'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language' : 'ru,en;q=0.9'
        })

    response = s.get("https://yandex.ru/search/", params=query)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = []

    if soup.find_all('form', action="/checkcaptcha"):
        print("Поздравляю, вы всё сломали. Теперь нас забанили в Яндексе.")
        exit()

    for link in soup.find_all('a', class_='link link_theme_normal organic__url link_cropped_no i-bem'):
        print(link['href'])
        links.append(link['href'])

    return links

def save_links(links):
    try:
        with open(f"{region}_{request}.txt", "w") as f:
            print(*links, file=f)
    except:
        with open("temp.txt", "w") as f:
            print(*links, file=f)
        print("""
    Ошибка записи в файл. Возможно, запрос содержит недопустимые символы.
    Вы можете посмотреть результаты во временном файле 'temp.txt.'""")
        pass


print_hello_message()

ya_xml = get_user_ya_xml()
request = get_user_request()
region = get_user_region()

query = {'text' : request, 'lr' : region}

if ya_xml:
    user, key = ya_xml
    query['user'] = user
    query['key'] = key

links = search_with_lr(query)
save_links(links)