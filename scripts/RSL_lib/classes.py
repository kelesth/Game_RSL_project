class Object:
    """ class have info about some object on screen"""

    def __init__(self, cords):
        self.cords = cords


class Menu:
    """ class have an information about some menu (some special screen)"""

    def __init__(self, buttons, objects):
        self._buttons: dict[str: Object] = buttons
        self._objects: dict[str: Object] = objects

    def get_button(self, name):
        """ give info about button by name """
        try:
            return self._buttons[name]
        except KeyError:
            print('Wrong button Key given:', name)


def create_dfm() -> Menu:
    """ Create dungeon fighting menu """

