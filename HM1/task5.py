# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math


xa = int(input('Input x(A): '))

ya = int(input('Input y(A): '))

xb = int(input('Input x(B): '))

yb = int(input('Input y(B): '))

result = float(math.sqrt((xb-xa)**2+(yb-ya)**2))

print (f'{str(result)[:4]}')
