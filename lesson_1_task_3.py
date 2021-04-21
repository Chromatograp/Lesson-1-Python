<<<<<<< HEAD
from pip._vendor.progress import counter
from pipenv.vendor.orderedmultidict import f

print("Задача 3.")
g = int(input("Введите любое однозначное число: "))
if g >= 0:
    print(f'{g}+{g}{g}+{g}{g}{g}=', g + g * 11 + g * 111)
=======

print("Задача 3.")

g = input("Введите любое однозначное число: ")

if '-' not in g:
    g1 = int(g)
    g2 = int(g + g)
    g3 = int(g + g + g)
    print(f'{g}+{g}{g}+{g}{g}{g}=', g1 + g2 + g3)
>>>>>>> branch
else:
    print("Число должно быть положительным.")
