# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input('Input natural number: '))

i=1
t=0
nat = list()
for i in range (i, num+1):
    t = num % i
    if t == 0:
        nat.append(i)

print("Simple multipliers of number ",num, "is: ", nat )