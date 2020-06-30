from pynput import mouse, keyboard


def print_on_move(x, y):
    print('Pointer moved to {0}'.format((x, y)))


def print_on_click(x, y, button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
    if not pressed:
        return False


def print_on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))


class MouseListener:
    def __init__(self, on_move=print_on_move, on_click=print_on_click, on_scroll=print_on_scroll):
        self.listener = mouse.Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll)
        self.listener.start()

    def join(self):
        self.listener.join()
