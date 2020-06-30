from pynput import keyboard
from pynput.keyboard import Key


def print_on_press(key):
    # 监听按键
    print('{0} pressed'.format(key))


def print_on_release(key):
    # 监听释放
    print('{0} release'.format(key))
    if key == Key.esc:
        # Stop listener
        return False


class KeyboardListener:
    def __init__(self, on_press=print_on_press, on_release=print_on_release):
        self.listener = keyboard.Listener(
            on_press=on_press,
            on_release=on_release
        )
        self.listener.start()

    def join(self):
        self.listener.join()

if __name__ == '__main__':
    listener = KeyboardListener()
    listener.join()
