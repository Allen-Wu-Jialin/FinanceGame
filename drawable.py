import abc
from pygame_functions import *


class Drawable(metaclass=abc.ABCMeta):
    def __init__(self, x=0, y=0, sprite=None):
        self.__sprite = sprite
        if self.__sprite is not None:
            showSprite(self.__sprite)

        self.__x_coord = x
        self.__y_coord = y

    def set_coord(self, x, y):
        self.__x_coord = x
        self.__y_coord = y

    def set_x_position(self, x):
        self.__x_coord = x

    def set_y_position(self, y):
        self.__y_coord = y

    def get_sprite(self):
        return self.__sprite

    def get_coord(self):
        return self.__x_coord, self.__y_coord

    def get_x_position(self):
        return self.__x_coord

    def get_y_position(self):
        return self.__y_coord

    @abc.abstractmethod
    def draw(self):
        pass
