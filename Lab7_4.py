import http.client

connect = http.client.HTTPSConnection("beda.pnzgu.ru") # Установка соединения с веб-сервером
connect.request("GET", "/anatoly/anatoly.webp") # Отправка запроса на сервер методом GET, запрашивая содержимое страницы по указанному пути
answer = connect.getresponse() # Получение ответа от сервера на запрос

if answer.status == 200: # Код состояния HTTP 200 указывает на успешное выполнение запроса
    with open("Tolyan", "wb") as f: # Создание бинарного файла для загрузки изображения
        f.write(answer.read()) # Загрузка изображения в созданный файл
else:
    print("Не удалось получить запрошенную страницу. Код состояния: ", answer.status)