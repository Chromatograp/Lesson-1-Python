from pip._vendor.progress import counter
from pipenv.vendor.orderedmultidict import f

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
