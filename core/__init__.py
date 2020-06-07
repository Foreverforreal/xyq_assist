import win32api
import win32con
import win32gui
import win32print


def get_real_resolution():
    """获取真实的分辨率"""
    hDC = win32gui.GetDC(0)
    # 横向分辨率
    w = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
    # 纵向分辨率
    h = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)
    return w, h


def get_screen_size():
    """获取缩放后的分辨率"""
    w = win32api.GetSystemMetrics(0)
    h = win32api.GetSystemMetrics(1)
    return w, h


def compute_screen_scale_rate():
    real_resolution = get_real_resolution()
    screen_size = get_screen_size()
    return round(real_resolution[0] / screen_size[0], 2)


screen_scale_rate = compute_screen_scale_rate()
