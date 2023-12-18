import http.client # Модуль для работы с HTTP-запросами
from html.parser import HTMLParser # Модуль для парсинга HTML

class MyParser(HTMLParser): # Метод handle_starttag вызывается при парсинге любого открывающего тега
    img = [] # Список
    links = [] # Список

    def handle_starttag(self, tag, attrs): # Вызывается при обнаружении каждого открывающего HTML-тега
        if tag == 'img': # Проверка на то, является ли тег <img>
            for attr in attrs: # Если да, то извлекается значение атрибутов src (для изображений)
                if attr[0] == 'src':
                    self.img.append(attr[1]) # Добавление значения атрибута в список

        if tag == 'a': # Для других ссылок
            for attr in attrs: # Если да, то извлекается значение атрибутов href (для ссылок)
                if attr[0] == 'href':
                    self.links.append(attr[1]) # Добавление значения атрибута в список

parser = MyParser() # Создаем экземпляр класса MyParser
conn = http.client.HTTPSConnection("beda.pnzgu.ru") # Устанавливаем соединение с сервером beda.pnzgu.ru методом HTTPS
conn.request("GET", "/anatoly/") # отправляем запрос на сервер методом GET
r = conn.getresponse() # Получаем ответ от сервера
parser.feed(r.read().decode()) # Передаем полученные данные в метод feed() для парсинга
parser.close()

print(parser.links) # Печать списка ссылок, которые были извлечены при парсинге

# Блок для выполнения цикла для каждой извлеченной ссылки. Происходит повторное отправление запроса на каждый URL, извлечение HTML-кода с этой страницы, его парсинг.
# Затем происходит отправка запроса на загрузку изображения и сохранение его под новым именем: tolya_ (где _ - порядковый номер изображения)
for i in range(len(parser.links)):
    conn.request("GET", "/anatoly/" + parser.links[i])
    r = conn.getresponse()
    parser.feed(r.read().decode())
    parser.close()
    conn.request("GET", "/anatoly/" + parser.img[i])
    r = conn.getresponse()

    with open('TOLYAN/' + 'Anatoly' + str(i) + '.png', 'wb') as f:
        f.write(r.read())
    
    # Участок кода для вывода на экран значения parser.links[i] - ссылки на страницу, которая была извлечена в цикле.
    # Затем parser.img[i] - значения атрибута src тега img, которое является URL изображения на этой странице.
    # Он используется для отслеживания процесса и проверки того, что программа извлекает нужные данные
    print(parser.links[i])
    print(parser.img[i])

# Блок для отправления запроса на загрузку извлеченного изображения и сохранения его под именем Vaserman.png    
for image in parser.img:
    conn.request("GET", "/anatoly/" + image)
    r = conn.getresponse()
    with open('TOLYAN/' + 'Vaserman.png', 'wb') as f:
        f.write(r.read())
