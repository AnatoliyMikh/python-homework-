# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Input number: '))
n = list()

while num > 0:
    a = num % 2
    n.append(a)
    num = num // 2
n.reverse()

print(n)