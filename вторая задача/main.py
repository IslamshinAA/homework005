# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import random
total = 200
player = 'Пользователь'
# player2 = 'Пользователь №2'
print(f"На столе {total} конфет")
def test_enter(name) -> int:
    a = int(input(f'{name}, возьмите конфеты: '))
    while 0 <= a > 28: # проверка на число
      a = int(input(f'{name} Возьмите конфеты. (За один ход можно забрать не более чем 28 конфет!) : '))
    return a

def bot_calc(tot) ->int:
    a =  random.randint(1,29)
    while tot-a < 28 and tot > 30 :  # умный бот
        a = random.randint(1,29)
    return a

flag = random.randint(1,3)
while total > 28:
    if flag == 1:
        candy = test_enter(player)
        total -= candy
        flag = 2
        print(f'Ты взял {candy} конфет. Количество оставшихся конфет {total}')
    else:
        candy = bot_calc(total) # random.randint(1,29) честная игра или test_enter(player2) два пользователя
        total -= candy
        flag = 1
        print(f'Бот взял {candy} конфет. Количество оставшихся конфет {total}')
if flag == 1:
    print(f'А ты хорош!Победа! ')
else:
    print(f'Бот забрал {total} и победил тебя ')