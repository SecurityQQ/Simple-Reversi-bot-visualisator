"""Bot By A.Malyshev"""
__author__ = 'Alexander Malyshev'

from random import choice

# 0 = black 1 = white -1 = undeffined

map = [
    [-1, -1, -1, -1, -1, -1, -1, -1], #0
    [-1, 1, -1, -1, -1, -1, -1, -1], #1
    [-1, 0, -1, -1, -1, -1, -1, -1], #2
    [-1, 0, -1, 0, 0, 0, 1, -1],      #3
    [-1, 0, -1, -1, -1, -1, -1, -1], #4
    [-1, -1, -1, -1, -1, -1, -1, -1], #5
    [-1, -1, -1, -1, -1, -1, -1, -1], #6
    [-1, -1, -1, -1, -1, -1, -1, -1], #7
    ]
map = [[1, 1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 1, 1, 1, 1, 0],
       [1, 1, 0, 0, 1, 1, 0, 0],
       [1, 1, 0, 0, 1, 1, 0, 0],
       [1, 1, 0, 0, 0, 0, 0, 0],
       [1, 1, 1, 1, 1, -1, 0, 1],
       [1, 1, 1, 1, 1, 1, 0, 1]]


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
                            #print("dist = ", distance)
                            maxcatch = distance
                            availiable_turns.append((temp_y, temp_x))
                            #print("turns = ", availiable_turns)

        return(availiable_turns)
def deletedublicates(list):
    new_list=[]
    for l in list:
        if l not in new_list:
            new_list.append(l)
    return new_list

def find_mine(map, color):
    list = []
    for i in range(8):
        for j in range(8):
            if map[i][j] == color:
                list.append((i, j))
    if list != []:
        return list

def optimal_turn(map, turns, color):
    corners = [(0, 0), (0, 7), (7, 0), (7, 7)]
    turns2 = []
    turns1 = []
    for turn in turns:
        if turn in corners:
            return turn
    else:
        for corner in corners:
          for turn in turns:
            if map[corner[0]][corner[1]] == (color ^ 1):
                if corner[0] in turn or corner[1] in turn:
                    turns2.append(turn)
                    break
            else:
              if turn not in turns1: turns1.append(turn)
    print(turns1)
    if turns1 != []: return choice(turns1)
    else: return choice(turns2)

def make_turn(map, color):
    print(map)
    if color == 0:
        print("black")
    else:
        print("white")
    global maxcatch
    maxcatch = -1
    turns = []
    mine_chips = find_mine(map, color)
    for chips in mine_chips:
        turns_for_cords = find_turns(map, chips[0], chips[1], color)
        for t in turns_for_cords:
            turns.append(t)
    if turns != []:
        turn = (optimal_turn(map, turns, color))
        #return turn[0], turn[1]
        return turn[1], turn[0]
print(make_turn(map, 1))