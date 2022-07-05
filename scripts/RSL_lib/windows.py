import os
import win32gui
import win32con
import win32api
from time import sleep


def get_windows() -> dict:
    """ Get dict with pairs: name of all active (open) windows, and its handle """

    def enum_callback(hwnd, top_windows: dict[int: str]):
        """ Necessary func for working win32gui.EnumWindows() correctly """
        top_windows[hwnd] = win32gui.GetWindowText(hwnd)

    top_windows_loc = dict()
    win32gui.EnumWindows(enum_callback, top_windows_loc)
    return top_windows_loc


def get_hwnd(title: str) -> int:
    """ Search window's handle by its name (title)
        !Use only if sure that this window must be open yet! """

    top_windows = get_windows()
    print('Opening in process...')
    while not(title in top_windows.values()):
        sleep(1)
        top_windows = get_windows()

    for hwnd, name in top_windows.items():
        if name == title:
            print('Opening completed\n')
            return hwnd


def convert_window_pos(hwnd):
    """ Convert window position from GetWindowRect to format (left_top_angle_x, left_top_angle_y, weigh, high) """
    sleep(0.5)
    left_top_angle_x, left_top_angle_y, right, bottom = win32gui.GetWindowRect(hwnd)
    high = bottom - left_top_angle_y
    weigh = right - left_top_angle_x
    position = (left_top_angle_x, left_top_angle_y, weigh, high)
    return position


def resize_window(hwnd, pos):
    """ Change window pose/size """
    new_pos = None

    while not(new_pos == pos):
        new_pos = convert_window_pos(hwnd)
        win32gui.MoveWindow(hwnd, *pos, True)
        sleep(0.5)


def open_raid_app(position: tuple = (-8, 0, 1280, 751)) -> None:
    """ Open Raid application, move it in standard place """

    raid_path = r'C:\Users\gorpr\OneDrive\Рабочий стол\Raid Shadow Legends.lnk'
    os.startfile(raid_path)
    hwnd = get_hwnd('Raid: Shadow Legends')
    win32gui.SetForegroundWindow(hwnd)
    resize_window(hwnd, position)


def click(x: int, y: int, hwnd) -> None:
    """ Click in given cords with moving cursor """
    if not (check_if_foreground(hwnd)):
        win32gui.SetForegroundWindow(hwnd)

    win32api.SetCursorPos((x, y))
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, win32api.MAKELONG(x, y))
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, win32api.MAKELONG(x, y))


def check_if_foreground(hwnd) -> bool:
    """ Check if current window is foreground """
    if win32gui.GetForegroundWindow() == hwnd:
        return True
    return False


if __name__ == '__main__':
    hwnd1 = 0
    open_raid_app()
    for pair in get_windows().items():
        if pair[1] == 'Raid: Shadow Legends':
            hwnd1 = pair[0]
    print(hwnd1)
    sleep(10)
    click(1098, 656, hwnd1)
