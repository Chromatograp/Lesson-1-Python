from pip._vendor.progress import counter
from pipenv.vendor.orderedmultidict import f

print("Задача 1.")
a: int = 5
b = a + 6
c = b - 3
d = 4.66
t: int = 3615
s = ['xyz']

print("Созданные переменные: а -", a, "; b -", b, "; c -", c, "; d -", d, "; t -", t, "; s -", s)

print("Переменная a -", a)
print("Класс переменной а -", type(a))

print("Переменная s -", s)
print("Класс переменной s -", type(s))

print("Переменная d -", d)
print("Класс переменной d -", type(d))
print('a+b-c=', a + b - c)

name = input("Введите свое имя:")
age = int(input("Введите свой возраст:"))
print("Вас зовут", name, "и вам", age, "лет.")
