from tkinter import *
from random import *
from time import *
from PIL.Image import *
from PIL.ImageTk import *

import bots

N = 8
DELTA = 10
BOTS = [41, 3]

names = ['', '']


def Check(x, y, dx, dy):
    flag = False
    while 0 <= x < N and 0 <= y < N and field[y][x][0] == (TURN ^ 1):
        flag = True
        x += dx
        y += dy
    return flag and 0 <= x < N and 0 <= y < N and field[y][x][0] == TURN

def PossibleMoves():
    return [(x, y) for x in range(N) for y in range(N) if field[y][x][0] == -1 and any(Check(x + dx, y + dy, dx, dy) for dx in range(-1, 2) for dy in range(-1, 2) if dx or dy)]

def UpdateField():
    counters = [0, 0]
    for x in range(N):
        for y in range(N):
            if field[y][x][0] != -1:
                counters[field[y][x][0]] += 1
                #field[y][x][1] = canvas.create_image(SIZE / N * (x + 0.5), SIZE / N * (y + 0.5), image = IMAGES[field[y][x][0]])
                canvas.delete(field[y][x][1])
                field[y][x][1] = canvas.create_oval(SIZE / N * (x + 0.125), SIZE / N * (y + 0.125), SIZE / N * (x + 0.875), SIZE / N * (y + 0.875), fill = ['black', 'white'][field[y][x][0]])
    Scores.configure(text = 'Black: %3s (%s)\nWhite: %3s (%s)\n%s\'s turn' % (counters[0], names[0], counters[1], names[1], ['Black', 'White'][TURN]))
    window.update()

def Setup():
    global field, TURN
    for color, i in sum(field, []):
        canvas.delete(i)
    field = [[[-1, 1 << 179] for x in range(N)] for y in range(N)]
    TURN = randint(0, 1)
    field[3][3:5], field[4][3:5] = ([[1, 1 << 179], [0, 1 << 179]], [[0, 1 << 179], [1, 1 << 179]]) if TURN else ([[0, 1 << 179], [1, 1 << 179]], [[1, 1 << 179], [0, 1 << 179]])
    UpdateField()

def Turn(event):
    global TURN
    x, y = int(event.x // (SIZE / N)), int(event.y // (SIZE / N))
    if (x, y) not in PossibleMoves():
        return False
    flag = False
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if (dx or dy) and Check(x + dx, y + dy, dx, dy):
                flag, X, Y = True, x + dx, y + dy
                while field[Y][X][0] != TURN:
                    field[Y][X][0] = TURN
                    Y += dy
                    X += dx
    if flag:
        field[y][x][0] = TURN
        TURN ^= 1
    UpdateField()
    if not PossibleMoves():
        TURN ^= 1
        return False
    UpdateField()
    return True

def TurnWithReaction(event):
    if Turn(event) and PossibleMoves():
        #sleep(DELTA / 1000)
        event.x, event.y = map(lambda x: SIZE / N * (x + 0.5), bots.turn(TURN, BOTS[0], [[position[0] for position in line] for line in field]))
        Turn(event)

def PlayBots():
    names[0] = bots.name(BOTS[0])
    names[1] = bots.name(BOTS[1])
    event = Event()
    if PossibleMoves():
        event.x, event.y = map(lambda x: SIZE / N * (x + 0.5), bots.turn(TURN, BOTS[TURN], [[position[0] for position in line] for line in field]))
        Turn(event)
    if PossibleMoves():
        window.after(DELTA, PlayBots)

def MultiPlayer():
    names[0] = 'человек'
    names[1] = 'человек'
    Setup()
    window.bind_all('<Button-1>', Turn)

def SinglePlayer():
    names[0] = 'человек'
    names[1] = bots.name(BOTS[1])
    Setup()
    window.bind_all('<Button-1>', TurnWithReaction)

def ZeroPlayer():
    Setup()
    window.after(DELTA, PlayBots)

window = Tk()
field = []
TURN = 0

WIDTH, HEIGHT = window.winfo_screenwidth(), window.winfo_screenheight()
SIZE = min(WIDTH, HEIGHT)
#IMAGES = [PhotoImage(open('%s.png', x).resize((int((SIZE + N - 1) // N), int((SIZE + N - 1) // N)))) for x in ['black', 'white']] + [PhotoImage(open('blank.png', x).resize((int((SIZE + N - 1) // N), int((SIZE + N - 1) // N))))]

window.title('Reversi')
window.iconphoto(True, PhotoImage(file = 'icon.png'))
window.geometry('%sx%s+0+0' % (WIDTH, HEIGHT))
window.attributes('-fullscreen', True)
window.resizable(width = False, height = False)

LeftFrame = Frame(window, width = (WIDTH - SIZE) // 2, height = HEIGHT)
LeftFrame.pack_propagate(False)
LeftFrame.pack(side = LEFT)
Scores = Label(LeftFrame, padx = 5, justify = 'left', wraplength = (WIDTH - SIZE) // 2, font = ('Arial %s' % (HEIGHT // 63)), text = 'Scores:\nHere should be a lot of information like "ITS %s\' TURN" and so on' % ['BLACKS', 'WHITES'][TURN])
Scores.pack(side = LEFT)

MainFrame = Frame(window, width = SIZE, height = HEIGHT)
MainFrame.pack_propagate(False)
MainFrame.pack(side = LEFT)
canvas = Canvas(MainFrame, height = SIZE, width = SIZE)
canvas.pack(side = TOP)

for x in range(N - 1):
    canvas.create_line(0, SIZE / N * (x + 1), SIZE, SIZE / N * (x + 1), width = 2)
    canvas.create_line(SIZE / N * (x + 1), 0, SIZE / N * (x + 1), SIZE, width = 2)

RightFrame = Frame(window, width = (WIDTH - SIZE) // 2, height = HEIGHT)
RightFrame.pack_propagate(False)
RightFrame.pack(side = LEFT)
MultiPlayerGameButton = Button(RightFrame, text = '2 players', width = (WIDTH - SIZE) // 2, padx = 5, font = ('Arial %s' % (HEIGHT // 50)), command = MultiPlayer)
SinglePlayerGameButton = Button(RightFrame, text = '1 player', width = (WIDTH - SIZE) // 2, padx = 5, font = ('Arial %s' % (HEIGHT // 50)), command = SinglePlayer)
ZeroPlayerGameButton = Button(RightFrame, text = 'Watch bots', width = (WIDTH - SIZE) // 2, padx = 5, font = ('Arial %s' % (HEIGHT // 50)), command = ZeroPlayer)
MultiPlayerGameButton.pack()
SinglePlayerGameButton.pack()
ZeroPlayerGameButton.pack()

window.mainloop()
