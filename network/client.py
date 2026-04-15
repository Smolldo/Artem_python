import socket
# import time

# client = socket.socket()
# client.connect(('127.0.0.1', 8888))

# msg = 'HELLO_WORLD'

# for char in msg:
#     client.send(char.encode())
#     print(char)
#     time.sleep(.2)

# client.close()

# client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# while True:
#     msg = input('Введи повідомлення: ')
#     client.sendto(msg.encode(), ('127.0.0.1', 9999))


import threading

MY_PORT = 9998
TARGET_IP = input('IP Співрозмовника: ')
TARGET_PORT = 9999

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
    

    