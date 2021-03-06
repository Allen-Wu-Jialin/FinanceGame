from drawable import Drawable
from pygame_functions import *


class Player(Drawable):
    def __init__(self):
        super().__init__(sprite=makeSprite("personSprite.png"))

        # Range goes from 0-100 for every stat except money
        self.__happiness = 100
        self.__money = 500
        self.__hunger = 100
        self.__fitness = 100
        self.__fatigue = 0
        self.__location = "outside"

    def set_location(self, location):
        self.__location = location

    def increase_money(self, money_amount):
        self.__money += money_amount

    def increase_hunger(self, hunger_amount):
        self.__hunger += hunger_amount

    def increase_fitness(self, fitness_amount):
        self.__fitness += fitness_amount

    def increase_fatigue(self, fatigue_amount):
        self.__fatigue += fatigue_amount

    def get_location(self):
        return self.__location

    def get_hunger(self):
        return self.__hunger

    def get_fitness(self):
        return self.__fitness

    def get_fatigue(self):
        return self.__fatigue

    def get_happiness(self):
        return self.__happiness

    def draw(self):
        moveSprite(self.get_sprite(), self.get_x_position(), self.get_y_position())
