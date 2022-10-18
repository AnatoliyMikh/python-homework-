# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

a = list()
n = int(input('Input N: '))

sum = 0
i = 1

while i<=n:
    a.append((1 + 1 / i)**i)
    i+=1
    sum = sum + a[-1] 

print('sum of numbers = ',sum)