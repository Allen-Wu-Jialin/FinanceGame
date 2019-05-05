#This will create several classes with bars that update over time.
from drawable import Drawable
from pygame_functions import *
import abc

# This is Jiongheng. I wrote the code to display bars. They should update automatically
# if you change any of the player's stats during runtime.
# I can't make it tomorrow because I have to study for my comp ethics midterm, sorry
# I can still code some stuff if you want me to tho

class bar(Drawable):
    def __init__(self, color, xPos, yPos):
        super().__init__(xPos, yPos)
        self.__color = color
        self.__percent = 100

    def set_percentage(self, percent):
        # Note: Percentage is in decimals (0 to 1)
        self.__percent = percent

    def draw(self):
        """
        Draws a red bar and another bar of a different color on top of the red bar
        :return:
        """
        drawRect(self.get_x_position(), self.get_y_position(), 100, 10, (255, 0, 0))
        drawRect(self.get_x_position(), self.get_y_position(), 100 * self.__percent, 10, self.__color)

class playerbar(bar, metaclass=abc.ABCMeta):
    def __init__(self, player, color, xPos, yPos):
        super().__init__(color, xPos, yPos)
        self.__player = player

    def get_player(self):
        return self.__player

    @abc.abstractmethod
    def update(self):
        pass

class hunger(playerbar):
    def __init__(self, player, xPos, yPos):
        super().__init__(player, (255, 127, 0), xPos, yPos)

    def update(self):
        self.set_percentage(self.get_player().get_hunger() / 100.0)

class happiness(playerbar):
    def __init__(self, player, xPos, yPos):
        super().__init__(player, (255, 192, 203), xPos, yPos)

    def update(self):
        self.set_percentage(self.get_player().get_happiness() / 100.0)

class fatigue(playerbar):
    def __init__(self, player, xPos, yPos):
        super().__init__(player, (165,42,42), xPos, yPos)

    def update(self):
        self.set_percentage(self.get_player().get_fatigue() / 100.0)

class fitness(playerbar):
    def __init__(self, player, xPos, yPos):
        super().__init__(player, (0, 255, 0), xPos, yPos)

    def update(self):
        self.set_percentage(self.get_player().get_fitness() / 100.0)