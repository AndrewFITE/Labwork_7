import socket

print("Соединение установлено! Ожидается подключение клиента...")
students = {"Окороков": "Андрей", "Коросткин": "Антон", "Казанкин": "Максим", "Чумаков": "Матвей"}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1', 12345))

while True:
    message, address = server_socket.recvfrom(4096)
    print("Адрес подключенного клиента:", address)
    enter_surname = "Введите фамилию студента: ".encode()
    server_socket.sendto(enter_surname, address)
    message, address = server_socket.recvfrom(4096)
    if students.get(message.decode().strip()) == None:
        error = str("Error! Фамилия студента отсутствует в списке студентов вашей группы!\n").encode()
        print("Сообщение об ошибке отправлено клиенту\n")
        server_socket.sendto(error, address)
    else:
        print("Получено от клиента:", message.decode())
        answer = str("Привет, " + students.get(message.decode().strip()) + "!\n").encode()
        print("Приветствие отправлено клиенту!\n")
        server_socket.sendto(answer, address)
