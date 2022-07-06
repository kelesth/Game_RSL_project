from time import sleep
import win32api
import mss
import mss.tools
import os
from typing import Callable


def read_command(com):
    """ Convert string to command """
    def str_to_type(sym: str) -> any:
        """ Convert str to correct type """
        if sym[0] and sym[-1] == '\'':
            return sym[1:-1]
        else:
            return int(sym)

    func = com[:com.index('(')]
    com = com[com.index('(') + 1:-1]
    if com != '':
        args = tuple(map(lambda el: el.replace(' ', ''), com.split(',')))
        args = tuple(map(str_to_type, args))
    else:
        args = None
    return func, args


def get_mouse() -> None:
    """ Give cords of cursor """
    print('You have 10 seconds to move mouse in necessary place')
    sleep(10)
    print('Please hold on yur mouse - getting in process...')
    print('Cursor pos is:', win32api.GetCursorPos())


def get_img(left, top, width, height, name):
    """ Save picture in images/pictures """
    with mss.mss() as sct:
        # Use 1st monitor
        monitor = sct.monitors[1]

        bbox = {'left': left, 'top': top, 'width': width, 'height': height}
        print('You have 3 seconds to open necessary window')
        sleep(3)
        img = sct.grab(bbox)
        path = r"C:\Users\gorpr\PycharmProjects\Game_RSL_project\images\pictures"
        output_path = os.sep.join([path, f"{name}.png"])
        mss.tools.to_png(img.rgb, img.size, output=output_path)

        info_path = os.sep.join([path, "__info__.txt"])
        with open(info_path, 'a') as file:
            file.write(' '.join(map(str, (name, left, top, width, height, '\n'))))

        print('Image has been creating')


if __name__ == '__main__':
    func_dct: dict[str: Callable] = {'get_mouse': get_mouse,
                                     'get_img': get_img}
    while True:
        try:
            command = input('helper.py << ')
            if command == 'help':
                for name in func_dct.keys():
                    print(f'\t{name}: {func_dct[name].__doc__}')
            elif command == '':
                break
            else:
                func_name, func_args = read_command(command)
                if func_args:
                    func_dct[func_name](*func_args)
                else:
                    func_dct[func_name]()
            print()
        except Exception as exc:
            print(exc)
            print('Something wrong\n')
