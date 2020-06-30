import socket

class SocketClient:
    def __init__(self, host, port=12345):
        s = socket.socket()  # 创建 socket 对象
        s.connect((host, port))
        self.socket = s

    def send(self, data):
        self.socket.send(data)




if __name__ == '__main__':
    client = SocketClient(socket.gethostname())
    client.send(b'10011')