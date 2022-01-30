import asyncio
from random import randint as rnd
from time import sleep


def game_1():  # создаём функцию для первой игры (game_1)
    print('Загадайте число от 1 до 10,а компьютер попытается отгадать его')  # правила game_1
    b = int(input('Введите количество попыток'))  # переменная, которая будет отвечать за кол-во попыток
    a = list(i for i in range(1, 11))  # создаём список чисел, которые пользователь мог загадать
    for i in range(b):  # повторяем попытки отгадать, пока не закончатся попытки
        index = rnd(0, len(a) - 1)  # случайный индекс для выбора числа из списка
        print(a[index])
        if input('Напишите Ответ ').lower() == 'да':
            break  # заканчиваем цикл
        print('Осталось попыток', b - i - 1)  # счёт попыток
        a.pop(index)  # Удаляем элемент с индексом 'x'


def game_2():  # создаём функцию для второй игры (game_2)
    a = rnd(1, 10)  # переменная которая равно любому числу от 1 до 10
    print('Постарайтесь отгадать число которое загадал компьютер')  # правила game_2
    attempts = int(input('Введите количество попыток'))
    print('Введите число')
    for i in range(attempts):  # вводим количество попыток
        b = int(input())
        if b != a:
            print('Повезёт в следующий раз')
            print('Осталось попыток', attempts - i - 1)  # счет попыток
        else:  # условие к оператору 'if'
            print('Ты угадал,поздравляем!')
            break  # заканчиваем цикл


async def promotion():
    print("hgdf")
    sleep(20)
    await promotion()


def menu():
    while True:  # условие
        print(
            'Чтобы выбрать игру напишите "Загадать число" или "Отгадать число" или "Выход" если хотите выйти из игры')  # опции к игре
        x = input().lower()
        if x == "загадать число":
            game_1()
        elif x == "отгадать число":
            game_2()
        elif x == "выход":
            break  # заканчиваем цикл
        else:
            print('повторите ввод')


if __name__ == "__main__":
    asyncio.run(promotion())
    menu()
