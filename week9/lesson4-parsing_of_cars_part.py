# TODO Реализовать парсер на сайте https://www.mashina.kg/
# 1. Выберите марку машины
# 2. Нужно спарсить  цену в сомах и долларах, название,  картинку, описание, количество просмотров
# (спарсить все машины на сайте данной марки реализуя пагинацию )
# 3. Сохранить все данные в csv файл...

import pandas as pd
from urllib import request
from bs4 import BeautifulSoup

list_result_of_cars = []


def get_details_of_cars(page_link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.36 '
    }
    req = request.Request(page_link, headers=headers)
    response = request.urlopen(req)
    soup = BeautifulSoup(response, 'html.parser')
    res = soup.select_one('.seller-comments .comment').get_text().strip()
    return res


def get_cars_on_page(soup):
    list_result_of_cars_local = soup.select('.table-view-list .list-item')
    for item in list_result_of_cars_local:
        car = {'name': None, 'image': None, 'price_dollar': None, 'price_som': None, 'description': None, 'views': None}
        car['views'] = item.find(class_='counters').find(class_='listing-icons').get_text()
        print(car['views'])
        car['name'] = item.find(class_='name').get_text().strip()
        images = item.find(class_='lazy-image')
        image = ''
        if images is not None:
            image = images['src']
        car['image'] = image
        price = item.find(class_='block price')
        car['price_dollar'] = item.find(class_='block price').select_one('strong').get_text()
        price.strong.extract()
        car['price_soms'] = price.get_text().strip()
        list_result_of_cars.append(car)
        page_link = item.find('a')['href']
        car['description'] = get_details_of_cars('https://www.mashina.kg' + page_link)


def get_all_pages():
    count = 1
    base_url = "https://www.mashina.kg/search/acura/all/?currency=2&sort_by=upped_at+desc&page="
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.36 '
    }
    no_results = False
    while not no_results:
        req = request.Request(base_url + str(count), headers=headers)
        response = request.urlopen(req)
        soup = BeautifulSoup(response, 'html.parser')
        no_res_soup = soup.find(class_='list-item')
        get_cars_on_page(soup)
        if no_res_soup is None:
            no_results = True
        count += 1


get_all_pages()
print(list_result_of_cars)

df = pd.DataFrame(list_result_of_cars)
df.to_csv("list_of_dict_to_csv.csv")

# req = request.Request(base_url, headers=headers)
# response = request.urlopen(req)
# get_quantity_cars(body=response)
