from pip._vendor.progress import counter
from pipenv.vendor.orderedmultidict import f

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