# Написать программу, которая считывает несколько чисел и выводит среднее арифметическое этих чисел
a = list(map(int, input().split()))

a.__add__([523, 1243])

# print(sum(a) / len(a))

"""
def task3():
    a = int(input())
    b = 1
    while a > 1:
        b = b * a
        a = a - 1
    print(b)


def fac(a):
    if a == 0:
        return 1
    return fac(a - 1) * a


# print(fac(5))

a = list(map(int, input().split()))
for x in a:  # for i in range(len(a)):
    if x % 2 == 0:  # if a[i] % 2 == 0:
        print(x)

# 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = []
for i in range(1, 11):
    a.append(i)

a = list(i for i in range(1, 11))
"""
