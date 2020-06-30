from pynput.keyboard import Key

from core.keyboard_listener import KeyboardListener
from core.mouse_listener import MouseListener
from remote_desktop import encode
from remote_desktop.socket_client import SocketClient

client = SocketClient('192.168.1.133')

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
                client.send(encode('p:{0}&&'.format(key.name)))
            elif hasattr(key, 'char'):
                client.send(encode('p:{0}&&'.format(key.char)))

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


if __name__ == '__main__':
    # mouse_listener = MouseListener(on_move, on_click)
    # mouse_listener.join()

    keyboard_listener = KeyboardListener(on_press, on_release)
    keyboard_listener.join()
