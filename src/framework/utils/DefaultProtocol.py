class DefaultProtocol:
    def encode(self, message: str):
        return message.encode()

    def decode(self, message: any):
        return message.decode()
