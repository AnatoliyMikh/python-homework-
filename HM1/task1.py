# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

result = int(input('Input number weekday: '))

if result == 6 or result == 7:
    print('true')
elif result == 1 or result == 2 or result == 3 or result == 4 or result == 5:
    print('False')
else:
    print('False. Only 7 days in a week')