import mss
import mss.tools
import cv2
import os
from time import sleep, time
import numpy as np


def get_img(left, top, width, height) -> None:
    """ Save picture in temp """
    with mss.mss() as sct:
        # Use 1st monitor
        monitor = sct.monitors[1]

        bbox = {'left': left, 'top': top, 'width': width, 'height': height}
        img = sct.grab(bbox)
        path = r"C:\Users\gorpr\PycharmProjects\Game_RSL_project\images\temp\temp.png"
        mss.tools.to_png(img.rgb, img.size, output=path)


def is_same(image_1, image_2) -> False:
    """ Check comparing of images"""
    image_1 = np.matrix(image_1)
    image_2 = np.matrix(image_2)
    if np.allclose(image_1, image_2):
        return True
    return False


def check_afm():
    """ Check if current menu is after fight menu """
    get_img(795, 645, 205, 35)
    sample_path = r'C:\\Users\\gorpr\\PycharmProjects\\Game_RSL_project\\images\\pictures\\change_heroes_button.png'
    cur_path = r'C:\\Users\\gorpr\\PycharmProjects\\Game_RSL_project\\images\\temp\\temp.png'
    sample_img = cv2.imread(sample_path, cv2.IMREAD_GRAYSCALE)
    cur_img = cv2.imread(cur_path, cv2.IMREAD_GRAYSCALE)
    if is_same(sample_img, cur_img):
        return True


def check_menu() -> str:
    """ Check, which menu enter on the screen now """
    start = time()
    if check_afm():
        print('time:', time() - start)
        print('\tAFM menu was founded')
        return 'afm'
    else:
        return ''


if __name__ == '__main__':
    print(check_menu())
