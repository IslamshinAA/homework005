# Создайте программу для игры в ""Крестики-нолики"".
import random

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8 ]
player = 'X'
player1 = 'o'

def field(cells):
    print("f\t _____________")
    print(f"\t | {cells[0]} | {cells[1]} | {cells[2]} |")
    print(f"\t |___|___|___|")
    print(f"\t | {cells[3]} | {cells[4]} | {cells[5]} |")
    print(f"\t |___|___|___|")
    print(f"\t | {cells[6]} | {cells[7]} | {cells[8]} |")
    print(f"\t |___|___|___|")

def move_enter(name) -> int:
    a = int(input(f'{name}, сделайте ход (цифры от 1 до 9: '))
    while 1 <= a > 8:
      a = int(input(f'{name} Такой позиции в поле не существует  : '))
    return a
def win(res):
    x = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8))
    for i in x:
        if res[i[0]] == res[i[1]] == res[i[2]]:
            return res[i[0]]
        return False

flag_rand = random.randint(1,3)

