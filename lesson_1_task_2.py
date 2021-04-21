<<<<<<< HEAD
from pip._vendor.progress import counter
from pipenv.vendor.orderedmultidict import f
=======
>>>>>>> branch

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
<<<<<<< HEAD
print(f'Время в часах: {h}:{m}:{s}')
=======
print(f'Время в часах: {h:02d}:{m:02d}:{s:02d}')
>>>>>>> branch
