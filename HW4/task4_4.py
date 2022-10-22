# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

list2 = str(input('Input some list: '))
find_elem = input('Input find element: ')

list1 = list2.split(" ")
l = len(list1)

m = list1.count(find_elem)
if m > 1:
    el1 = list1.index(find_elem, 0, l)
    el2 = list1.index(find_elem, el1+1, l)
    print('list: ', list1, 'find: ', find_elem, 'answer: ', el2)
else:
    print('list: ', list1, 'find: ', find_elem, 'answer: ', -1)


