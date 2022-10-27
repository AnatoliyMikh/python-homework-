# Напишите программу, удаляющую из текста все слова, содержащие "абв".

def filter_text(text):
    t = text.split(" ")
    i=0
    stop_list = []
    for word in t:
        if "а" in word:    
            stop_list.append(word)
        if "б" in word:    
            stop_list.append(word)
        if "в" in word:    
            stop_list.append(word)
    return stop_list

sample_text = input('Input sample text: ')
edit = sample_text.split()
new_text = filter_text(sample_text)
final_text = " ".join(filter(lambda word: word not in new_text, edit))
print('Original text:', sample_text)
print('filtered_text:', final_text)