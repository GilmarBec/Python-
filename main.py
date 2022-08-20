from src.framework.internal.socket_listener import SocketListener
from src.framework.utils import UDPClient

ip, src_port, dest_port = ['191.245.89.219', 50002, 50001]

client = UDPClient(receiver_port=src_port, sender_port=dest_port, ip=ip)
listener = SocketListener(client)
listener.start()

while True:
    msg = input('> ')
    client.send(msg)
