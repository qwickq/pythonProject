from pygame import *
from random import randint as rnd

# Константы для игры
START_X = rnd(0, 1500)
START_Y = rnd(0, 1000)
SCREEN_LENGTH = 1920  # Длина экрана
SCREEN_WIDTH = 1000  # Ширина экрана
SNAKE_WIDTH = 25  # Ширина змеи
SNAKE_HEIGHT = 25  # Высота змеи
LAND = Rect(0, 0, SCREEN_LENGTH, SCREEN_WIDTH)
SPEED = 2.5  # Скорости змеи
# Начальная прорисовка игры, создание поля
init()
display.set_caption("Snake")
screen = display.set_mode([SCREEN_LENGTH, SCREEN_WIDTH])
clock = time.Clock()

# Глобальные переменные
head = Rect(START_X, START_Y, SNAKE_WIDTH, SNAKE_HEIGHT)
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


class Snake:  # Класс ,,Змея''
    def __init__(self, length, width, speed):
        self.length = length
        self.width = width
        self.speed = speed
        self.x = rnd(4 * length, int(SCREEN_LENGTH * 0.95))
        self.y = rnd(width / 2, SCREEN_WIDTH - width / 2)

    def appearance(self):
        draw.rect(screen, "#ff00ff", Rect(self.x, self.y, self.length, self.width))

    def move(self):  # Создаём функцию ,,move''
        global change_x, change_y
        self.x += change_x
        self.y += change_y


snake = Snake(25, 20, SPEED)

play = True
while play:
    for x in event.get():
        if x.type == QUIT:
            play = False
    if snake.x + snake.length // 2 > SCREEN_LENGTH or snake.y + snake.width // 2 > SCREEN_WIDTH or snake.x - snake.length // 2 < 0 or snake.y - snake.width // 2 < 0:
        play = False

    chg_drct()

    if food.side / 2 + food.x > snake.x > food.x - food.side / 2 and food.side / 2 + food.y > snake.y > food.y - food.side / 2:
        food = Food(SNAKE_WIDTH, "apple")

    draw.rect(screen, (11, 102, 35), LAND)
    food.appearance()
    snake.appearance()
    snake.move()
    display.update()
    clock.tick(75)
