import win32api
import win32con

from remote_desktop import decode
from remote_desktop.socket_server import SocketServer


def execute(socket, data):
    mes = str(data, encoding='utf-8')
    action, d = decode(mes)
    if action == 'm':
        position = [int(p) for p in d.split(',')]
        print(position)
        # win32api.SetCursorPos(position)  # 设置鼠标位置(x, y)
    elif action == 'c':
        [x, y, button, pressed] = d.split(',')
        if pressed == 'True':
            win32api.SetCursorPos((x, y))  # 设置鼠标位置(x, y)
            if button == 'Button.left':
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)  # 点击鼠标左键
            elif button == 'Button.right':
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN | win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)  # 点击鼠标左键



if __name__ == '__main__':
    server = SocketServer()
    server.listen(execute)