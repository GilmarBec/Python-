import socket

from src.framework.utils.DefaultProtocol import DefaultProtocol


class UDPClient:
    BUFFER_SIZE = 1024

    __receiver_socket: socket.socket
    __sender_socket: socket.socket
    __receiver_port: int
    __sender_port: int
    __ip: str
    __protocol: DefaultProtocol

    def __init__(
            self, receiver_port: int, sender_port: int, ip: str, port: int,
            protocol: DefaultProtocol = DefaultProtocol()
    ):
        self.__receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__receiver_socket.bind(('0.0.0.0', receiver_port))

        self.__sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__sender_socket.bind(('0.0.0.0', sender_port))
        self.__sender_socket.settimeout(0.1)  # 100ms

        self.__receiver_port = receiver_port
        self.__sender_port = sender_port
        self.__ip = ip
        self.__protocol = protocol

    #  This application send the message to the ip on the same receiver port as a pattern
    def send(self, message: str, port: int = None):
        if port is None:
            port = self.__receiver_port

        self.__sender_socket.sendto(self.__protocol.encode(message=message), (self.__ip, port))

    def receive(self) -> str:
        encoded_message, from_address = self.__receiver_socket.recvfrom(self.BUFFER_SIZE)
        message = self.__protocol.decode(encoded_message)

        return message
