# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


def file_1():
    f = open("task5_pol1.txt", "r", encoding="UTF-8")
    a = f.read()
    f.close()
    return a


def file_2():
    f = open("task5_pol2.txt", "r", encoding="UTF-8")
    b = f.read()
    f.close()
    return b

def addition_file(pol):
    f = open("task5_final.txt", "w", encoding="UTF-8")
    f.write(pol)
    f.close()


def operation(a, b):
    sum = list()
    d = len(a) 
    i = 0
    while i < d:
        sum.append(int(a[i])+ int(b[i]))
        i +=6
    pol = str(f'{sum[0]}*x^{a[4]}+{sum[1]}*x^{a[10]}+{sum[2]}=0')
    return pol

mn_1 = file_1()
print("многочлен 1:", mn_1)

mn_2 = file_2()
print("многочлен 2:", mn_2)

koef = operation(mn_1, mn_2)
addition_file(koef)
print("сумма:", koef)
