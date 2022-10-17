# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from re import I


n = int(input('Input number: '))
sum =1
i = 1

while i <= n:
    sum=sum*i
    i+=1
print('Summ of digits= ',sum)