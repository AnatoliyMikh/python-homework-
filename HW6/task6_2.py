# Напишите программу, удаляющую из текста все слова содержащие "абв".

text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
    этого абв текста все вабвс слова, содерабващие содержащие "абв"'

def del_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(my_text)

text = del_words(text)
print(text)