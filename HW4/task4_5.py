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

# def operation(c):
#     c = str(c.split("*"))
#     # c = c.rstrip("=0")
#     return c



mn_1 = str(file_1())
mn_1 = mn_1.rstrip("=0")
mn_1  = mn_1.split('*')

print(mn_1)

mn_2 = str(file_2())
# print(mn_2)

