from src.framework.utils import UDPClient


class DefaultUDPClient(UDPClient):
    def __init__(self, receiver_port: int, sender_port: int, ip: str):
        super(DefaultUDPClient, self).__init__(sender_port=sender_port, receiver_port=receiver_port, )

    def send(self, message: any):

        super(DefaultUDPClient, self).send(message)
