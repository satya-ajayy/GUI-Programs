from tkinter import *


def callback(r, c):
    global player
    if player == 'X' and states[r][c] == 0 and stop_game is False:
        b[r][c].configure(text='X', fg='blue', bg='red')
        states[r][c] = 'X'
        player = 'O'
    if player == 'O' and states[r][c] == 0 and stop_game is False:
        b[r][c].configure(text='O', fg='orange', bg='#9EFD38')
        states[r][c] = 'O'
        player = 'X'
    check_for_winner()


def check_for_winner():
    global stop_game
    for val in range(3):
        if states[val][0] == states[val][1] == states[val][2] != 0:
            b[val][0].configure(text='WIN', bg='black')
            b[val][1].configure(text='FOR', bg='black')
            b[val][2].configure(text=str(states[val][0]) + "!!!", bg='black')
            stop_game = True
    for val in range(3):
        if states[0][val] == states[1][val] == states[2][val] != 0:
            b[0][val].configure(text='WIN', bg='black')
            b[1][val].configure(text='FOR', bg='black')
            b[2][val].configure(text=str(states[0][val]) + "!!!", bg='black')
            stop_game = True
    if states[0][0] == states[1][1] == states[2][2] != 0:
        b[0][0].configure(text='WIN', bg='black')
        b[1][1].configure(text='FOR', bg='black')
        b[2][2].configure(text=str(states[0][0]) + "!!!", bg='black')
        stop_game = True
    if states[2][0] == states[1][1] == states[0][2] != 0:
        b[2][0].configure(text='WIN', bg='black')
        b[1][1].configure(text='FOR', bg='black')
        b[0][2].configure(text=str(states[0][2]) + "!!!", bg='black')
        stop_game = True


root = Tk()
root.title("Tic-Tac-Toe")
b = [[0 for _ in range(3)] for _ in range(3)]
states = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
for i in range(3):
    for j in range(3):
        b[i][j] = Button(font=('Verdana', 56), width=3, borderwidth=3, bg='yellow')
        b[i][j].configure(command=lambda r=i, c=j: callback(r, c))
        b[i][j].grid(row=i, column=j)
player = 'X'
stop_game = False
mainloop()
