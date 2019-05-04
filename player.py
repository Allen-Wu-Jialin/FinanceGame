from drawable import Drawable
from pygame_functions import *


class Player(Drawable):
    def __init__(self):
        super(Drawable, self).__init__()

        # Range goes from 0-100 for every stat except money
        self.__happiness = 100
        self.__money = 500
        self.__hunger = 100
        self.__fitness = 100
        self.__fatigue = 0

    def increase_money(self, money_amount):
        self.__money += money_amount

    def increase_hunger(self, hunger_amount):
        self.__hunger += hunger_amount

    def increase_fitness(self, fitness_amount):
        self.__fitness += fitness_amount

    def increase_fatigue(self, fatigue_amount):
        self.__fatigue += fatigue_amount

    def draw(self):
        person = makeSprite("personSprite.png")
        showSprite(person)
        moveSprite(person, self.get_x_position(), self.get_y_position())