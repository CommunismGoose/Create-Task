from random import random
import tkinter as tk
from tkinter import messagebox
import time

starttime = time.time()

#generate sx by sy minesweeper board with mines placed with probablity of prob
def createBoard(sx, sy, prob):
    board = []
    for i in range(sy):
        row = []
        for j in range(sx):
            row.append(random() < prob)
        board.append(row)
    return board

def printMines(board):
    letters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dimx = len(board[0])
    dimy = len(board)
    print("  " + " ".join([letters[x] for x in range(dimx)]))
    for i in range(dimy):
        t = letters[i]
        for j in range(dimx):
            t += " X" if board[i][j] else " ."
        print(t)

def calcDangerous(board):
    dimx = len(board[0])
    dimy = len(board)
    ret = createBoard(dimx, dimy, 0) #board to change and return

    for i in range(dimy):
        for j in range(dimx):
            for y in range(-1, 2):
                for x in range(-1, 2):
                    addx = j + x
                    addy = i + y
                    if not (x == y == 0) and addx >= 0 and addx < dimx and addy >= 0 and addy < dimy:
                        ret[addy][addx] += board[i][j]

    return ret

def copylist(l1, l2):
    for i in range(len(l2)):
        for j in range(len(l2[0])):
            l1[i][j] = l2[i][j]

def fill(posx, posy, dimx, dimy, danger, btn, safeopened):
    if posx < 0 or posx >= dimx or posy < 0 or posy >= dimy:
        return

    index = posy * dimx + posx
    if btn[index]["state"] == tk.DISABLED:
        return

    d = danger[posy][posx]
    
    btn[index]["text"] = "" if d==0 else d
    btn[index]["background"] = ["lightgoldenrodyellow", "lightgoldenrod", "orange", "lightcoral", "IndianRed1", "PaleVioletRed1", "MediumOrchid1", "MediumPurple1", "alice blue"][d]
    btn[index]["state"] = tk.DISABLED
    safeopened[0] += 1
    
    if d != 0:
        return

    for y in range(-1, 2):
        for x in range(-1, 2):
            addx = posx + x
            addy = posy + y
            if not (x == y == 0):
                fill(addx, addy, dimx, dimy, danger, btn, safeopened)

def buttonPress(root, posx, posy, dimx, dimy, board, danger, btn, firstmove, prob, totalsafe, safeopened):
    index = posy * dimx + posx

    if firstmove[0]:
        copylist(board, createBoard(dimx, dimy, prob))

        for i in range(-1, 2):
            for j in range(-1, 2):
                addx = posx + j
                addy = posy + i
                if addx >= 0 and addx < dimx and addy >= 0 and addy < dimy:
                    board[addy][addx] = False

        totalsafe[0] = sum([row.count(False) for row in board])
        copylist(danger, calcDangerous(board))
        firstmove[0] = False
    if board[posy][posx]:
        btn[index]["background"] = "red"
        messagebox.showinfo("You lost!", "You hit a mine! Bye bye! >:)")
        root.quit()
    else:
        fill(posx, posy, dimx, dimy, danger, btn, safeopened)
        if safeopened[0] >= totalsafe[0]:
            wowt = '%.2f'%(time.time() - starttime)
            messagebox.showinfo("You won!", "You found all the safe squares in " + str(wowt) + " seconds, good job! :)")
            root.quit()


def toggleFlag(event, x, y, dimx, dimy, flags, btn):
    index = y * dimx + x
    if btn[index]["state"] == tk.DISABLED and not flags[y][x]:
        return
    if flags[y][x]:
        flags[y][x] = False
        btn[index]["state"] = tk.ACTIVE
        btn[index]["background"] = "#aaddaa" if random() < 0.5 else "#aaccaa"
        btn[index]["text"] = ""
    else:
        flags[y][x] = True
        btn[index]["state"] = tk.DISABLED
        btn[index]["background"] = "#8888FF"
        btn[index]["text"] = "Flag"

def Minesweeper(width, height, prob):
    global flagImage

    wwidth = width * 36
    wheight = height * 36

    #make master window
    root = tk.Tk()
    root.title("Game Catalog - Minesweeper")
    root.configure(background = "antiquewhite")
    #put the window in the upper left corner of the screen with set dimensions
    #root.geometry(str(wwidth)+"x"+str(wheight)+"+-7+0")
    root.geometry(str(wwidth)+"x"+str(wheight)+"+400+200")
    #make the window unresizeable
    root.minsize(wwidth, wheight) 
    root.maxsize(wwidth, wheight)

    board = createBoard(width, height, 0)
    danger = createBoard(width, height, 0)
    flags = createBoard(width, height, 0)

    totalsafe = [0]
    safeopened = [0]

    firstmove = [True]

    btn = []
    for i in range(height):
        for j in range(width):
            btn.append(tk.Button(root, background="#aaddaa" if random() < 0.5 else "#aaccaa", width=4, height=2, text="",
                                 command=lambda cx=j, cy=i: buttonPress(root, cx, cy, width, height, board, danger, btn, firstmove, prob, totalsafe, safeopened)))
            btn[i*width+j].place(x=j*36, y=i*36)
            btn[i*width+j].bind("<Button-3>", lambda event=0, cx=j, cy=i: toggleFlag(event, cx, cy, width, height, flags, btn))

    root.mainloop()
    #root.destroy()

#Minesweeper(12, 12, 0.15)
