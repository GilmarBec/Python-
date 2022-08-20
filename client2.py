import socket
import threading

ip, src_port, dest_port = ['127.0.0.1', 50001, 50002]

# print('Keep Alive')
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.bind(('0.0.0.0', src_port))
# sock.sendto(b'0', (ip, dest_port))
#
# print('ready to exchange messages\n')

def listen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', src_port))
    sock.sendto(b'0', (ip, dest_port))

    while True:
        data = sock.recv(1024)
        print('\rpeer: {}\n> '.format(data.decode()), end='')


listener = threading.Thread(target=listen, daemon=True)
listener.start()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', dest_port))

while True:
    msg = input('> ')
    sock.sendto(msg.encode(), (ip, src_port))
