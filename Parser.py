import requests
from bs4 import BeautifulSoup
def parse():
    url = 'https://omsk.drom.ru/auto/all/?minprice=950000&unsold=1&distance=200&order=price'
    page = requests.get(url)
    print(page.status_code)
    page_parsed = BeautifulSoup(page.text, 'html.parser')
    autos = page_parsed.findAll('div', class_='css-l1wt7n e3f4v4l2')
    autos1 = page_parsed.findAll('span', class_='css-46itwz e162wx9x0')
    with open('autos.txt', 'w') as f:
        for auto in autos:
            name = auto.find('span').text.strip()
            for auto1 in autos1:
                name1 = auto1.find('span').text.strip()
                f.write('Модель: ' + name + ' года. Цена: ' + name1 + ' руб.' '\n')
                break