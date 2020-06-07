from pynput import mouse

from core.util import *

handle = get_xyq_handle()

from pynput import mouse


def on_move(x, y):
    print('Pointer moved to {0}'.format((x, y)))


def on_click(x, y, button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
    if not pressed:
        # Stop listener
        return False


def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))


def compute_relative_pos(x, y, button, pressed):
    l, t, r, b = get_window_rect(handle)
    print('相对窗口x坐标: ' + str(x - l))
    print('相对窗口y坐标: ' + str(y - t))
    if not pressed:
        return False


if __name__ == '__main__':
    # listener = mouse.Listener(
    #     on_move=on_move,
    #     on_click=on_click,
    #     on_scroll=on_scroll)
    # listener.start()

    with mouse.Listener(
            on_move=on_move,
            on_click=compute_relative_pos,
            on_scroll=on_scroll) as listener:
        listener.join()
