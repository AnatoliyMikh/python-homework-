# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

i=0
k = int(input('input k:'))
sp = list()
while i < 20:
    t = int(random.uniform(0,100)) 
    sp.append(t)
    i += 1
print(str(sp))                          # просмотр полученного списка случайных чисел

s = str(f'{random.choice(sp)}*x^{k}+')

p = k
j = 0
while j < p:
    if k > 0:
        s += str(f'{random.choice(sp)}x^{k-1}+')
        j += 1
        k -= 1
    else:
        s += str(f'{random.choice(sp)}=0')

# s = s.rstrip(s[-1])+' = 0'

print(s)
