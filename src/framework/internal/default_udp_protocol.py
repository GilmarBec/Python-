from src.framework.utils.DefaultProtocol import DefaultProtocol


class DefaultUDPProtocol(DefaultProtocol):
    def encode(self, message: str):
        return message.encode()

    def decode(self, message: str):
        return message
