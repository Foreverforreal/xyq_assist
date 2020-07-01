import socket

from pynput.keyboard import Key

from core.keyboard_listener import KeyboardListener
from core.mouse_listener import MouseListener
from remote_desktop import encode
from remote_desktop.socket_client import SocketClient

# client = SocketClient('192.168.1.133')
client = SocketClient(socket.gethostname())

listen_keyboard = False


def on_move(x, y):
    client.send(encode('m:{0},{1}&&'.format(x, y)))

def on_click(x, y, button, pressed):
    client.send(encode('c:{0},{1},{2},{3}&&'.format(x, y, button, pressed)))


def on_press(key):
    global listen_keyboard
    t = listen_keyboard

    if key == Key.esc:
        listen_keyboard = (not t)
    else:
        if listen_keyboard:
            if hasattr(key, 'name'):
                print(key.name)
                client.send(encode('p:{0}&&'.format(key.name)))
            elif hasattr(key, 'char'):
                print(key.char)
                client.send(encode('p:{0}&&'.format(key.char)))
            elif hasattr(key, 'vk'):
                client.send(encode('pvk:{0}&&'.format(key.vk)))

def on_release(key):
    global listen_keyboard
    t = listen_keyboard

    if key == Key.esc:
        listen_keyboard = (not t)
    else:
        if listen_keyboard:
            if hasattr(key, 'name'):
                client.send(encode('r:{0}&&'.format(key.name)))
            elif hasattr(key, 'char'):
                client.send(encode('r:{0}&&'.format(key.char)))
            elif hasattr(key, 'vk'):
                client.send(encode('rk:{0}&&'.format(key.vk)))



if __name__ == '__main__':
    # mouse_listener = MouseListener(on_move, on_click)
    # mouse_listener.join()

    keyboard_listener = KeyboardListener(on_press)
    keyboard_listener.join()
