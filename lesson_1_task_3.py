
print("Задача 3.")

g = input("Введите любое однозначное число: ")

if '-' not in g:
    g1 = int(g)
    g2 = int(g + g)
    g3 = int(g + g + g)
    print(f'{g}+{g}{g}+{g}{g}{g}=', g1 + g2 + g3)
else:
    print("Число должно быть положительным.")
