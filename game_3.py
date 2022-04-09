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


class Food:  # создаём класс ,,Food" для внутриигрового увеличения змеи
    """Класс еды"""
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
    """ изменение направления головы змеи """
    if snake[0].increase_reset >= snake[0].min_distance_to_rotate:
        if key.get_pressed()[key.key_code("w")] and snake[0].direction != 's':
            snake[0].direction = 'w'  # up

        if key.get_pressed()[key.key_code("d")] and snake[0].direction != 'a':
            snake[0].direction = 'd'  # right

        if key.get_pressed()[key.key_code("s")] and snake[0].direction != 'w':
            snake[0].direction = 's'  # down

        if key.get_pressed()[key.key_code("a")] and snake[0].direction != 'd':
            snake[0].direction = 'a'  # left
    snake[0].increase_reset += SPEED  # увеличение пройденого расстояния после поворота у ГОЛОВЫ змеи


class BodySnake:  # Класс ,,Змея'' # создаем класс BodySnake - тело змеи
    def __init__(self, length, width, speed, x, y):
        self.length = length
        self.width = width
        self.speed = speed
        self.x = x
        self.y = y
        self.increase_reset = 0  # увеличивается пока не поворачиваем // актуальное пройденное расстояние после поворота
        self.min_distance_to_rotate = self.width  # проверяет, что надо поворачиваться или (только для головы) можно поворачивать
        self.direction = 'd'

    def appearance(self):
        draw.rect(screen, "#ff00ff", Rect(self.x, self.y, self.length, self.width))

    def move(self):  # Создаём функцию ,,move'' для движении змеи
        if self.direction == 'w':
            self.y -= SPEED
        if self.direction == 's':
            self.y += SPEED
        if self.direction == 'd':
            self.x += SPEED
        if self.direction == 'a':
            self.x -= SPEED


def move_body_snake():
    """Поворачиваем тело змеи, кроме головы"""
    global snake
    for i in range(1,len(snake)):



# голова змеи
head_snake = BodySnake(SNAKE_LENGTH, SNAKE_WIDTH, SPEED, rnd(4 * SNAKE_LENGTH, int(SCREEN_LENGTH * 0.95)),
                       rnd(SNAKE_WIDTH // 2, SCREEN_WIDTH - SNAKE_WIDTH // 2))

snake = [head_snake, BodySnake(SNAKE_LENGTH, SNAKE_WIDTH, SPEED, head_snake.x - SNAKE_LENGTH, head_snake.y),
         BodySnake(SNAKE_LENGTH, SNAKE_WIDTH, SPEED, head_snake.x - SNAKE_LENGTH * 2, head_snake.y)]


def grow():
    """увеличение змеи"""
    if snake[-1].length == SNAKE_LENGTH:  # Если хвост змейки - квадрат
        snake.append(BodySnake(SNAKE_LENGTH / 2, SNAKE_WIDTH, SPEED, snake[-1].x - snake[-1].length // 2,
                               snake[-1].y))  # добавляем новый полуквадрат (вырастит после следующего поедания пищи)
    else:  # если хвост змейки - полуквадрат
        snake[-1].x -= snake[-1].length
        snake[-1].length *= 2  # увеличиваем длину, чтобы хвост стал тоже квадратом


play = True
while play:
    for e in event.get():
        if e.type == QUIT:
            play = False

    # выход за пределы экрана
    if snake[0].x + snake[0].length // 2 > SCREEN_LENGTH or snake[0].y + snake[0].width // 2 > SCREEN_WIDTH \
            or snake[0].x - snake[0].length // 2 < 0 or snake[0].y - snake[0].width // 2 < 0:
        play = False

    chg_drct()  # snake[0].direction == snake[1].direction
    move_body_snake()

    if food.side / 2 + food.x > snake[0].x > food.x - food.side / 2 and food.side / 2 + food.y > snake[0].y > food.y - food.side / 2:
        food = Food(SNAKE_LENGTH, "apple")
        grow()

    draw.rect(screen, (11, 102, 35), LAND)
    food.appearance()
    for i in range(len(snake)):  # рисуем и двигаем каждый элемент из списка (каждую часть тела змеи)
        snake[i].move()
        snake[i].appearance()

    display.update()
    clock.tick(75)

display.quit()
