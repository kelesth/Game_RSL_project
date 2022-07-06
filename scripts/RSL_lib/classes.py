class Object:
    """ class have info about some object on screen"""

    def __init__(self, cords):
        self.cords = cords


class Menu:
    """ class have an information about some menu (some special screen)"""

    def __init__(self, buttons, objects):
        self._buttons: dict[str: Object] = buttons
        self._objects: dict[str: Object] = objects

    def get_button(self, name) -> Object:
        """ give info about button by name """
        try:
            return self._buttons[name]
        except KeyError:
            print('Wrong button Key given:', name)


def create_afm() -> Menu:
    """ Create dungeon after fighting menu """
    change_heroes_button = Object((900, 675))
    again_button = Object((670, 671))
    continue_button = Object((1131, 675))
    buttons = {'chb': change_heroes_button, 'ab': again_button, 'cb': continue_button}
    objects = {}
    return Menu(buttons, objects)
