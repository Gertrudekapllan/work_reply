# TODO Реализовать парсер на сайте https://www.mashina.kg/
# 1. Выберите марку машины
# 2. Нужно спарсить  цену в сомах и долларах, название,  картинку, описание, количество просмотров
# (спарсить все машины на сайте данной марки реализуя пагинацию )
# 3. Сохранить все данные в csv файл

from urllib import request
from bs4 import BeautifulSoup

# URL-адрес для начала парсинга
base_url = "https://www.mashina.kg/search/honda/all/?currency=2&sort_by=upped_at+desc&page="

make = "acura"
list_result_of_cars = []


#TODO пагинация: 1 - вычислить количество найденных машин с помощью бьют супа. класс кнопки общего колва найденных машин
# и получить атрибут - число. <input type="submit" class="btn btn-primary" id="search-submit" value="Найдено 4057
# объявлений"> с помощью ре можно получчить только число. 2 - сделать бескон число обходов цикла по страницам пока
# результат не вернет пустой список то и будет условием прерывания цикла.


def get_cars_on_page(soup):
    list_result_of_cars_local = soup.select('.table-view-list .list-item')
    for item in list_result_of_cars_local:
        car = {'name': None, 'image': None, 'price_dollar': None, 'price_som': None}
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



def get_all_pages():
    count = 200
    base_url = "https://www.mashina.kg/search/honda/all/?currency=2&sort_by=upped_at+desc&page="
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
# req = request.Request(base_url, headers=headers)
# response = request.urlopen(req)
# get_quantity_cars(body=response)


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