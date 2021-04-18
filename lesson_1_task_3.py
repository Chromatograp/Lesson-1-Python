from pip._vendor.progress import counter
from pipenv.vendor.orderedmultidict import f

print("Задача 3.")
g = int(input("Введите любое однозначное число: "))
if g >= 0:
    print(f'{g}+{g}{g}+{g}{g}{g}=', g + g * 11 + g * 111)
else:
    print("Число должно быть положительным.")
