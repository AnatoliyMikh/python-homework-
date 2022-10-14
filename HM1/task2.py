# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Input x: '))
y = int(input('Input y: '))
z = int(input('Input z: '))

first = not (x or y or z)
second = not x and not y and not z

if first == second:
    print('true')
else:
    print('false')