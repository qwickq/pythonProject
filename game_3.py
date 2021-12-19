from pygame import *
from random import randint as rnd

# Начальная прорисовка игры, создание поля
init()
display.set_caption("Snake")
screen = display.set_mode([1920, 1020])
clock = time.Clock()

# константы для игры
START_X = rnd(0, 1500)
START_Y = rnd(0, 1000)
SNAKE_WIDTH = 25
SNAKE_HEIGHT = 25
LAND = Rect(0, 0, 1920, 1020)
SPEED = 2.5

# глобальные переменные
head = Rect(START_X, START_Y, SNAKE_WIDTH, SNAKE_HEIGHT)
change_x = SPEED
change_y = 0


class Food:
    def __init__(self, side, food_type):
        self.side = side
        self.x = rnd(0, 1500)
        self.y = rnd(0, 1000)
        self.type = food_type

    def appearance(self):
        # img = image.load("IMG_3854.jpg").convert()
        # rectangle = img.get_rect()
        draw.rect(screen, [10, 10, 10], Rect(self.x, self.y, self.side, self.side))


food = Food(SNAKE_WIDTH, "ewg")


def move(move_x: type(SPEED), move_y: type(SPEED)) -> None:
    return head.move_ip(move_x, move_y)


def chg_drct() -> None:
    """ создание функции для изменения направления """

    global change_x, change_y
    if key.get_pressed()[key.key_code("w")] and not change_y:
        change_x = 0
        change_y = -SPEED

    if key.get_pressed()[key.key_code("a")] and not change_x:
        change_x = -SPEED
        change_y = 0

    if key.get_pressed()[key.key_code("s")] and not change_y:
        change_x = 0
        change_y = SPEED

    if key.get_pressed()[key.key_code("d")] and not change_x:
        change_x = SPEED
        change_y = 0


play = True
while play:
    for x in event.get():
        if x.type == QUIT:
            play = False
    if head.right > 1920 or head.bottom > 1020 or head.left < 0 or head.top < 0:
        play = False

    chg_drct()

    if (head.x > food.x - food.side / 2 and None):
        food = Food(SNAKE_WIDTH, "dsgvs")

    draw.rect(screen, (11, 102, 35), LAND)
    food.appearance()
    draw.rect(screen, "#ff00ff", head)
    move(change_x, change_y)
    display.update()
    clock.tick(75)