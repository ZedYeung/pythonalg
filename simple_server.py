import socket

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)
while True:
    client, addr = s.accept()
    print('get connection from', addr)
    client.send('Thank you for connecting')
    client.close





