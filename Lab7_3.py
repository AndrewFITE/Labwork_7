import http.client

connect = http.client.HTTPSConnection("beda.pnzgu.ru") # Установка соединения с веб-сервером
connect.request("GET", "/anatoly/") # Отправка запроса на сервер методом GET, запрашивая содержимое страницы по указанному пути
answer = connect.getresponse() # Получение ответа от сервера на запрос

if answer.status == 200: # Код состояния HTTP 200 указывает на успешное выполнение запроса
    data = answer.read().decode()  # Декодировка полученных данных из байтов в текст
    print(data)
else:
    print("Не удалось получить запрошенную страницу. Код состояния: ", answer.status)