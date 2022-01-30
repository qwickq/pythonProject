import time

from pygame import *
from random import randint as rnd

# Константы для игры
SCREEN_LENGTH = 1920  # Длина экрана
SCREEN_WIDTH = 1020  # Ширина экрана
SNAKE_LENGTH = 25  # Длина змеи
SNAKE_WIDTH = 20  # Ширина змеи
LAND = Rect(0, 0, SCREEN_LENGTH, SCREEN_WIDTH)
SPEED = 2.5  # Скорости змеи
# Начальная прорисовка игры, создание поля
init()
display.set_caption("Snake")
screen = display.set_mode([SCREEN_LENGTH, SCREEN_WIDTH])
clock = time.Clock()

# Глобальные переменные
change_x = SPEED
change_y = 0


class Food:  # Класс ,,Еда''
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


class BodySnake:  # Класс ,,Змея''
    def __init__(self, length, width, speed, x, y):
        self.length = length
        self.width = width
        self.speed = speed
        self.x = x
        self.y = y

    def appearance(self):
        draw.rect(screen, "#ff00ff", Rect(self.x, self.y, self.length, self.width))

    def move(self):  # Создаём функцию ,,move''
        global change_x, change_y
        self.x += change_x
        self.y += change_y


# голова змеи
head_snake = BodySnake(SNAKE_LENGTH, SNAKE_WIDTH, SPEED, rnd(4 * SNAKE_LENGTH, int(SCREEN_LENGTH * 0.95)),
                       rnd(SNAKE_WIDTH // 2, SCREEN_WIDTH - SNAKE_WIDTH // 2))

snake = [head_snake, BodySnake(SNAKE_LENGTH, SNAKE_WIDTH, SPEED, head_snake.x - SNAKE_LENGTH, head_snake.y),
         BodySnake(SNAKE_LENGTH, SNAKE_WIDTH, SPEED, head_snake.x - SNAKE_LENGTH * 2, head_snake.y)]


def grow():
    """рост змеи"""
    if snake[-1].length == SNAKE_LENGTH:  # Если хвост змейки - квадрат
        snake.append(BodySnake(SNAKE_LENGTH / 2, SNAKE_WIDTH, SPEED, snake[-1].x - snake[-1].length // 2,
                               snake[-1].y))  # добавляем новый полуквадрат (вырастит после следующего поедания пищи)
    else:  # если хвост змейки - полуквадрат
        snake[-1].x -= snake[-1].length
        snake[-1].length *= 2  # увеличиваем длину, чтобы хвост стал тоже квадратом


play = True
while play:
    for x in event.get():
        if x.type == QUIT:
            play = False

    # выход за пределы экрана
    if snake[0].x + snake[0].length // 2 > SCREEN_LENGTH or snake[0].y + snake[0].width // 2 > SCREEN_WIDTH \
            or snake[0].x - snake[0].length // 2 < 0 or snake[0].y - snake[0].width // 2 < 0:
        play = False

    chg_drct()

    if food.side / 2 + food.x > snake[0].x > food.x - food.side / 2 and food.side / 2 + food.y > snake[0].y > food.y - food.side / 2:
        food = Food(SNAKE_LENGTH, "apple")
        grow()

    draw.rect(screen, (11, 102, 35), LAND)
    food.appearance()
    for i in range(len(snake)):
        snake[i].appearance()
        snake[i].move()
    display.update()
    clock.tick(75)
