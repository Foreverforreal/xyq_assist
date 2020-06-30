import socket

from core.mouse_listener import MouseListener
from remote_desktop import encode
from remote_desktop.socket_client import SocketClient

client = SocketClient(socket.gethostname())


def on_move(x, y):
    client.send(encode('m:{0},{1}'.format(x, y)))


def on_click(x, y, button, pressed):
    client.send(encode('c:{0},{1},{2},{3}'.format(x, y, button, pressed)))

if __name__ == '__main__':
    mouse_listener = MouseListener(on_move, on_click)
    mouse_listener.join()
