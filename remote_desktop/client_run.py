import socket
import time

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
    if key == Key.esc:
        listen_keyboard = not listen_keyboard

    if listen_keyboard:
        client.send(encode('p:{0}&&'.format(key)))


if __name__ == '__main__':
    mouse_listener = MouseListener(on_move, on_click)
    mouse_listener.join()

    keyboard_listener = KeyboardListener(on_press)
    keyboard_listener.join()
