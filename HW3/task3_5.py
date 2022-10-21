# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = input('Input number: ')
n = int(n)

num1 = 1
num2 = 1
res1 = list() 

i = 2 
while i < n:
    num_sum = num2 + num1
    res1.append(num_sum)
    num1 = num2
    num2 = num_sum
    i += 1
 
print (res1)