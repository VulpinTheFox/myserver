import socket




sock = socket.socket()

print("Соединение с сервером")
sock.connect(('localhost', 9090))
print("Введите сообщение")
str = input()

print("Отправка данных серверу")
sock.send(str.encode('utf-8'))

print("Прием данных серверу")
data = sock.recv(1024)

print(data.decode('utf-8'))

print("Разрыв соединения с сервером")
sock.close()