# # Создайте программу для игры с конфетами человек против человека.

# # Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

from random import randint


print("who goes first?")
def bot_step():
    step = randint(1,28)
    return step

def game(param):
    amount = 2021
    while amount > 0:
        if param == 1:
            n = int(input("how many candies you want to take: "))
            param = 2
            amount = amount - n
            i = 1
        else:
            n = bot_step()
            param = 1
            amount = amount - n
            i =2
    if amount == 0 or amount < 0:
        if i == 1:
            print("Exelent! You win!")
        else:    
            print("Sorry, you loose")
        
num_of_player = randint(1,2)
if num_of_player == 1:
    print("You go first")
    game(num_of_player)
else:
    print("I will be first")
    game(num_of_player)








