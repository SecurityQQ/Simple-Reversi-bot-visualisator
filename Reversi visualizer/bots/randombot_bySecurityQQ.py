__author__ = 'Alexander Malyshev'


from random import choice

# 0 = black 1 = white -1 = undeffined


def find_turns(map, y, x, color):
    directions = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]
    availiable_turns = []
    if map[y][x] == color:
        for i, j in directions:
            temp_y = y + i
            temp_x = x + j
            while 0 <= temp_y <= 7 and 0 <= temp_x <= 7:
                    if map[temp_y][temp_x] == (not color):
                        temp_y+=i
                        temp_x+=j
                    else:
                        break
            if 0 <= temp_y <= 7 and 0 <= temp_x <= 7:
                if (temp_y, temp_x) != (y + i, x +j):
                    if map[temp_y][temp_x] != color:
                        availiable_turns.append((temp_y, temp_x))
        return(availiable_turns)

def find_mine(map, color):
    list = []
    for i in range(8):
        for j in range(8):
            if map[i][j] == color:
                list.append((i, j))
    if list != []:
        return list

def optimal_turn(turns):

    return turn

def make_turn(map, color=1):
    """Alexander Malyshev"""
    turns = []
    mine_chips = find_mine(map, color)
    for chips in mine_chips:
        turns_for_cords = find_turns(map, chips[0], chips[1], color)
        for t in turns_for_cords:
            turns.append(t)
    if turns != []:
        turn = (optimal_turn(turns))
        return turn[1], turn[0]