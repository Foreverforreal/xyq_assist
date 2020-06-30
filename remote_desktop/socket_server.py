import socket


class SocketServer:
    def __init__(self, port=12345):
        s = socket.socket()  # 创建 socket 对象
        host = socket.gethostname()  # 获取本地主机名
        s.bind((host, port))  # 绑定端口
        self.socket = s

    def listen(self, callback):
        self.socket.listen(5)  # 等待客户端连接
        c, addr = self.socket.accept()  # 建立客户端连接
        print('连接地址：', addr)

        while True:
            data = c.recv(1024)
            if len(data) > 0:
                callback(c, data)



if __name__ == '__main__':
    server = SocketServer()
    server.listen()
