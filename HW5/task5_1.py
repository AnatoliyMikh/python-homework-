# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def edit_text(text):
    t = text.split(" ")
    new_text = []
    for i in range (len(t)):
        if (lambda t:('а' or 'б' or 'в') in t[i]) == False:
            new_text += t[i]
    return new_text

sample_text = input('Input sample text: ')
print('Original text:', sample_text)
print(edit_text(sample_text))