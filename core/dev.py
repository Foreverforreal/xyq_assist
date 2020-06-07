from pynput import mouse

from core.util import *

handle = get_xyq_handle()


def on_move(x, y):
    print('Pointer moved to {}'.format((x, y)))


def on_click(x, y, button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
    if not pressed:
        return False


def on_scroll(x, y, dx, dy):
    print('scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))


def compute_relative_pos():
    x, y = get_cursor_pos()
    l, t, r, b = get_window_rect(handle)


if __name__ == '__main__':
    with mouse.Listener(no_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()
