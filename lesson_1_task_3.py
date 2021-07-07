<<<<<<< HEAD
<<<<<<< HEAD
from pip._vendor.progress import counter
from pipenv.vendor.orderedmultidict import f

print("Задача 3.")
g = int(input("Введите любое однозначное число: "))
if g >= 0:
    print(f'{g}+{g}{g}+{g}{g}{g}=', g + g * 11 + g * 111)
=======
=======
>>>>>>> e487f2b74c4055cb30724a8ecdf27802fb2f3629

print("Задача 3.")

g = input("Введите любое однозначное число: ")

if '-' not in g:
    g1 = int(g)
    g2 = int(g + g)
    g3 = int(g + g + g)
    print(f'{g}+{g}{g}+{g}{g}{g}=', g1 + g2 + g3)
<<<<<<< HEAD
>>>>>>> branch
=======
>>>>>>> e487f2b74c4055cb30724a8ecdf27802fb2f3629
else:
    print("Число должно быть положительным.")
