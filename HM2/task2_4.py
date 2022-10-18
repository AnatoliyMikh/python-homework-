# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

a = int(input('input start point(-N): '))
b = int(input('input end point(N): '))

i = a
sp = list()

for i in range(a, b+1):
    sp.append(i)

print(sp, end=" ")

c = sp [8]
d = sp [11]


if c != 0 or d != 0:
    work = c * d
    print('Work of numbers is: ', work)
else:
    print('there is(are) no number(s) on the positions')