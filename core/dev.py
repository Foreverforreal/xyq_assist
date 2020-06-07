from pynput import mouse, keyboard
from pynput.keyboard import Key, KeyCode

from core import menu_list
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


def on_press(key):
    # 监听按键
    print('{0} pressed'.format(key))


def on_release(key):
    # 监听释放
    print('{0} release'.format(key))
    if key == Key.esc:
        # Stop listener
        return False


def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))


i = 0


def compute_relative_pos(key: KeyCode):
    global i
    if hasattr(key, 'char') and 'd' == key.char:
        x, y = get_cursor_pos()
        l, t, r, b = get_window_rect(handle)

        offset_x = str(x - l)
        offset_y = str(y - t)
        print('相对窗口x坐标: ' + str(x - l))
        print('相对窗口y坐标: ' + str(y - t))
        with open('../menu.txt', 'wa') as file:
            file.write("{}:{} {}".format(menu_list[i], offset_x, offset_y))
            i = i + 1


if __name__ == '__main__':
    # listener = mouse.Listener(
    #     on_move=on_move,
    #     on_click=on_click,
    #     on_scroll=on_scroll)
    # listener.start()

    # with mouse.Listener(
    #     # on_move= on_move,
    #         on_click=compute_relative_pos,
    #         on_scroll=on_scroll) as listener:
    #     listener.join()

    # 连接事件以及释放
    with keyboard.Listener(
            on_press=compute_relative_pos,
            # on_release=on_release
    ) as listener:
        listener.join()
