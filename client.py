import socket
import threading

ip, src_port, dest_port = ['192.168.0.15', 50002, 50001]

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

    print('Awaiting Connection')

    while True:
        data = sock.recv(1024).decode()

        print(f'\rasd: {data}\n> ', end='')


listener = threading.Thread(target=listen, daemon=True)
listener.start()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', dest_port))

while True:
    msg = input('> ')
    sock.sendto(str(msg).encode(), (ip, src_port))
