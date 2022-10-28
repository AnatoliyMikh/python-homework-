# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.

def open_file():
    f = open('5_1_input.txt', 'r', encoding='UTF-8')
    value = f.read()
    f.close()
    return value

def write_file(text):
    f = open('5_2_output.txt', 'w', encoding='UTF-8')
    f.write(text)
    f.close()
    
def zip_text(sample_text):
    new_string = "" 
    i = 0
    while i < len(sample_text):
        # подсчитывает количество вхождений символа в индексе `i`
        count = 1
 
        while i + 1 < len(sample_text) and sample_text[i] == sample_text[i + 1]:
            count = count + 1
            i = i + 1
        new_string += str(count) + sample_text[i]
        i = i + 1
 
    return new_string

question = input('You want zip or unzip? (write z/u):')
if question == 'z':
    orig = open_file()
    new_text = str(zip_text(orig))
    write_file(new_text)
    print(new_text)
else:
    orig = open_file()