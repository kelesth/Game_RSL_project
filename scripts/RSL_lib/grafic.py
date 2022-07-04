import os
import win32gui
import win32con
from time import sleep


def get_windows() -> dict:
    """ Get dict with pairs: name of all active (open) windows, and its handle """

    def enum_callback(hwnd, top_windows: dict[int: str]):
        """ Necessary func for working win32gui.GetWindowText correctly """
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


def open_raid_app() -> None:
    """ Open Raid application, move it in standard place """
    raid_place = r'C:\Users\gorpr\OneDrive\Рабочий стол\Raid Shadow Legends.lnk'
    hwnd = get_hwnd('Raid: Shadow Legends')


if __name__ == '__main__':
    os.startfile(r'C:\Users\gorpr\OneDrive\Рабочий стол\Raid Shadow Legends.lnk')
    hwnd1 = get_hwnd('Raid: Shadow Legends')
    print(hwnd1)
    windows = get_windows()
    for pair in windows.items():
        if pair[1] == 'Raid: Shadow Legends':
            print(pair)
