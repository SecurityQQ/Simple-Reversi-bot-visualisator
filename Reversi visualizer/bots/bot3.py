"""PuzzleBot"""
__author__ = 'Puzzletime'
from random import choice
from pprint import pprint



def find_possible(maps, x, y, color):
    offset = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
    x2, y2 = x, y
    warrior = 0
    if color == 0: warrior = 1
    possible = []

    if maps[y][x] == -1:
        for x_off, y_off in offset:
            x2 = x + x_off
            y2 = y + y_off
            counter = 0
            finding = True

            while (x2 >= 0) and (x2 <= 7) and (y2 >= 0) and (x2 <= 7) and finding:
                try:
                    if maps[y2][x2] == color:
                        finding = False
                        if counter > 0:
                            possible.append([x, y, counter])
                    elif maps[y2][x2] == warrior:
                        x2 += x_off
                        y2 += y_off
                        counter += 1
                    else:
                        finding = False
                except:
                    finding = False
    return possible



def make_turn(maps, indicator):
    possible = []

    for y in range(8):
        for x in range(8):
            p = find_possible(maps, x, y, indicator)
            if len(p) > 0:
                possible.append(p)

    for p in possible:
        if ((p[0][0] == 0) or (p[0][0] == 7)) and\
                (p[0][0] == p[0][1]):
            p[0][2] *= 2
        elif (p[0][0] == 0) or (p[0][0] == 7) or\
                (p[0][1] == 0) or (p[0][1] == 7):
            p[0][2] *= 1.5

    last_p = [possible[0][0]]
    for p in possible:
        if p[0][2] > last_p[0][2]:
            last_p = [p[0]]
        elif p[0][2] == last_p[0][2]:
            last_p.append(p[0])

    p = choice(last_p)
    return p[0], p[1]






MAP_TEST = [
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1,  0,  1, -1, -1, -1],
    [-1, -1, -1,  1,  0, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1],
]

turn = make_turn(MAP_TEST, 0)
print(turn)