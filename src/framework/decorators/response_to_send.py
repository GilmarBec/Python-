from src.framework.utils import UDPClient


def response_to_send(client: UDPClient, port: int):
    def wrapper(func):
        def send_and_return(*args, **kwargs):
            res = func(*args, **kwargs)
            client.send(res, port)
            return func(*args, **kwargs)
        return send_and_return
    return wrapper
