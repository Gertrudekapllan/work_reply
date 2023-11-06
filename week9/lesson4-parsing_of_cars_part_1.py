# TODO Реализовать парсер на сайте https://www.mashina.kg/
# 1. Выберите марку машины
# 2. Нужно спарсить  цену в сомах и долларах, название,  картинку, описание, количество просмотров
# (спарсить все машины на сайте данной марки реализуя пагинацию )
# 3. Сохранить все данные в csv файл

from urllib import request
from bs4 import BeautifulSoup
import csv

# URL-адрес для начала парсинга
base_url = "https://www.mashina.kg/search/acura/all/"

make = "acura"
list_result_of_cars = []

def get_cars_on_page(body):

    soup = BeautifulSoup(body, 'html.parser')
    list_result_of_cars_local = soup.select('.table-view-list .list-item')
    for item in list_result_of_cars_local:
        name = item.find(class_='name').get_text().strip()
        image = item.find(class_='lazy-image')['data-src']
        price = item.find(class_='block price').get_text().strip()
        price_parts = price.split()
        print(price, 'цена в сомах')
        # Выберите вторую часть, которая содержит цену в сомах
        price_soms = price_parts[0:3]

        print("цена в долл:", price_soms)
        print(name, price)

# пагинация: 1 - вычислить количество найденных машин с помощью бьют супа. класс кнопки общего колва найденных машин и получить атрибут - число. <input type="submit" class="btn btn-primary" id="search-submit" value="Найдено 4057 объявлений"> с помощью ре можно получчить только число. 2 - сделать бескон число обходов цикла по страницам пока результат не вернет пустой список то и будет условием прерывания цикла.
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/58.0.3029.110 Safari/537.36 '
}
req = request.Request(base_url, headers=headers)
response = request.urlopen(req)
get_cars_on_page(body=response)

# # CSV-файл для записи данных
# with open('mashina_kg_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     fieldnames = ['Title', 'Price (KGS)', 'Price (USD)', 'Description', 'Views', 'Image URL']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#
#     # парсинг страниц с пагинацией
#     page = 1
#     while True:
#         page_url = f"{base_url}{make}/page/{page}"
#         response = requests.get(page_url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#
#         # Парсинг информации о машинах
#         cars = soup.find_all('div', class_='classified__content')
#         if not cars:
#             break  # Если нет больше машин, выходим из цикла
#
#         for car in cars:
#             title = car.find('h2', class_='classified__title').text
#             price_kgs = car.find('span', class_='classified__price_kgs').text
#             price_usd = car.find('span', class_='classified__price_usd').text
#             description = car.find('p', class_='classified__description').text
#             views = car.find('span', class_='classified__views').text
#             image_url = car.find('img', class_='classified__img')['src']
#
#             # Запись данных в CSV-файл
#             writer.writerow({
#                 'Title': title,
#                 'Price (KGS)': price_kgs,
#                 'Price (USD)': price_usd,
#                 'Description': description,
#                 'Views': views,
#                 'Image URL': image_url
#             })
#
#         page += 1  # Переход к следующей странице
#
# print("Парсинг завершен и данные сохранены в mashina_kg_data.csv.")
