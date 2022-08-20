from src.framework.internal.socket_listener import SocketListener
from src.framework.utils import UDPClient


def start(src_port, dest_port, ip, port):
    client = UDPClient(receiver_port=src_port, sender_port=dest_port, ip=ip, port=port)
    listener = SocketListener(client).start()

    return client


def default_send():
    return input('> ')
