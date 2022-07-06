from RSL_lib import grafic
from RSL_lib import windows
from RSL_lib import classes
from time import sleep


if __name__ == '__main__':
    raid_hwnd = 0
    for pair in windows.get_windows().items():
        if pair[1] == 'Raid: Shadow Legends':
            raid_hwnd = pair[0]
            break
    else:
        print('Raid window not found')
        exit(0)
    while True:
        kind = grafic.check_menu()
        if kind == 'afm':
            menu = classes.create_afm()
            windows.click(*menu.get_button('ab').cords, raid_hwnd)
        sleep(1)
