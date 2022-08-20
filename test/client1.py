from src.framework.decorators.response_to_send import response_to_send
from test.common.common import default_send, start

ip, src_port, dest_port = ['127.0.0.1', 50002, 50001]
client = start(src_port=src_port, dest_port=dest_port, ip=ip, port=50003)


@response_to_send(client, 50003)
def send():
    return default_send()


while True:
    send()
