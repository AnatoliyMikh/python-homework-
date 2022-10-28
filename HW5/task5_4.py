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
        count = 1
        while i + 1 < len(sample_text) and sample_text[i] == sample_text[i + 1]:
            count += 1
            i += 1
        new_string += str(count) + sample_text[i]
        i += 1
    return new_string

def unzip_text(sample_text):
    count = 0
    i = 0
    new_string = ""
    while i < len(sample_text):
    
        if sample_text[i].isdigit():
            count = int(sample_text[i])
        else:
            new_string += sample_text[i]*count
            count = 0
        i += 1
    return new_string


question = input('You want zip or unzip? (write z/u):')
if question == 'z':
    orig = open_file()
    new_text = str(zip_text(orig))
    write_file(new_text)
    print(new_text)
else:
    orig = open_file()
    new_text = str(unzip_text(orig))
    write_file(new_text)
    print(new_text)