import requests # импортируем библиотеку requests для выполнения http-запросов
from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup для разбора html-кода
def parse():
    url = 'https://omsk.drom.ru/auto/all/' # URL адрес
    page = requests.get(url) # методом get отправляем запрос на сервер и получаем ответ в переменную
    print(page.status_code)  # выводим ответ сервера, чтобы убедиться, что запрос был успешным
    page_parsed = BeautifulSoup(page.text, 'html.parser') # обрабатываем page, передав в качестве аргументов html-код страницы и парсер, который будет использоваться для его обработки.
    employees = page_parsed.findAll('div', class_="css-17lk78h e3f4v4l2") #  находим на странице все элементы div, у которых заданы стили padding: 5px и font-size: 120%, и сохраняем их
    with open('result.txt', 'w') as f: # открываем, а точнее создаем файл в режиме записи
        for employee in employees: # проходимся в цикле по всем элементам списка employees
            name = employee.find('span') # находим в каждом элементе div первый тег 'a', получаем текст из нее методом text, удаляем лишние пробелы в начале и конце строки методом strip и сохраняем имя в переменную name.
            f.write(name + '\n') # записываем имя сотрудника в файл

