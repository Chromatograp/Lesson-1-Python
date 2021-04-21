<<<<<<< HEAD
from pip._vendor.progress import counter
from pipenv.vendor.orderedmultidict import f
=======
>>>>>>> branch

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
