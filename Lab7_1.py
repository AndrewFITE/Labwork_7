import socket

print("Соединение установлено! Ожидается подключение клиента...")
students = {"Окороков": "Андрей", "Коросткин": "Антон", "Казанкин": "Максим", "Чумаков": "Матвей"}

with socket.create_server(('127.0.0.1', 12345)) as serversocket:
    while True:
        user_socket, address = serversocket.accept()
        print("Адрес подключенного клиента:", address)
        enter_surname = "Введите фамилию студента: ".encode()
        user_socket.send(enter_surname)
        message = user_socket.recv(4096) # Читаем данные, полученные от клиента, по 4кб
        if students.setdefault(message.decode()[:-1]) == None:
            error = str("Error! Фамилия студента отсутствует в списке студентов вашей группы!" + "\n").encode()
            print("Сообщение об ошибке отправлено клиенту\n")
            user_socket.send(error)
            user_socket.close()
        else:
            print("Получено от клиента:", message.decode())
            answer = str("Привет, " + students.setdefault(message.decode()[:-1]) + "!" + "\n").encode()
            print("Приветствие отправлено клиенту\n")
            user_socket.send(answer)
            user_socket.close()

