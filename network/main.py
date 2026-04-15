import socket

# server = socket.socket()
# server.bind(('0.0.0.0', 8888))
# server.listen()

# client, _ = server.accept()

# data = b""
# while True:
#     chunk = client.recv(4)
#     if not chunk:
#         break
#     data+= chunk
# print(f'Recieved: {data.decode()}')


# server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server.bind(('0.0.0.0', 9999))

# print('UPD сервер запущено')

# while True:
#     data, addr = server.recvfrom(1024)
#     print(f'Від {addr}: {data.decode()}')

import threading

MY_PORT = 9999
TARGET_IP = input('IP Співрозмовника: ')
TARGET_PORT = 9998

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', MY_PORT))

print('Чат запущено')

def recieve():
    while True:
        data, addr = sock.recvfrom(1024)
        print(f'\n[{addr}] {data.decode()}')

threading.Thread(target=recieve, daemon=True).start()

while True:
    msg = input('ТИ: ')
    sock.sendto(msg.encode(), (TARGET_IP, TARGET_PORT))
    