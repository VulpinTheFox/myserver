import socket



sock = socket.socket()

print("Запуск сервера")

sock.bind(('', 9090))

print("Начало прослушивания порта")

sock.listen(1)
conn, addr = sock.accept()
print("Подключение клиента")

try:
	while True:
		print("Прием данных от клиента")
		data = conn.recv(1024)
		if not data:
			break
		conn.send(data.upper())
		print("Отправка данных клиенту")

except Exception as e:
	print("Что-то пошло не так")


print("Отключение клиента")
conn.close()

print("Отключение сервера")