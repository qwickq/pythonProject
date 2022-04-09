from threading import Event, Thread


def a(a_: int, main_event: Event, change_event: Event):
    for i in range(10):
        main_event.wait()
        main_event.clear()
        print(a_)
        change_event.set()


def b(b_: int, main_event: Event, change_event: Event):
    for i in range(10):
        main_event.wait()
        main_event.clear()
        print(b_)
        change_event.set()


event1 = Event()
event2 = Event()

thread1 = Thread(target=a, args=(1, event1, event2))
thread2 = Thread(target=b, args=(2, event2, event1))

thread1.start()
thread2.start()

event1.set()


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


class A:
    def __init__(self):
        self.a = 5
        self.b = 6

    def c(self):
        self.a += 1
        self.b += 2


a = A()
a.b = "Vasya"

f = A()
f.b = "Petya"
