import random

display_width = 800
display_height = 600


class Player:

    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed


class Ball:

    def __init__(self, x, y, width, height, speed_x, speed_y):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed_x = random.choice(speed_x)
        self.speed_y = speed_y


class Enemy:

    def __init__(self, x, y, dead):
        if dead is False:
            self.x = x
            self.y = y
            self.width = 90
            self.height = 25
            self.dead = dead

        if dead is True:
            self.width = 0
            self.height = 0
            self.dead = dead

# List where all the enemies are stored
enemy_list = []


# Easy way of making multiple enemies without hard coding
def make_enemy1(number):

    for i in range(0, number):

        i = Enemy(20 + display_width * 0.12 * i,
                  display_height * 0.27,
                  False)
        enemy_list.append(i)


def make_enemy2(number):

    for i in range(0, number):

        i = Enemy(20 + display_width * 0.12 * i,
                  display_height * 0.22,
                  False)
        enemy_list.append(i)


def make_enemy3(number):

    for i in range(0, number):

        i = Enemy(20 + display_width * 0.12 * i,
                  display_height * 0.17,
                  False)
        enemy_list.append(i)


def make_enemy4(number):

    for i in range(0, number):

        i = Enemy(20 + display_width * 0.12 * i,
                  display_height * 0.12,
                  False)
        enemy_list.append(i)


def make_enemy5(number):

    for i in range(0, number):

        i = Enemy(20 + display_width * 0.12 * i,
                  display_height * 0.07,
                  False)
        enemy_list.append(i)


def make_enemy6(number):

    for i in range(0, number):

        i = Enemy(20 + display_width * 0.12 * i,
                  display_height * 0.02,
                  False)
        enemy_list.append(i)
