# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

sample_text = input('Input sample text: ')

print('Original text:', sample_text)

print(edit_text(sample_text))

def edit_text(text):
    t = text.split(" ")
    