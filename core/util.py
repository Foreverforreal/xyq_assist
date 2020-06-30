import random
import time

import win32api
import win32con
import win32gui
from PIL import ImageGrab

from core import screen_scale_rate, xyq_handle

debug = True

def move_click(x, y, t=0):  # 移动鼠标并点击左键
    win32api.SetCursorPos((x, y))  # 设置鼠标位置(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)  # 点击鼠标左键
    time.sleep(random.random() * 2 + 1)  # sleep一下

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)  # 点击鼠标左键

    if t == 0:
        time.sleep(random.random() * 2 + 1)  # sleep一下
    else:
        time.sleep(t)
    return 0


def get_cursor_pos():
    return win32api.GetCursorPos()


def focus_on_wd(wd_handle):
    win32gui.ShowWindow(wd_handle, win32con.SW_NORMAL)
    win32gui.SetActiveWindow(wd_handle)
    win32gui.SetForegroundWindow(wd_handle)
    time.sleep(0.2)


def get_window_rect(handle):  # 获取阴阳师窗口信息
    if handle == 0:
        return None
    else:
        (left, top, right, bottom) = win32gui.GetWindowRect(handle)
        if debug:
            print('原始rect: {}'.format((left, top, right, bottom)))
        return left, top, right, bottom


def test_wd_rect():
    while True:
        get_window_rect(xyq_handle)
        time.sleep(1)


def real_rect(rect: tuple):
    return (int(i * screen_scale_rate) for i in rect)


def screen_cut(wd_handle):
    focus_on_wd(wd_handle)

    rect = get_window_rect(wd_handle)
    rect = real_rect(rect)
    print(rect)
    image: ImageGrab.Image = ImageGrab.grab(rect)
    with open(r"C:\Users\49948\Desktop\a.jpg", 'w') as file:
        image.save(file)


def click_menu(handle, menu: str):
    focus_on_wd(handle)

    rect = get_window_rect(handle)
    with open('../menu.txt', 'r') as file:
        while (m := file.readline()) != '':
            if m.startswith(menu):
                coord = m[len(menu) + 1:].replace('\n', '')
                x, y = coord.split(' ')
                click_x = rect[0] + int(x)
                click_y = rect[1] + int(y)
                print('click position: {} {}'.format(click_x, click_y))

                move_click(click_x, click_y)


if __name__ == '__main__':
    screen_cut(xyq_handle)
