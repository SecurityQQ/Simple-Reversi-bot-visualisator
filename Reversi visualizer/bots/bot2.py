__author__ = 'Alexander Malyshev'

from random import choice

# 0 = black 1 = white -1 = undeffined

map = [
    [-1, -1, -1, -1, -1, -1, -1, -1], #0
    [-1, -1, -1, -1, -1, -1, -1, -1], #1
    [-1, -1, -1, -1, -1, -1, -1, -1], #2
    [-1, 0, -1, 0, 0, 0, 1, -1],      #3
    [-1, 1, -1, -1, -1, -1, -1, -1], #4
    [-1, -1, -1, -1, -1, -1, -1, -1], #5
    [-1, -1, -1, -1, -1, -1, -1, -1], #6
    [-1, -1, -1, -1, -1, -1, -1, -1], #7
    ]

maxcatch = -1

def find_turns(map, y, x, color):
    directions = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]
    availiable_turns = []
    global maxcatch
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
                        distance = max(abs(temp_y-y), abs(temp_x-x))
                        if distance >= maxcatch:
                            print("dist = ", distance)
                            maxcatch = distance
                            availiable_turns.append((temp_y, temp_x))
                            print("turns = ", availiable_turns)

        return(availiable_turns)

def find_mine(map, color):
    list = []
    for i in range(8):
        for j in range(8):
            if map[i][j] == color:
                list.append((i, j))
    if list != []:
        return list

def optimal_turn(map, turns):
    
    turn = choice(turns)
    return turn

def make_turn(map, color=1):
    """Alexander Malyshev"""
    global maxcatch
    maxcatch = -1
    turns = []
    mine_chips = find_mine(map, color)
    for chips in mine_chips:
        turns_for_cords = find_turns(map, chips[0], chips[1], color)
        for t in turns_for_cords:
            turns.append(t)
    if turns != []:
        turn = (optimal_turn(map, turns))
        return turn[1], turn[0]

print(make_turn(map, 1))