from src.framework.utils import AbstractListener, UDPClient


class SocketListener(AbstractListener):
    __client: UDPClient

    def __init__(self, client: UDPClient):
        super(SocketListener, self).__init__()
        self.__client = client

    def _run(self):
        while True:
            data = self.__client.receive()
            # print('\nDATA:', data, '\n')
            if data != '':
                print(f'\rnode: {data}\n> ')
