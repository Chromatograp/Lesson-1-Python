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

print("Задача 2.")
time = int(input('Введите время в секундах: '))
m = time // 60
if m < 60:
    pass
else:
    m = m % 60

s: int = time % 60
i = time // 60
h = i // 60
print(f'Время в часах: {h}:{m}:{s}')

print("Задача 3.")
g = int(input("Введите любое однозначное число: "))
if g >= 0:
    print(f'{g}+{g}{g}+{g}{g}{g}=', g + g * 11 + g * 111)
else:
    print("Число должно быть положительным.")

print("Задача 4.")
a = int(input('Введите целое положительное многозначное число: '))
if a > 0:
    m = a % 10
    a = a // 10
    while a > 0:
        if a % 10 > m:
            m = a % 10
            a = a // 10
    print("Самая большая цифра в вашем числе ", m)
else:
    print("Число должно быть положительным.")

print("Задача 5.")
profit = int(input('Прибыль '))
cost_price = int(input('Себестоимость '))
number = int(input('Численность сотрудников '))
salary = (profit - cost_price) / number

if profit > cost_price:
    print('Бизнес рентабелен.')
    print('Выручка - ', profit - cost_price)
    print("Зарплата %.2f" % salary)
else:
    print('Бизнес не рентабелен.')
    print('Убыток - ', cost_price - profit)

print("Задача 6.")
print('Результативность бега.')
first = int(input('Введите начальный результат: '))
last = int(input('Введите желаемый результат: '))
grow = int(input('Введите, на какой процент вы собираетесь увеличивать результат: '))
d = 0
while first <= last:
    d += 1
    print(d, 'день - {:.2f}'.format(first))
    first = first + (first / grow)

print('Вы достигнете желаемого результата', last, 'километров на', d + 1, 'день.')
