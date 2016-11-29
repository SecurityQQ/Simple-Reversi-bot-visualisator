"""My bot""" # <-- INSERT YOUR BOT NAME HERE

from random import choice
# IMPORT ANYTHING YOU NEED

__all__ = ['make_turn']

def Check(x, y, dx, dy, field, color):
    flag = False
    while 0 <= x < len(field) and 0 <= y < len(field) and field[y][x] == (color ^ 1):
        flag = True
        x += dx
        y += dy
    return flag and 0 <= x < len(field) and 0 <= y < len(field) and field[y][x] == color

def PossibleMoves(field, color):
    return [(x, y) for x in range(len(field)) for y in range(len(field)) if field[y][x] == -1 and any(Check(x + dx, y + dy, dx, dy, field, color) for dx in range(-1, 2)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    for dy in range(-1, 2) if dx or dy)]

def make_turn(field, color):
    return choice(PossibleMoves(field, color))
