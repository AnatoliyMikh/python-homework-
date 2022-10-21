# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def sp(a):

    i = 0
    j = len(a)-1
    sum = list()

    while i <= j:
        sl = int(a[i])*int(a[j])
        sum.append(sl)
        j -= 1
        i += 1
    return sum
    
print(sp(input('input some list: ')))