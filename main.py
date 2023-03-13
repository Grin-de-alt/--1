import requests 
from bs4 import BeautifulSoup 
def parse():
    url = 'https://omsk.drom.ru/auto/all/' 
    page = requests.get(url) 
    print(page.status_code)  
    page_parsed = BeautifulSoup(page.text, 'html.parser') 
    employees = page_parsed.findAll('div', class_="css-17lk78h e3f4v4l2") 
    with open('result.txt', 'w') as f: 
        for employee in employees: 
            name = employee.find('span') 
            f.write(name + '\n') 

