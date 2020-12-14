import requests
from bs4 import BeautifulSoup

URL = 'http://frsah.ro/index.php/2020/12/14/comisia-de-sah-in-scoala-a-frsah-se-reuneste-in-data-de-8-ianuarie-2021/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

content = soup.find(id='post-9861')
# print(results_table.prettify())

title_content = content.find(class_='td-post-header')
title = title_content.find('h1', class_='entry-title')

post_content = content.find(class_='td-post-content')
text_content = post_content.find('p')

with open('homework.txt', 'w') as file:
    file.write(str(title))
    file.write('\n')
    file.write(str(text_content))

with open('homework.txt', 'r') as file:
    for line in file.readlines():
        print(f'line: {line}', end='')