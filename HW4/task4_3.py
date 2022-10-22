# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

list1 = input('input subsequence: ')
list2 = list()

i = 0
d = len(list1)-1
for i in range (i, d):
    if list1.count(list1[i]) == 1:
            list2.append(list1[i])

print('input subsequence:',list1,';','not repeating elements: ',list2) 