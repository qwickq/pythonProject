from pygame import *
from random import randint as rnd, choice

# Константы для игры
SCREEN_LENGTH = 1920  # Длина экрана
SCREEN_WIDTH = 1020  # Ширина экрана
SNAKE_LENGTH = 25  # Длина змеи
SNAKE_WIDTH = 20  # Ширина змеи
LAND = Rect(0, 0, SCREEN_LENGTH, SCREEN_WIDTH)
SPEED_HORIZONTAL = SNAKE_LENGTH / 10  # Скорости змеи
SPEED_VERTICAL = SNAKE_WIDTH / 10

# Начальная прорисовка игры, создание поля
init()
display.set_caption("Snake")
screen = display.set_mode([SCREEN_LENGTH, SCREEN_WIDTH])
clock = time.Clock()


class Food:  # создаём класс ,,Food" для внутриигрового увеличения змеи
    """Класс еды"""

    def __init__(self, side, food_type):
        self.side = side
        self.x = rnd(50, 1400)
        self.y = rnd(50, 900)
        self.type = food_type
        self.img = transform.scale(image.load(choice(["IMG_3854.jpg", "IMG_3855.jpg"])), (self.side, self.side))

    def appearance(self):
        screen.blit(self.img, (self.x, self.y))


food = Food(SNAKE_WIDTH, "ewg")


def chg_drct() -> None:
    """ изменение направления головы змеи """
    if snake[0].increase_reset > snake[0].min_distance_to_rotate:
        if key.get_pressed()[key.key_code("w")] and snake[0].direction != 's':
            snake[0].direction = 'w'  # up
            snake[0].increase_reset = 0

        elif key.get_pressed()[key.key_code("d")] and snake[0].direction != 'a':
            snake[0].direction = 'd'  # right
            snake[0].increase_reset = 0

        elif key.get_pressed()[key.key_code("s")] and snake[0].direction != 'w':
            snake[0].direction = 's'  # down
            snake[0].increase_reset = 0

        elif key.get_pressed()[key.key_code("a")] and snake[0].direction != 'd':
            snake[0].direction = 'a'  # left
            snake[0].increase_reset = 0

    snake[0].increase_reset += SPEED_HORIZONTAL  # увеличение пройденого расстояния после поворота у ГОЛОВЫ змеи


class BodySnake:  # Класс ,,Змея'' # создаем класс BodySnake - тело змеи
    def __init__(self, length, width, x, y):
        self.length = length
        self.width = width
        self.x = x
        self.y = y
        self.increase_reset = 0  # увеличивается пока не поворачиваем // актуальное пройденное расстояние после поворота
        self.min_distance_to_rotate = self.length  # проверяет, что надо поворачиваться или (только для головы) можно
        self.direction = 'd'

    def appearance(self):
        draw.rect(screen, "#ff00ff", Rect(self.x, self.y, self.length, self.width))

    def move(self):  # Создаём функцию ,,move'' для движении змеи
        if self.direction == 'w':
            self.y -= SPEED_VERTICAL
        if self.direction == 's':
            self.y += SPEED_VERTICAL
        if self.direction == 'd':
            self.x += SPEED_HORIZONTAL
        if self.direction == 'a':
            self.x -= SPEED_HORIZONTAL


def move_body_snake():
    """Поворачиваем тело змеи, кроме головы"""
    global snake
    for index in range(1, len(snake)):
        if snake[index].x == snake[index - 1].x or snake[index].y == snake[index - 1].y:
            snake[index].direction = snake[index - 1].direction
        snake[index].move()


# голова змеи
head_snake = BodySnake(SNAKE_LENGTH, SNAKE_WIDTH, rnd(4 * SNAKE_LENGTH, int(SCREEN_LENGTH * 0.90)),
                       rnd(SNAKE_WIDTH // 2, SCREEN_WIDTH - SNAKE_WIDTH))

snake = [head_snake, BodySnake(SNAKE_LENGTH, SNAKE_WIDTH, head_snake.x - SNAKE_LENGTH, head_snake.y),
         BodySnake(SNAKE_LENGTH, SNAKE_WIDTH, head_snake.x - SNAKE_LENGTH * 2, head_snake.y)]


def grow():
    """Увеличение змеи"""
    if snake[-1].length == SNAKE_LENGTH:  # Если хвост змейки - квадрат
        # добавляем новый полуквадрат (вырастит после следующего поедания пищи)
        if snake[-1].direction == 'd':
            snake.append(BodySnake(SNAKE_LENGTH / 2, SNAKE_WIDTH, snake[-1].x - snake[-1].length, snake[-1].y))
        elif snake[-1].direction == 'a':
            snake.append(BodySnake(SNAKE_LENGTH / 2, SNAKE_WIDTH, snake[-1].x + snake[-1].length, snake[-1].y))
        elif snake[-1].direction == 'w':
            snake.append(BodySnake(SNAKE_LENGTH / 2, SNAKE_WIDTH, snake[-1].x, snake[-1].y + snake[-1].width))
        else:
            snake.append(BodySnake(SNAKE_LENGTH / 2, SNAKE_WIDTH, snake[-1].x, snake[-1].y - snake[-1].width))
    else:  # если хвост змейки - полуквадрат
        snake[-1].length *= 2  # увеличиваем длину, чтобы хвост стал тоже квадратом


play = True
while play:
    for e in event.get():
        if e.type == QUIT:
            play = False

    # выход за пределы экрана
    if snake[0].x + snake[0].length // 2 > SCREEN_LENGTH or snake[0].y + snake[0].width // 2 > SCREEN_WIDTH \
            or snake[0].x - snake[0].length // 2 < 0 or snake[0].y - snake[0].width // 2 < 0:ы
        play = False

    head, bodies = snake[0], snake[2:]
    for body in bodies:
        if body.x < head.x < body.x + body.length and body.y < head.y < body.y + body.width or \
           body.x < head.x + head.length < body.x + body.length and body.y < head.y < body.y + body.width or \
           body.x < head.x < body.x + body.length and body.y < head.y + head.width < body.y + body.width or \
           body.x < head.x + head.length < body.x + body.length and body.y < head.y + head.width < body.y + body.width:
            play = False
            break

    chg_drct()
    snake[0].move()

    move_body_snake()

    if food.side / 2 + food.x > snake[0].x > food.x - food.side / 2\
            and food.side / 2 + food.y > snake[0].y > food.y - food.side / 2:
        food = Food(SNAKE_LENGTH, "apple")
        grow()

    draw.rect(screen, (11, 102, 35), LAND)
    food.appearance()

    for i in range(len(snake)):  # рисуем каждый элемент из списка (каждую часть тела змеи)
        snake[i].appearance()

    display.update()
    clock.tick(75)

display.quit()
