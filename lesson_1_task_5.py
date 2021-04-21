<<<<<<< HEAD
from pip._vendor.progress import counter
from pipenv.vendor.orderedmultidict import f
=======
>>>>>>> branch

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