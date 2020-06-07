import sys
from random import random

import win32api
import time

import win32con
import win32gui
import win32print
from PIL import ImageGrab

from core import screen_scale_rate

debug = True


def move_click(x, y, t=0):  # 移动鼠标并点击左键
    win32api.SetCursorPos((x, y))  # 设置鼠标位置(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
                         win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)  # 点击鼠标左键
    if t == 0:
        time.sleep(random.random() * 2 + 1)  # sleep一下
    else:
        time.sleep(t)
    return 0


def get_cursor_pos():
    return win32api.GetCursorPos()



def get_xyq_handle():
    # wd_name = u'梦幻西游 - 星云引擎'
    wd_name = u'test.txt - 记事本'
    return win32gui.FindWindow(0, wd_name)  # 获取窗口句柄


def get_window_rect(handle):  # 获取阴阳师窗口信息
    if handle == 0:
        # text.insert('end', '小轩提示：请打开PC端阴阳师\n')
        # text.see('end')  # 自动显示底部
        return None
    else:
        (left, top, right, bottom) = win32gui.GetWindowRect(handle)
        if debug:
            print('原始rect: {}'.format((left, top, right, bottom)))
        return left, top, right, bottom


def test_wd_rect():
    handle = get_xyq_handle()
    while True:
        get_window_rect(handle)
        time.sleep(1)


def real_rect(rect: tuple):
    return (int(i * screen_scale_rate) for i in rect)


def screen_cut():
    rect = get_window_rect(get_xyq_handle())
    rect = real_rect(rect)
    print(rect)
    image: ImageGrab.Image = ImageGrab.grab(rect)
    image.save(open(r"C:\Users\49948\Desktop\a.jpg", 'w'))

if __name__ == '__main__':
    screen_cut()

