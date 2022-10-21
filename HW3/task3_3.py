# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19 
def max_num(a):
    max_=a[0]

    i=0

    while i < len(a):
        if max_ < a[i]:
            max_ = a[i]
        i += 1
    
    return max_

def min_num(b):
    min_=b[0]

    i=0

    while i > len(b):
        if min_ > b[i]:
            min_ = b[i]
        i += 1
    
    return min_


list1 = [1.1, 1.2, 3.1, 5, 10.01]
result = max_num(list1) - min_num(list1)

print(result%100)





