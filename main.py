from pip._vendor.progress import counter
from pipenv.vendor.orderedmultidict import f

a: int = 5
b = a + 6
c = b - 3
d = 4.66
t: int = 3615
s = ['xyz']

print(a, b, c, d, t, s)
print('a + b - c =', a + b - c)
print(a)
print(type(a))

print(s)
print(type(s))

print(d)
print(type(d))

time = int(input('Введите время в секундах'))
m = time // 60
if m < 60:
    pass
else:
    var: int = m % 60
s: int = time % 60
i = time // 60
h = i // 60
print('Время в часах', h, ':', m, ':', s)

g = int(input("Введите любое однозначное число: "))
print('a + aa + aaa =', g + g * 11 + g * 111)

a = int(input('Введите число'))
m = a % 10
a = a // 10
while a > 0:
    if a % 10 > m:
        m = a % 10
    a = a // 10
print(m)

data = int(input('Прибыль'))
data1 = int(input('Себестоимость'))
data2 = int(input('Численность сотрудников'))
salary = (data - data1) / data2

if data > data1:
    print('Бизнес рентабелен')
    print('Зарплата', salary, type(salary))
else:
    print('Бизнес не рентабелен')

print('Результативность спортсмена')
x = 2
y = 3
z = x / 10
while x < y:
    print('день - {:.2f}'.format(x))
    x = x + z
    print(days(x))
print('Программа завершена')
